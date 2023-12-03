import uuid
from datetime import datetime


class CompositorEntity:

    def __init__(self):
        self.id = uuid.uuid4()
        self.name = str(input("\nDigite o nome: "))
        self.birth_place = str(input("Digite o local de nascimento: "))

        birth = str(input("Digite a data de nascimento (ano-mes-dia): "))
        self.birthday = datetime.strptime(birth, "%Y-%m-%d")

        dead = str(input("Digite se o compositor ainda esta vivo (sim/nao): "))
        if dead.lower() == "sim":
            death = str(input("Digite a data de morte: "))
            self.death_date = datetime.strptime(death, "%Y-%m-%d")
        else:
            self.death_date = None
