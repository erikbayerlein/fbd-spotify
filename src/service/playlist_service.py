from src.db.db import DataBaseService
from src.service.faixa_service import FaixaService
from src.entities.playlist import PlaylistEntity
from src.service.album_service import AlbumService


class PlaylistService:
    def __init__(self):
        pass

    def add_to_db(self):
        playlist = PlaylistEntity()
        sql_query = f"playlist (id_playlist, nome, data_criacao, tempo_total_exec) VALUES ('{playlist.id}', '{playlist.name}', '{playlist.creation_date}', '{playlist.execution_time}')"
        DataBaseService().insert(sql_query)

    def faixa_to_playlist(self):
        rows_playlist = PlaylistService().show_playlists()
        for row in rows_playlist:
            print(row)
        playlist_name = str(input("Identifique o nome da playlist que voce gostaria de adicionar uma faixa: "))
        playlist_id = PlaylistService().find_by_name(playlist_name)
        
        print("\n\n")

        rows_faixa = FaixaService().show_faixas()
        for row in rows_faixa:
            print(row)
        faixa_descr = str(input("Identifique a descricao da faixa: "))
        faixa_id = FaixaService().find_by_name(faixa_descr)

        sql_query_insert = f"faixa_playlist (id_faixa, id_playlist) VALUES ('{faixa_id}', '{playlist_id}')"
        DataBaseService().insert(sql_query_insert)

    def update(self, opt):
        print(f"------------- PLAYLISTS -------------")
        PlaylistService().show_playlists()

        if opt == 1:
            playlist_name = str(input("\nDigite o nome da playlist: "))
            playlist_id = PlaylistService().find_by_name(playlist_name)

            print("\n\n")
            print(f"------------- {playlist_name} -------------")
            self.show_faixas_in_playlist(playlist_id)

            print("\n")
            AlbumService().show_albums()
            album_descr = str(input("\nDigite o nome do album para visualizar as faixas: "))
            AlbumService().show_faixas_in_album(album_descr)

            faixa_descr = str(input("Digite a descricao da faixa para adicionar na playlist: "))
            faixa_id = FaixaService().find_by_descr(faixa_descr)

            sql_query = f"faixa_playlist (id_faixa, id_playlist) VALUES ('{faixa_id}', '{playlist_id}')"
            DataBaseService().insert(sql_query)
        else:
            playlist_name = str(input("\nDigite o nome da playlist: "))
            playlist_id = PlaylistService().find_by_name(playlist_name)

            print("\n\n\n")
            print(f"------------- {playlist_name} -------------")
            PlaylistService().show_faixas_in_playlist(playlist_id)

            faixa_descr = str(input("\nDigite a descricao da faixa: "))
            faixa_id = FaixaService().find_by_descr(faixa_descr)

            sql_query = f"faixa_playlist WHERE id_faixa = '{faixa_id}' AND id_playlist = '{playlist_id}'"
            DataBaseService().delete(sql_query)

    def show_playlists(self):
        sql_query = f"nome FROM playlist"
        rows = DataBaseService().search(sql_query)
        for row in rows:
            print(row[0])
    
    def find_by_name(self, name):
        sql_query = f"id_playlist FROM playlist WHERE nome = '{name}'"
        return DataBaseService().search(sql_query)[0][0]
    
    def show_faixas_in_playlist(self, playlist_id):
        sql_query = f"f.descricao FROM faixa f INNER JOIN faixa_playlist fpl ON f.id_faixa = fpl.id_faixa WHERE fpl.id_playlist = '{playlist_id}'"
        rows = DataBaseService().search(sql_query)
        for row in rows:
            print(row[0])