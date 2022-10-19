from modules.example.entity import Result,db

def create(data):
    result=Result(**data)
    db.session.add(result)
    db.session.commit()
    db.session.refresh(result)
    return result

def update(id,data):
    query = Result.query.filter_by(id=id).first()
    for var,value in vars(data).items():
        if value:
            setattr(query,var,value)

    db.session.add(query)
    db.session.commit()
    db.session.refresh(query)
    return query

def list_data(page,per_page):
    result=Result.query.paginate(page=page,per_page=per_page)
    return result