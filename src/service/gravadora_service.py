import time

from src.db.db import DataBaseService
from src.entities.gravadora import GravadoraEntity


class GravadoraService:
    def __init__(self):
        pass

    def add_to_db(self):
        grav_entity = GravadoraEntity()

        sql_query_grav = f"gravadora (id_grav, website, nome, ender) VALUES ('{grav_entity.id}', '{grav_entity.site}', '{grav_entity.name}', '{grav_entity.address}')"
        DataBaseService().insert(sql_query_grav)
        for phone in grav_entity.phone:
            sql_query_phones = f"telefone_gravadora (telefone, id_grav) VALUES ('{phone}', '{grav_entity.id}'))"
            DataBaseService().insert(sql_query_phones)

    def add_to_db_relational(self, id, site, name, ender, phones):
        sql_query_grav = f"gravadora (id_grav, website, nome, ender) VALUES ('{id}', '{site}', '{name}', '{ender}')"
        DataBaseService().insert(sql_query_grav)
        for phone in phones:
            sql_query_phones = f"telefone_gravadora (telefone, id_grav) VALUES ('{phone}', '{id}')"
            DataBaseService().insert(sql_query_phones)

    def show_gravadoras(self):
        sql_query = f"nome FROM gravadora"
        rows = DataBaseService().search(sql_query)
        print("\n --------- GRAVADORAS ---------")
        for row in rows:
            print(row[0])

    def find_by_name(self, name):
        sql_query = f"id_grav FROM gravadora WHERE nome = '{name}'"
        return DataBaseService().search(sql_query)[0][0]