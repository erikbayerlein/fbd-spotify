from src.db.db import DataBaseService
from src.entities.type_composition import TypeCompositionEntity


class TypeCompositionService:
    def __init__(self):
        pass

    def add_to_db(self):
        type_comp = TypeCompositionEntity()
        sql_query = f"tipo_composicao (id_tipo_comp, descricao) VALUES ('{type_comp.id}', '{type_comp.descr}')"
        DataBaseService().insert(sql_query)
        return type_comp.id
    
    def show_type_compositions(self):
        sql_query = f"descricao FROM tipo_composicao"
        rows_type_comp = DataBaseService().search(sql_query)
        print("\n --------- TIPO DE COMPOSICOES ---------")
        for row in rows_type_comp:
            print(row[0])
    
    def find_by_descr(self, descr):
        sql_query = f"id_tipo_comp FROM tipo_composicao WHERE descricao = '{descr}'"
        return DataBaseService().search(sql_query)[0][0]