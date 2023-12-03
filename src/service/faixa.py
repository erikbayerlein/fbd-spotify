import uuid
from datetime import datetime

from db.db import DataBaseService
from service.album_service import AlbumService


class FaixaService:
    def __init__(self):
        pass

    def new_faixa(self):
        ab_service = AlbumService()
        db_service = DataBaseService()

        self.id = uuid.uuid4()
        self.name = str(input("\nDigite o nome: "))
        self.descr = str(input("Digite a descricao: "))

        exec_time = str(input("Digite o tempo de execucao em minutos e segundos: "))
        self.exec_time = datetime.strptime(exec_time, "%M:%S").time()

        self.position_album = int(input("Digite a posicao no album: "))

        print("\n")

        album_rows = ab_service.show_albums()
        for row in album_rows:
            print(row)
        answr = str(input("\nDesejaria criar um novo album para a faixa? (sim/nao): ")).lower()
        if answr == "sim":
            ab_service.new_album(True)
            if ab_service.enviroment == "cd":
                num_physical_env = int(input(f"Identifique o numero do cd que esta a faixa: "))
                self.num_cd = num_physical_env
                self.num_vinil = None
            elif ab_service.enviroment == "vinil":
                num_physical_env = int(input(f"Identifique o numero do vinil que esta a faixa: "))
                self.num_vinil = num_physical_env
                self.num_cd = None
            else:
                self.num_vinil = None
                self.num_cd = None
                
        else:
            album_name = str(input("Identifique o nome do album a qual a faixa pertence: "))
            sql_get_album = f"id_album, meio_fisico FROM album WHERE nome = {album_name}"
            album = db_service.search(sql_get_album)
            id_album = album[0]
            enviroment = album[1]
            self.id_album = id_album
            if enviroment == "cd":
                num_physical_env = int(input(f"Identifique o numero do cd que esta a faixa: "))
                self.num_cd = num_physical_env
                self.num_vinil = None
            elif enviroment == "vinil":
                num_physical_env = int(input(f"Identifique o numero do cd que esta a faixa: "))
                self.num_cd = num_physical_env
                self.num_vinil = None
            else:
                self.num_vinil = None
                self.num_cd = None 



    # TODO - FUNCAO DE BUSCA DE GRAVADORA POR NOME
    def add_to_bd(self):
        db_service = DataBaseService()
        sql_query_grav = f"gravadora \
                    (id_grav, site, nome, ender) \
                    VALUES \
                    ({self.name}, {self.site}. {self.name}, {self.ender})"
        db_service.insert(sql_query_grav)

    def show_faixas():
        db_service = DataBaseService()
        sql_query = f"nome FROM faixa"
        return db_service.search(sql_query)
