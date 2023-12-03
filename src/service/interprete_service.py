from src.db.db import DataBaseService
from src.entities.interprete import InterpreteEntity

class InterpreteService:
    def __init__(self):
        pass

    def add_to_db(self):
        interp = InterpreteEntity()
        sql_query = f"interprete (id_interprete, nome, tipo) VALUES ('{interp.id}', '{interp.name}', '{interp.type}')"
        DataBaseService().insert(sql_query)
        return interp.id

    def show_interpretes(self):
        sql_query = "nome FROM interprete"
        rows = DataBaseService().search(sql_query)
        for row in rows:
            print(row)

    def find_by_name(self, name):
        sql_query = f"id_interprete FROM interprete WHERE nome = {name}"
        return DataBaseService().search(sql_query)[0][0]
