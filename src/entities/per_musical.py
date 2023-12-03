import uuid
from datetime import datetime


class PerMusicalEntity:

    def __init__(self, id=None, descr=None, start_date=None, end_date=None):
        self.id = uuid.uuid4()
        self.descr = str(input("Digite a descricao: "))

        start = str(input("Digite a data de inicio (ano-mes-dia): "))
        self.start_date = datetime.strptime(start, "%Y-%m-%d")

        opt = str(input("O periodo musical ja acabou? (sim/nao): "))
        if opt.lower() == "sim":
            end = str(input("Digite a data do termino (ano-mes-dia): "))
            self.end_date = datetime.strptime(end, "%Y-%m-%d")
        else:
            self.end_date = None
