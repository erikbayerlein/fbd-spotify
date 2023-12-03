import uuid


class InterpreteEntity:
    def __init__(self):
        self.id = uuid.uuid4()
        self.name = str(input("\nDigite o nome: "))
        self.type = str(input("Digite o tipo de interpretacao: "))
