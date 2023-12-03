import uuid

from db.db import DataBaseService
from entities.gravadora import GravadoraEntity


class GravadoraService:
    def __init__(self):
        pass

    def add_to_db(self):
        db_service = DataBaseService()
        grav_entity = GravadoraEntity()

        sql_query_grav = f"gravadora (id_grav, site, nome, ender) VALUES ({grav_entity.id}, {grav_entity.site}, {grav_entity.name}, {grav_entity.ender}"
        db_service.insert(sql_query_grav)
        for phone in grav_entity.phone:
            sql_query_phones = f"telefone_gravadora (telefone, id_grav) VALUES ({phone}, {grav_entity.id})"
            db_service.insert(sql_query_phones)

    def add_to_db_relational(self, id, site, name, ender, phones):
        db_service = DataBaseService()
        sql_query_grav = f"gravadora \
                        (id_grav, site, nome, ender) \
                        VALUES \
                        ({id}, {site}. {name}, {ender}"
        db_service.insert(sql_query_grav)
        for phone in phones:
            sql_query_phones = f"telefone_gravadora
                                (telefone, id_grav)
                                VALUES
                                ({phone}, {id})"
            db_service.insert(sql_query_phones)
