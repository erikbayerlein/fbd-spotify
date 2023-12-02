import uuid

from db.db import DataBaseService


class AlbumService:
    def __init__(self):
        pass

    def new_album(self):
        self.id = uuid.uuid4()
        self.name = str(input("\nDigite o nome: "))
        self.descrip = str(input("Digite a descricao: "))
        self.date_purchase = datetime(input("Digite o dia de compra: "))
        self.date_record = str(input("Digite o dia de gravacao: "))
        self.record = str(input("Digite o nome da Gravadora: "))
        self.purchase_type = str(input("Digite o tipo de compra: "))
        self.purchase_price = float(input("Digite o preco de compra: "))
        self.enviroment = str(input("Digite o meio fisico: "))
        if self.enviroment.lower() == "cd":
            self.type_cd = str(input("Digite o tipo de cd: "))
        else:
            self.type_cd = None

    # TODO - FUNCAO DE BUSCA DE GRAVADORA POR NOME
    def add_to_bd(self):
        db_service = DataBaseService()
        sql_query = f"album\
                    (id_album, id_grav, descricao, tipo_compra,\
                    preco, data_compra, data_gravacao,\
                    meio_fisico, tipo_grav_cd)\
                    VALUES\
                    ({self.id}, {self.record}. {self.descrip},
                    {self.purchase_type}, {self.purchase_price},
                    {self.date_purchase}, {self.date_record},
                    {self.enviroment}, {self.type_cd})"
        db_service.insert(sql_query)

