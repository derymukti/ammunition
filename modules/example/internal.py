from modules.example.delegate import Delegate
from modules.example.dto import CreateRequestDTO, ListDTO
from utils.http import response
from flask import request,abort

class Internal:
    """This class is only use by internal module"""
    
    def create(self,data):
        result = Delegate().create(data)
        return CreateRequestDTO.from_orm(result)

    def update(self,id,data):
        result = Delegate().update(id,data)
        return response.detail_response(data=CreateRequestDTO.from_orm(result).dict())

    def list_data(self):
        try:
            try:
                page = int(request.args.get('page',default=1))
                per_page = int(request.args.get('per_page',default=10))
            except Exception:
                page = 1
                per_page = 10
            result = Delegate().list_data(page=page,per_page=per_page)
            pagination = response.Pagination.from_orm(result)
            return response.list_response(ListDTO(list=result.items).dict()['list'],pagination=pagination.dict())
        except Exception:
            abort(400)
        