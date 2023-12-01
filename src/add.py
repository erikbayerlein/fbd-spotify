import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def add():
    print("\n\n\nEscolha a opcao que voce gostaria de adicionar:")
    print("\n1 - Faixa")
    print("2 - Playlist")
    print("3 - Adicionar Faixa em playlist")
    print("4 - Gravadora")
    print("5 - Voltar")

    a = int(input("\n"))

    match a:
        case 1: add()
        case 2: add()
        case 3: add()
        case 4: add()
        case 5: return
        case _: logger.error("Opcao invalida. Tente novamente")