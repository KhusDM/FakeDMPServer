import pandas as pd
from collections import defaultdict
from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# db = [{"id": "dmitry.khusnetdinov@sas.com",
#        "attrs": [{"primary": 10055, "secondary": 10177}, {"primary": 10052, "secondary": 10004},
#                  {"primary": 10057, "secondary": 10001}, {"primary": 10169, "secondary": 10003}]},
#       {"id": "cidemo.cis@gmail.com",
#        "attrs": [{"primary": 10055, "secondary": 10177}, {"primary": 10052, "secondary": 10007},
#                  {"primary": 10057, "secondary": 10002}, {"primary": 10169, "secondary": 10001}]}
#       ]

# users = source[source["id"] == "Dmitry.Khusnedinov@sas.com"].to_dict(orient="records")
# print()


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

excel_book = pd.ExcelFile("cleverdata_taxonomy_client.xlsm")
attributes_taxonomy = excel_book.parse(sheet_name='Attributes', header=2, index=False, usecols=[1, 2, 3, 4, 5])
dictionary_taxonomy = defaultdict(lambda: defaultdict())
for sheet in excel_book.sheet_names[7:]:
    data = excel_book.parse(sheet_name=sheet, index=False, header=2)
    for i, line in data.iterrows():
        dictionary_taxonomy[sheet][line.ID] = line.Description


# source = pd.read_excel("source2.xlsx")
# source["id"] = source["id"].str.lower()

from app import routes, models