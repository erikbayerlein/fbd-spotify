from datetime import datetime

from src.db.db import DataBaseService
from src.entities.per_musical import PerMusicalEntity

class PerMusicalService:
    def __init__(self):
        pass

    def add_to_db(self):
        per_musical = PerMusicalEntity()

        sql_query_per_music = f"periodo_musical (id_periodo_musical, descricao, data_inicio, data_fim) VALUES ({per_musical.id}, {per_musical.descr}, {per_musical.start_date}, {per_musical.end_date})"
        DataBaseService().insert(sql_query_per_music)

    def add_to_db_relational(self, id, descr, begin_date, end_date):
        db_service = DataBaseService()
        sql_query = f"periodo_musical (id_periodo_musical, descricao, data_inicio, data_fim) VALUES ({id}, {descr}, {begin_date}, {end_date})"
        db_service.insert(sql_query)

    def show_per_music(self):
        sql_query = f"descricao FROM periodo_musical"
        rows = DataBaseService().search(sql_query)
        for row in rows:
            print(row)

    def find_by_name(self, name):
        sql_query = f"id_periodo_musical FROM periodo_musical WHERE nome = {name}"
        return DataBaseService().search(sql_query)[0][0]
    
    def update(self):
        PerMusicalService().show_per_music()
        per_music_descr = str(input("\n\nIdentifique a descricao do periodo musical: "))

        new_end_date = str(input("\nDigite a nova data de termino: "))
        end_date = datetime.strptime(new_end_date, "%Y-%m-%d")

        sql_query = f"periodo_musical SET data_fim = {end_date} WHERE descricao = {per_music_descr}"
        DataBaseService().update(sql_query)