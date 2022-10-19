from typing import Optional
from flask import Response
from pydantic import BaseModel, validator
from utils.constants import HTTP_RESPONSE
import json
class Pagination(BaseModel):
    page: Optional[int] = 0
    next_num: Optional[int] = 0
    prev_num: Optional[int] = 0
    pages: Optional[int] = 0
    total: Optional[int] = 0
    per_page: Optional[int] = 0
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        validate_assignment = True

def return_response(data=None,http_status=HTTP_RESPONSE.SUCCESS):
    meta = {
        "status":http_status['STATUS'],
        "code":http_status['CODE']
    }
    response_data = json.dumps({
        "meta":meta,
        "data":data
    })
    return Response(response=response_data,status=http_status['HTTP_CODE'],mimetype='application/json')

def detail_response(data=None,http_status=HTTP_RESPONSE.SUCCESS):
    data = {
        "detail":data
    }
    return return_response(data,http_status)

def list_response(list=None,pagination=None,http_status=HTTP_RESPONSE.SUCCESS):
    data = {
            "list":list,
            "pagination":pagination,
    }
    return return_response(data,http_status)

def error_response(data=None,http_status=HTTP_RESPONSE.ERROR):
    data = {
        "errors":data   
    }
    return return_response(data,http_status)