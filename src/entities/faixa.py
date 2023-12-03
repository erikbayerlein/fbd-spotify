import uuid
from datetime import datetime

from db.db import DataBaseService
from service.album_service import AlbumService


class FaixaEntity:
    def __init__(self, id_album, enviroment, num, composition_id):
        self.id = uuid.uuid4()
        print(f"\n------------- Faixa {num} -------------")
        self.descr = str(input("Digite a descricao: "))

        exec_time = str(input("Digite o tempo de execucao em minutos e segundos: "))
        self.exec_time = datetime.strptime(exec_time, "%M:%S").time()

        self.position_album = num
        self.id_album = id_album
        self.id_composition = composition_id

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
