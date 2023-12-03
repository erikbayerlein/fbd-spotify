from db.db import DataBaseService
from entities.interprete import InterpreteEntity

class InterpreteService:
    def __init__(self):
        pass

    def add_to_db(self):
        db_service = DataBaseService()
        interp = InterpreteEntity()
        sql_query = f"interprete (id_interprete, nome, tipo) VALUES ({interp.id}, {interp.name}, {interp.type})"
        db_service.insert(sql_query)
        return interp.id

    def show_interpretes():
        db_service = DataBaseService()
        sql_query = "nome FROM interprete"
        rows = db_service.search(sql_query)
        for row in rows:
            print(row)

    def find_by_name(self, name):
        db_service = DataBaseService()
        sql_query = f"id_interprete FROM interprete WHERE nome = {name}"
        return db_service.search(sql_query)[0][0]
