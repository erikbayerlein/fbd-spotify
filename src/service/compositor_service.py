from datetime import datetime

from src.db.db import DataBaseService
from src.entities.compositor import CompositorEntity
from src.service.per_musical_service import PerMusicalService
from src.entities.per_musical import PerMusicalEntity


class CompositorService:
    def __init__(self):
        pass

    # relational = true: estamos criando um periodo musical em conjunto
    # relational = false: o periodo musical do compositor ja existe
    def add_to_db(self, relational=False):
        compositor = CompositorEntity()

        if relational:
            per_music = PerMusicalEntity()
            PerMusicalService().add_to_db_relational(per_music.id, per_music.descr, per_music.start_date, per_music.end_date)
            if compositor.death_date != None:
                sql_query_compositor = f"compositor (id_compositor, id_periodo_musical, nome, local_nasc, data_nasc, data_morte) VALUES ('{compositor.id}', '{per_music.id}', '{compositor.name}', '{compositor.birth_place}', '{compositor.birthday}', '{compositor.death_date}')"
            else:
                sql_query_compositor = f"compositor (id_compositor, id_periodo_musical, nome, local_nasc, data_nasc) VALUES ('{compositor.id}', '{per_music.id}', '{compositor.name}', '{compositor.birth_place}', '{compositor.birthday}')" 
            DataBaseService().insert(sql_query_compositor)
        else:
            print("\n")
            PerMusicalService().show_per_music()

            per_music_name = str(input("Digite o nome do periodo musical do compositor: "))
            id_per_music = PerMusicalService().find_by_name(per_music_name)

            if compositor.death_date != None:
                sql_query_compositor = f"compositor (id_compositor, id_periodo_musical, nome, local_nasc, data_nasc, data_morte) VALUES ('{compositor.id}', '{id_per_music}', '{compositor.name}', '{compositor.birth_place}', '{compositor.birthday}', '{compositor.death_date}')"
            else:
                sql_query_compositor = f"compositor (id_compositor, id_periodo_musical, nome, local_nasc, data_nasc) VALUES ('{compositor.id}', '{id_per_music}', '{compositor.name}', '{compositor.birth_place}', '{compositor.birthday}')"
            DataBaseService().insert(sql_query_compositor)
        return compositor.id

    def show_compositors(self):
        sql_query = f"nome FROM compositor"
        rows = DataBaseService().search(sql_query)
        print("\n--------- COMPOSITORES ---------")
        for row in rows:
            print(row[0])
    
    def find_by_name(self, name):
        db_service = DataBaseService()
        sql_query = f"id_compositor FROM compositor WHERE nome = '{name}'"
        return db_service.search(sql_query)[0][0]

    def update(self):
        CompositorService().show_compositors()
        comp_name = str(input("\n\nIdentifique o nome do compositor: "))

        new_death_date = str(input("\nDigite a nova data de morte: "))
        death_date = datetime.strptime(new_death_date, "%Y-%m-%d")

        sql_query = f"compositor SET data_morte = '{death_date}' WHERE nome = '{comp_name}'"
        DataBaseService().update(sql_query)

    def view_compositor_q3(self):
        sql_query = f"TOP 1 comp.nome, COUNT(fp.id_faixa) AS Contagem FROM compositor comp INNER JOIN faixa_compositor fc ON comp.id_compositor = fc.id_compositor INNER JOIN faixa f ON fc.id_faixa = f.id_faixa INNER JOIN faixa_playlist fp ON f.id_faixa = fp.id_faixa GROUP BY comp.nome ORDER BY Contagem DESC"
        rows = DataBaseService().search(sql_query)
        print("\n------------- Questao 3 -------------")
        for row in rows:
            print("NOME | CONTAGEM")
            print(f"{row[0]} - {row[1]}")
