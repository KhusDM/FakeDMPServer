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

from app import routes, models
