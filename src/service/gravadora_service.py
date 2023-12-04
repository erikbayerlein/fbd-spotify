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
    
    def view_gravadora_q2(self):
        sql_query = f"grav.id_grav, grav.nome, COUNT(DISTINCT pl.id_playlist) AS countPlaylist FROM gravadora grav JOIN album ab ON ab.id_grav = grav.id_grav JOIN faixa f ON f.id_album = ab.id_album JOIN faixa_compositor fc ON fc.id_faixa = f.id_faixa JOIN compositor comp ON comp.id_compositor = fc.id_compositor JOIN faixa_playlist fp ON fp.id_faixa = f.id_faixa JOIN playlist pl ON pl.id_playlist = fp.id_playlist JOIN (SELECT pl.id_playlist from album ab JOIN faixa f ON f.id_album = ab.id_album JOIN faixa_compositor fc ON fc.id_faixa = f.id_faixa JOIN compositor comp ON comp.id_compositor = fc.id_compositor JOIN faixa_playlist fp ON fp.id_faixa = f.id_faixa JOIN playlist pl ON pl.id_playlist = fp.id_playlist WHERE comp.nome LIKE 'Dvorack' GROUP BY pl.id_playlist) AS d ON d.id_playlist = pl.id_playlist GROUP BY grav.id_grav, grav.nome ORDER BY countPlaylist DESC LIMIT 1"
        rows = DataBaseService().search(sql_query)
        print("\n------------- Questao 2 -------------")
        for row in rows:
            print("NOME | CONTAGEM")
            print(f"{row[1]} - {row[2]}")