from flask import Flask
from utils.http import response
from utils.constants import HTTP_RESPONSE
from modules.example.controller import example
import os
from db import db
app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL","postgresql:///mydb")
db.init_app(app)

"""Register Modules"""
app.register_blueprint(example)

@app.errorhandler(404)
def r404(e):
	return response.error_response(data=str(e),http_status=HTTP_RESPONSE.NOT_FOUND)

@app.errorhandler(500)
def r500(e):
	return response.error_response(data=str(e),http_status=HTTP_RESPONSE.ERROR)

@app.errorhandler(400)
def r400(e):
	return response.error_response(data=str(e),http_status=HTTP_RESPONSE.FAILED)
