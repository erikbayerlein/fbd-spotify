import uuid
from datetime import datetime


class CompositorEntity:

    def __init__(self):
        self.id = uuid.uuid4()
        self.name = str(input("\nDigite o nome do compositor: "))
        self.birth_place = str(input("Digite o local de nascimento do compositor: "))

        birth = str(input("Digite a data de nascimento do compositor (ano-mes-dia): "))
        self.birthday = datetime.strptime(birth, "%Y-%m-%d")

        dead = str(input("Digite se o compositor ainda esta vivo (sim/nao): "))
        if dead.lower() == "nao":
            death = str(input("Digite a data de morte: "))
            self.death_date = datetime.strptime(death, "%Y-%m-%d")
        else:
            self.death_date = None
