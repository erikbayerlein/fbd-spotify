import uuid


class GravadoraEntity:

    def __init__(self):
        self.id = uuid.uuid4()
        self.name = str(input("\nDigite o nome da gravadora: "))
        self.site = str(input("Digite o site da gravadora: "))
        self.address = str(input("Digite o endereco gravadora: "))
        num = int(input("Digite quantos numeros a gravadora possui: "))
        self.phone = []
        for i in range(0, num):
            phone_num = int(input(f"Digite o telefone {i+1} da gravadora: "))
            self.phone.append(phone_num)
