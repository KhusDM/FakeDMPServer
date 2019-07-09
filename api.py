import pandas as pd
import math
import uuid
from random import randint
from collections import defaultdict
from app import app, db
from app.models import User

if (__name__ == "__main__"):
    app.run(debug=True)


def generate_data(count_rows):
    attributes = {"sd_gender": {"value": None, "start_interval": 10000, "end_interval": 10002},
                  "sd_age_estimated": {"value": None, "start_interval": 10000, "end_interval": 10013},
                  "sd_living_country": {"value": None, "start_interval": 10177, "end_interval": 10177},
                  "sd_job_profession": {"value": None, "start_interval": 10000, "end_interval": 10436},
                  "sd_job_pos_category": {"value": None, "start_interval": 10000, "end_interval": 10004},
                  "fin_acc_balance_avg_3m": {"value": None, "start_interval": 10000, "end_interval": 10986},
                  "sd_marital_status": {"value": None, "start_interval": 10000, "end_interval": 10005},
                  "sd_children": {"value": None, "start_interval": 10000, "end_interval": 10006},
                  "real_estate_owner_type": {"value": None, "start_interval": 10000, "end_interval": 10008},
                  "leisure_hobby": {"value": None, "start_interval": 10000, "end_interval": 10021},
                  "consumerelectronics_owner_type": {"value": None, "start_interval": 10000, "end_interval": 10039},
                  "consumerelectronics_interest_type": {"value": None, "start_interval": 10000, "end_interval": 10039},
                  "car_owner_count": {"value": None, "start_interval": 10000, "end_interval": 10003},
                  "insurance_user": {"value": None, "start_interval": 10000, "end_interval": 10011},
                  "insurance_interest": {"value": None, "start_interval": 10000, "end_interval": 10011},
                  }
    # users = []
    for i in range(count_rows):
        id = str(uuid.uuid4())
        for key in attributes.keys():
            attribute_type = attributes_taxonomy[attributes_taxonomy["Name"] == key]["Type"].tolist()[0]
            try:
                if (attribute_type != "D-Currency"):
                    attributes[key]["value"] = dictionary_taxonomy[attribute_type][
                        randint(attributes[key]["start_interval"], attributes[key]["end_interval"])]
                else:
                    attributes[key]["value"] = randint(15000, 150000)
            except:
                attributes[key]["value"] = dictionary_taxonomy[attribute_type][10000]

        user = User(id=id, sd_gender=attributes["sd_gender"]["value"],
                    sd_age_estimated=attributes["sd_age_estimated"]["value"],
                    sd_living_country=attributes["sd_living_country"]["value"],
                    sd_job_profession=attributes["sd_job_profession"]["value"],
                    sd_job_pos_category=attributes["sd_job_pos_category"]["value"],
                    fin_acc_balance_avg_3m=attributes["fin_acc_balance_avg_3m"]["value"],
                    sd_marital_status=attributes["sd_marital_status"]["value"],
                    sd_children=attributes["sd_children"]["value"],
                    real_estate_owner_type=attributes["real_estate_owner_type"]["value"],
                    leisure_hobby=attributes["leisure_hobby"]["value"],
                    consumerelectronics_owner_type=attributes["consumerelectronics_owner_type"]["value"],
                    consumerelectronics_interest_type=attributes["consumerelectronics_interest_type"]["value"],
                    car_owner_count=attributes["car_owner_count"]["value"],
                    insurance_user=attributes["insurance_user"]["value"],
                    insurance_interest=attributes["insurance_interest"]["value"]
                    )

        # users.append(user)
        db.session.add(user)

    db.session.commit()


excel_book = pd.ExcelFile("cleverdata_taxonomy_client.xlsm")
attributes_taxonomy = excel_book.parse(sheet_name='Attributes', header=2, index=False, usecols=[1, 2, 3, 4, 5])

dictionary_taxonomy = defaultdict(lambda: defaultdict())
for sheet in excel_book.sheet_names[7:]:
    data = excel_book.parse(sheet_name=sheet, index=False, header=2)
    for i, line in data.iterrows():
        if not (math.isnan(line.ID)):
            dictionary_taxonomy[sheet][int(line.ID)] = line.Description

if (len(User.query.all()) == 0):
    generate_data(100)
