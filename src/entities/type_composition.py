import uuid


class TypeComposition:
    def __init__(self):
        self.id = uuid.uuid4()
        self.descr = str(input("Digite a descricao do tipo de composicao: "))