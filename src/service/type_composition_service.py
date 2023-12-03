from db.db import DataBaseService
from entities.type_composition import TypeComposition


class TypeCompositionService:
    def __init__(self):
        pass

    def add_to_db(self):
        db_service = DataBaseService()
        type_comp = TypeComposition()
        sql_query = f"tipo_composicao (id_tipo_comp, descricao) VALUES ({type_comp.id}, {type_comp.descr})"
        db_service.insert(sql_query)
        return type_comp.id
    
    def show_type_compositions(self):
        db_service = DataBaseService()
        sql_query = f"descr FROM tipo_composicao"
        rows_type_comp = db_service.search(sql_query)
        for row in rows_type_comp:
            print(row)
    
    def find_by_descr(self, descr):
        db_service = DataBaseService()
        sql_query = f"id_tipo_comp FROM tipo_composicao WHERE descricao = {descr}"
        return db_service.search(sql_query)[0][0]