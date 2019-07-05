import pandas as pd
from collections import defaultdict
from flask import Flask, jsonify, abort, make_response, request

excel_book = pd.ExcelFile("cleverdata_taxonomy_client.xlsm")
attributes_taxonomy = excel_book.parse(sheet_name='Attributes', header=2, index=False, usecols=[1, 2, 3, 4, 5])
# attribute_type = attributes_taxonomy[attributes_taxonomy["Short Name"] == "id"]["Type"].tolist()[0]
dictionary_taxonomy = defaultdict(lambda: defaultdict())
for sheet in excel_book.sheet_names[7:]:
    data = excel_book.parse(sheet_name=sheet, index=False, header=2)
    for i, line in data.iterrows():
        dictionary_taxonomy[sheet][line.ID] = line.Description

source = pd.read_excel("source2.xlsx")
source["id"] = source["id"].str.lower()

# db = [{"id": "dmitry.khusnetdinov@sas.com",
#        "attrs": [{"primary": 10055, "secondary": 10177}, {"primary": 10052, "secondary": 10004},
#                  {"primary": 10057, "secondary": 10001}, {"primary": 10169, "secondary": 10003}]},
#       {"id": "cidemo.cis@gmail.com",
#        "attrs": [{"primary": 10055, "secondary": 10177}, {"primary": 10052, "secondary": 10007},
#                  {"primary": 10057, "secondary": 10002}, {"primary": 10169, "secondary": 10001}]}
#       ]

# users = source[source["id"] == "Dmitry.Khusnedinov@sas.com"].to_dict(orient="records")
# print()

values_type = ["Boolean", "Character", "Byte", "Integer",
               "Long", "Double", "String", "Enum", "ABoolean",
               "ACharacter", "AByte", "AInteger", "ALong", "ADouble",
               "AString", "AEnum", "AAByte"]


def encode_data(user):
    coded_data = dict()
    for key, value in user.items():
        if (key == "id"):
            coded_data["id"] = value
        else:
            if not ("attrs" in coded_data.keys()):
                coded_data["attrs"] = list()

            attribute = attributes_taxonomy[attributes_taxonomy["Name"] == key].to_dict(orient="records")[0]
            coded_attribute = {"primary": int(attribute["ID"]), "secondary": None}
            if not (attribute["Type"] in values_type) and (attribute["Type"] != "D-Currency"):
                for key2, value2 in dictionary_taxonomy[attribute["Type"]].items():
                    if (value == value2):
                        coded_attribute["secondary"] = key2
                        break
            else:
                coded_attribute["secondary"] = value

            coded_data["attrs"].append(coded_attribute)

    return coded_data


# users = source[source["id"] == "Dmitry.Khusnetdinov@sas.com"].to_dict(orient='records')
# if (len(users) != 0):
#     coded_data = encode_data(users[0])

app = Flask(__name__)


# @app.route('/fakeDMP/api/v1.0/users', methods=['GET'])
# def get_user_info():
#     users = list(filter(lambda u: u['id'] == request.args.get("id"), source["id"]))
#     if (len(users) == 0):
#         abort(404)
#
#     return jsonify(users[0])

@app.route('/fakeDMP/api/v1.0/users', methods=['GET'])
def get_user_info():
    users = source[source["id"] == request.args.get("id")].to_dict(orient='records')
    if (len(users) == 0):
        abort(404)

    coded_data = encode_data(users[0])
    return jsonify(coded_data)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'not found'}), 404)


if (__name__ == '__main__'):
    app.run(debug=True)
