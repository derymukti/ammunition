
from flask import Blueprint, request
from flask_pydantic import validate

from modules.example.dto import CreateRequestDTO
from modules.example.internal import Internal

from utils.http.validation import validation_response
example = Blueprint('example',__name__, url_prefix='/example')

@example.route('',methods=['POST'])
@validation_response
@validate()
def create_controller(body: CreateRequestDTO):
    return Internal().create(body)

@example.route('/<id>',methods=['PUT'])
@validation_response
@validate()
def update_controller(id: int, body: CreateRequestDTO):
    return Internal().update(id,body)

@example.route('/<id>',methods=['GET'])
@validation_response
@validate()
def detail_controller(id: int):
    return Internal().detail(id)

@example.route('',methods=['GET'])
def list_controller():
    return Internal().list_data()

@example.route('/<id>',methods=['DELETE'])
@validation_response
@validate()
def delete_controller(id: int):
    return Internal().delete(id)