import uuid

from db.db import DataBaseService


class InterpreteService:
    def __init__(self):
        pass

    def new_interprete(self):
        self.uuid = uuid.uuid4()
        self.name = str(input("\nDigite o nome: "))
        self.type = str(input("Digite o tipo de interpretacao: "))


    def add_to_bd(self):
        db_service = DataBaseService()
        sql_query = f"interprete\
                    (id_interprete, nome, tipo)\
                    VALUES\
                    ({self.id}, {self.name}, {self.type})"
        db_service.insert(sql_query)
