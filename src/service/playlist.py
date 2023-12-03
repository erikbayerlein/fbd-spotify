import uuid
from datetime import datetime

from db.db import DataBaseService
from service.faixa import FaixaService


class PlaylistService:
    def __init__(self):
        pass

    def new_playlist(self):
        self.id = uuid.uuid4()
        self.name = str(input("\nDigite o nome: "))
        self.creation_date = datetime.now()
        self.execution_time = 0

    def add_to_bd(self):
        db_service = DataBaseService()
        sql_query = f"playlist \
                    (id_playlist, nome, data_criacao, tempo_total_exec) \
                    VALUES \
                    ({self.id}, {self.name}. {self.creation_date}, {self.execution_time})"
        db_service.insert(sql_query)

    def faixa_to_playlist():
        f_service = FaixaService()
        db_service = DataBaseService()

        rows_playlist = PlaylistService.show_playlists()
        for row in rows_playlist:
            print(row)
        playlist_name = str(input("Identifique o nome da playlist que voce gostaria de adicionar uma faixa: "))

        sql_query_get_playlist = f"* FROM playlist WHERE nome = {playlist_name}"
        playlist = db_service.search(sql_query_get_playlist)
        
        print("\n\n")

        rows_faixa = f_service.show_faixas()
        for row in rows_faixa:
            print(row)
        faixa_name = str(input("Identifique o nome da faixa: "))

        sql_query_get_faixa = f"* FROM faixa WHERE nome = {faixa_name}"
        faixa = db_service.search(sql_query_get_faixa)

        sql_query_insert = f"faixa_playlist (id_faixa, id_playlist) VALUES ({faixa[0]}, {playlist[0]})"
        db_service.insert(sql_query_insert)

    def show_playlists():
        db_service = DataBaseService()
        sql_query = f"nome FROM playlist"
        return db_service.search(sql_query)