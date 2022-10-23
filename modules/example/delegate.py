from modules.example.repository import detail, list_data, update,create
class Delegate:
    """This class is use by other module"""
    
    def create(self,data):
        return create(data.dict())
    def update(self,id,data):
        return update(id,data)
    def detail(self,id):
        return detail(id)
    def list_data(self,page: int,per_page: int):
        return list_data(page=page,per_page=per_page)