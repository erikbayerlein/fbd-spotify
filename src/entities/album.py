import uuid
from datetime import datetime


class AlbumEntity:
    def __init__(self):
        self.id = uuid.uuid4()
        self.name = str(input("\nDigite o nome: "))
        self.descr = str(input("Digite a descricao: "))

        purchase_date = str(input("Digite a data de compra (ano-mes-dia): "))
        self.purch_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        
        rec_date = str(input("Digite a data de gravacao (ano-mes-dia): "))
        self.record_date = datetime.strptime(rec_date, "%Y-%m-%d")

        self.purch_type = str(input("Digite o tipo de compra: "))
        self.price = float(input("Digite o preco de compra: "))
        self.enviroment = str(input("Digite o meio fisico: ")).lower()
        if self.enviroment == "cd":
            self.type_cd = str(input("Digite o tipo de gravacao do cd: "))
        else:
            self.type_cd = None