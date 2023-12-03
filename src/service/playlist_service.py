from db.db import DataBaseService
from service.faixa_service import FaixaService
from entities.playlist import PlaylistEntity


class PlaylistService:
    def __init__(self):
        pass

    def add_to_db(self):
        playlist = PlaylistEntity()
        sql_query = f"playlist (id_playlist, nome, data_criacao, tempo_total_exec) VALUES ({playlist.id}, {playlist.name}, {playlist.creation_date}, {playlist.execution_time})"
        DataBaseService.insert(sql_query)

    def faixa_to_playlist(self):
        f_service = FaixaService()
        db_service = DataBaseService()
        pl_service = PlaylistService()

        rows_playlist = PlaylistService.show_playlists()
        for row in rows_playlist:
            print(row)
        playlist_name = str(input("Identifique o nome da playlist que voce gostaria de adicionar uma faixa: "))
        playlist_id = pl_service.find_by_name(playlist_name)
        
        print("\n\n")

        rows_faixa = f_service.show_faixas()
        for row in rows_faixa:
            print(row)
        faixa_descr = str(input("Identifique a descricao da faixa: "))
        faixa_id = f_service.find_by_name(faixa_descr)

        sql_query_insert = f"faixa_playlist (id_faixa, id_playlist) VALUES ({faixa_id}, {playlist_id})"
        db_service.insert(sql_query_insert)

    def update(self, opt):
        PlaylistService.show_playlists()

        if opt == 1:
            playlist_name = str(input("\nDigite o nome da playlist: "))
            playlist_id = PlaylistService.find_by_name(playlist_name)

            print("\n\n\n")
            print(f"------------- {playlist_name} -------------")
            PlaylistService.show_faixas_in_playlist(playlist_id)

            print("\n\n\n")
            print(f"------------- FAIXAS -------------")
            FaixaService.show_faixas()
            faixa_descr = str(input("\nDigite a descricao da faixa: "))
            faixa_id = FaixaService.find_by_descr(faixa_descr)

            sql_query = f"faixa_playlist (id_faixa, id_playlist) VALUES ({faixa_id}, {playlist_id})"
            DataBaseService.insert(sql_query)
        else:
            playlist_name = str(input("\nDigite o nome da playlist: "))
            playlist_id = PlaylistService.find_by_name(playlist_name)

            print("\n\n\n")
            print(f"------------- {playlist_name} -------------")
            PlaylistService.show_faixas_in_playlist(playlist_id)

            faixa_descr = str(input("\nDigite a descricao da faixa: "))
            faixa_id = FaixaService.find_by_descr(faixa_descr)

            sql_query = f"faixa_playlist WHERE id_faixa = {faixa_id} AND id_playlist = {playlist_id}"
            DataBaseService.delete(sql_query)

    def show_playlists(self):
        db_service = DataBaseService()
        sql_query = f"nome FROM playlist"
        rows = db_service.search(sql_query)
        for row in rows:
            print(row)
    
    def find_by_name(self, name):
        db_service = DataBaseService()
        sql_query = f"id_playlist FROM playlist WHERE nome = {name}"
        return db_service.search(sql_query)[0][0]
    
    def show_faixas_in_playlist(self, playlist_id):
        sql_query = f"f.descricao FROM faixa f INNER JOIN faixa_playlist fpl ON f.id_faixa = fpl.id_faixa WHERE fpl.id_playlist = {playlist_id}"
        rows = DataBaseService.search(sql_query)
        for row in rows:
            print(row)