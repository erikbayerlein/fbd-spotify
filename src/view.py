import logging

from src.service.compositor_service import CompositorService
from src.service.playlist_service import PlaylistService
from src.service.per_musical_service import PerMusicalService
from src.service.album_service import AlbumService
from src.service.faixa_service import FaixaService
from src.service.gravadora_service import GravadoraService
from src.service.interprete_service import InterpreteService
from src.service.type_composition_service import TypeCompositionService


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def view():
    while True:
        print("\n\n\nEscolha a opcao que voce gostaria de visualizar: ")
        print("0 - Querys das questoes")
        print("1 - Playlist")
        print("2 - Albuns")
        print("3 - Compositores")
        print("4 - Gravadoras")
        print("5 - Periodos Musicais")
        print("6 - Interpretes")
        print("7 - Tipos de Composicao") 
        print("8 - Voltar")

        opt = int(input("\n"))

        match opt:
            case 0: view_quests()
            case 1: view_playlist()
            case 2: view_album()
            case 3: view_compositor()
            case 4: view_gravadoras()
            case 5: view_per_musical()
            case 6: view_interpretes()
            case 7: view_comp_types()
            case 8: return
            case _: logger.error("Opcao invalida. Tente novamente")

def view_playlist():
    PlaylistService().show_playlists()
    playlist_name = str(input("\nDigite o nome da playlist para visualizar suas faixas: "))
    playlist_id = PlaylistService().find_by_name(playlist_name)
    print(f"\n --------- {playlist_name} ---------")
    PlaylistService().show_faixas_in_playlist(playlist_id)

def view_compositor():
    CompositorService().show_compositors()

def view_per_musical():
    PerMusicalService().show_per_music()

def view_album():
    AlbumService().show_albums()
    album_descr = str(input("\nDigite a descricao do album para visualizar suas faixas: "))
    AlbumService().show_faixas_in_album(album_descr)

def view_faixas():
    FaixaService().show_faixas()

def view_gravadoras():
    GravadoraService().show_gravadoras()

def view_interpretes():
    InterpreteService().show_interpretes()

def view_comp_types():
    TypeCompositionService().show_type_compositions()

def view_quests():
    AlbumService().view_album_q1()
    GravadoraService().view_gravadora_q2()
    CompositorService().view_compositor_q3()
    PlaylistService().view_playlist_q4()
    return