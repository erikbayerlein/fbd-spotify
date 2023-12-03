from src.entities.faixa import FaixaEntity

from src.db.db import DataBaseService
from src.service.compositor_service import CompositorService
from src.service.type_composition_service import TypeCompositionService
from src.service.interprete_service import InterpreteService


class FaixaService:
    def __init__(self):
        pass

    # TODO - CORRIGIR MEIO FISICO
    def add_to_db(self, id_album, album_enviroment):
        db_service = DataBaseService()

        num = int(input("Identifique quantas faixas o album possui: "))

        for i in range(0, num):
            opt_compositor = str(input(f"Voce gostaria de adicionar um novo compositor a faixa {num+1}? (sim/nao): ")).lower()
            if opt_compositor == "sim":
                opt_per_musical = str(input("Voce gostaria de adicionar um novo periodo musical ao compositor? (sim/nao): "))
                if opt_per_musical == "sim":
                    compositor_id = CompositorService().add_to_db(True)
                else:
                    compositor_id = CompositorService().add_to_db()
            else:
                CompositorService().show_compositors()
                comp_name = str(input("Identifique o nome do compositor: "))
                compositor_id = CompositorService().find_by_name(comp_name)

            opt_type_comp = str(input("Voce gostaria de adicionar um novo tipo de composicao? (sim/nao): ")).lower()
            if opt_type_comp == "sim":
                type_comp_id = TypeCompositionService().add_to_db()
            else:
                TypeCompositionService().show_type_compositions()
                type_comp_descr = str(input("Identifique a descricao do tipo de composicao: "))
                type_comp_id = TypeCompositionService().find_by_descr(type_comp_descr)

            opt_interpret = str(input("Voce gostaria de adicionar um novo interprete? (sim/nao): ")).lower()
            if opt_interpret == "sim":
                interprete_id = InterpreteService().add_to_db()
            else:
                InterpreteService().show_interpretes()
                interprete_name = str(input("Identifique o nome do interprete: "))
                interprete_id = InterpreteService().find_by_name(interprete_name)

            faixa = FaixaEntity(id_album, album_enviroment, i+1, type_comp_id)
            sql_query_faixa = f"faixa (id_faixa, id_album, id_tipo_comp, descricao, tempo_de_exec, pos_album, num_cd, num_vinil) VALUES ({faixa.id}, {faixa.id_album}, {faixa.id_composition}, {faixa.descr}, {faixa.exec_time}, {faixa.position_album}, {faixa.num_cd}, {faixa.num_vinil})"
            db_service.insert(sql_query_faixa)

            sql_query_faixa_compositor = f"faixa_compositor (id_faixa, id_compositor) VALUES ({faixa.id}, {compositor_id})"
            db_service.insert(sql_query_faixa_compositor)

            sql_query_faixa_interp = f"faixa_interprete (id_faixa, id_interprete) VALUES ({faixa.id}, {interprete_id})"
            db_service.insert(sql_query_faixa_interp)

    def find_by_descr(self, descr):
        db_service = DataBaseService()
        sql_query = f"id_faixa FROM faixa WHERE descricao = {descr}"
        return db_service.search(sql_query)[0][0]

    def show_faixas(self):
        db_service = DataBaseService()
        sql_query = f"descr FROM faixa"
        rows = db_service.search(sql_query)
        for row in rows:
            print(row)
