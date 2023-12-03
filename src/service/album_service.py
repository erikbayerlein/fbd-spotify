from src.db.db import DataBaseService

from src.entities.album import AlbumEntity
from src.entities.gravadora import GravadoraEntity
from src.entities.faixa import FaixaEntity

from src.service.gravadora_service import GravadoraService
from src.service.faixa_service import FaixaService


class AlbumService:
    def __init__(self):
        pass
    
    def add_to_bd(self, relational=False):
        db_service = DataBaseService()
        faixa_service = FaixaService()

        album = AlbumEntity()

        if relational:
            grav = GravadoraEntity()
            GravadoraService().add_to_db_relational(grav.id, grav.site, grav.name, grav.ender, grav.phones)            

            sql_query = f"album (id_album, id_grav, descricao, tipo_compra, preco, data_compra, data_gravacao, meio_fisico, tipo_grav_cd) VALUES ({album.id}, {grav.id}. {album.descr}, {album.purch_type}, {album.price}, {album.purch_date}, {album.record_date}, {album.enviroment}, {album.type_cd})"
            db_service.insert(sql_query)

        faixa_service.add_to_db(album.id, album.enviroment)
        
    def show_albums():
        sql_query = f"nome FROM album"
        return DataBaseService.search(sql_query)