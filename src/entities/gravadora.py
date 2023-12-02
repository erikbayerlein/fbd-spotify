import uuid

from db.db import DataBaseService


class GravadoraService:
    def __init__(self):
        pass

    def new_gravadora(self):
        self.uuid = uuid.uuid4()
        self.name = str(input("\nDigite o nome: "))
        self.site = str(input("Digite o site: "))
        self.address = str(input("Digite o endereco: "))
        num = int(input("Digite quantos numeros a gravadora possui: "))
        self.phone = []
        for i in range(0, num):
            phone_num = int(input(f"Digite o telefone {i+1} da gravadora: "))
            self.phone.append(phone_num)

    def add_to_bd(self):
        db_service = DataBaseService()
        sql_query_grav = f"gravadora\
                    (id_grav, site, nome, ender)\
                    VALUES\
                    ({self.id}, {self.site}. {self.name}, {self.ender}"
        db_service.insert(sql_query_grav)
        
        for phone in self.phone:
            sql_query_phones = f"telefone_gravadora
                        (telefone, id_grav)
                        VALUES
                        ({phone}, {self.id})"
            db_service.insert(sql_query_phones)

