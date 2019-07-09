from app import app
from api import attributes_taxonomy, dictionary_taxonomy
from flask import jsonify, abort, make_response, send_file, request
from app.models import User

values_type = ["Boolean", "Character", "Byte", "Integer",
               "Long", "Double", "String", "Enum", "ABoolean",
               "ACharacter", "AByte", "AInteger", "ALong", "ADouble",
               "AString", "AEnum", "AAByte"]


def encode_data(user):
    coded_data = dict()
    for key, value in user.items():
        if (key == "_sa_instance_state"):
            continue
        elif (key == "id"):
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


# @app.route('/fakeDMP/api/v1.0/users', methods=['GET'])
# def get_user_info():
#     users = source[source["id"] == request.args.get("id")].to_dict(orient='records')
#     if (len(users) == 0):
#         abort(404)
#
#     coded_data = encode_data(users[0])
#     return jsonify(coded_data)

@app.route('/fakeDMP/api/v1.0/users', methods=['GET'])
def get_user_info():
    # user = User.query.get(request.args.get("id"))
    user = User.query.get("efb0112f-9cc1-4c58-9bb2-30b96f1abd37")
    if (user == None):
        abort(404)

    coded_data = encode_data(vars(user))
    return jsonify(coded_data)


@app.route('/fakeDMP/api/v1.0/pixel.gif', methods=['GET'])
def get_pixel():
    return send_file("images/pixel.gif", mimetype="image/gif")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'not found'}), 404)
