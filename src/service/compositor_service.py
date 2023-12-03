from db.db import DataBaseService
from entities.compositor import CompositorEntity
from service.per_musical_service import PerMusicalService
from entities.per_musical import PerMusicalEntity


class CompositorService:
    def __init__(self):
        pass

    # relational = true: estamos criando um periodo musical em conjunto
    # relational = false: o periodo musical do compositor ja existe
    def add_to_db(self, relational=False):
        db_service = DataBaseService()
        per_music_service = PerMusicalService()

        compositor = CompositorEntity()

        if relational:
            per_music = PerMusicalEntity()
            per_music_service.add_to_db_relational(per_music.id, per_music.descr, per_music.start_date, per_music.end_date)
            
            sql_query_compositor = f"compositor (id_compositor, id_periodo_musical, \
                                    nome, local_nasc, data_nasc, data_morte) \
                                    VALUES \
                                    ({compositor.id}, {per_music.id}, {compositor.name}, {compositor.birth_place}, \
                                    {compositor.birthday}, {compositor.death_date}))"
            db_service.insert(sql_query_compositor)

        else:
            print("\n")
            per_music_rows = per_music_service.show_per_music()
            for row in per_music_rows:
                print(row)

            per_music_name = str(input("Digite o nome do periodo musical do compositor: "))
            sql_query_get_per_music = f"* FROM periodo_musical WHERE nome = {per_music_name}"
            per_music = db_service.search(sql_query_get_per_music)
            id_per_music = per_music[0]

            sql_query_grav = f"compositor \
                            (id_compositor, id_periodo_musical, \
                            nome, local_nasc, \
                            data_nasc, data_morte) \
                            VALUES \
                            ({compositor.id}, {id_per_music}, {compositor.name}, \
                            {compositor.birth_place}, {compositor.birthday}, {compositor.death_date})"
            db_service.insert(sql_query_grav)

    def add_to_db_relational(self, per_musical_id):
        return

    def show_compositors():
        db_service = DataBaseService()
        sql_query = f"nome FROM compositors"
        return db_service.search(sql_query)