from db.db import DataBaseService
from entities.per_musical import PerMusicalEntity

class PerMusicalService:
    def __init__(self):
        pass

    def add_to_db(self):
        db_service = DataBaseService()
        per_musical = PerMusicalEntity()

        sql_query_per_music = f"periodo_musical (id_periodo_musical, \
                                descricao, data_inicio, data_fim) \
                                VALUES \
                                ({per_musical.id}, {per_musical.descr}, \
                                {per_musical.start_date}, {per_musical.end_date})"
        db_service.insert(sql_query_per_music)

    def add_to_db_relational(self, id, descr, begin_date, end_date):
        db_service = DataBaseService()
        sql_query = f"periodo_musical (id_periodo_musical, \
                    descricao, data_inicio, data_fim) \
                    VALUES \
                    ({id}, {descr}, {begin_date}, {end_date})"
        db_service.insert(sql_query)

    def show_per_music():
        db_service = DataBaseService()
        sql_query = f"descricao FROM periodo_musical"
        return db_service.search(sql_query) 