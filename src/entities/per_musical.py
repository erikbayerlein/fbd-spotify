import uuid
from datetime import datetime


class PerMusicalEntity:

    def __init__(self):
        self.id = uuid.uuid4()
        self.descr = str(input("Digite a descricao do periodo musical: "))

        start = str(input("Digite a data de inicio (ano-mes-dia) do periodo musical: "))
        self.start_date = datetime.strptime(start, "%Y-%m-%d")

        end = str(input("Digite a data do termino (ano-mes-dia): "))
        self.end_date = datetime.strptime(end, "%Y-%m-%d")
