import uuid

from db.db import DataBaseService


class CompositorService:
    def __init__(self):
        pass

    def new_compositor(self):
        self.uuid = uuid.uuid4()
        self.name = str(input("\nDigite o nome: "))
        self.birth_place = str(input("Digite o local de nascimento: "))
        self.birthday = date(input("Digite a data de nascimento: "))
        self.musical_period = str(input("Digite o periodo musical: "))
        #TODO - FUNCAO PARA IMPRIMIR O NOME DE TODOS OS PERIODOS MUSICAIS

        dead = str(input("Digite se o compositor ainda esta vivo (sim/nao): "))
        if dead.lower() == "sim":
            self.death_date = date(input("Digite a data de morte: "))
        else:
            self.death_date = None


    # TODO - FUNCAO DE BUSCA DE PERIODO MUSICAL POR NOME
    def add_to_bd(self):
        db_service = DataBaseService()
        sql_query_grav = f"compositor\
                    (id_compositor, id_periodo_musical,
                    nome, local_nasc,
                    data_nasc, data_morte)\
                    VALUES\
                    ({self.id}, {self.musical_period}, {self.name}, 
                    {self.birth_place}, {self.birthday}, {self.death_date})"
        db_service.insert(sql_query_grav)
