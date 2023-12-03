import logging

from src.add import add
from src.update import update
from src.view import view

from src.db.db import DataBaseService


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def menu():
    db_service = DataBaseService()
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("""
        __             _     ___          
        / _\_ __   ___ | |_  / _ \___ _ __ 
        \ \| '_ \ / _ \| __|/ /_)/ _ \ '__|
        _\ \ |_) | (_) | |_/ ___/  __/ |   
        \__/ .__/ \___/ \__\/    \___|_|   
        |_|                             
        """)
        print("\nEscolha uma das opcoes abaixo:")
        print("\n1 - Visualizar")
        print("2 - Adicionar")
        print("3 - Atualizar")
        print("4 - Sair")

        a = int(input("\n"))

        match a:
            case 1: view()
            case 2: add()
            case 3: update()
            case 4: 
                db_service.close_connection()
                exit()
            case _: logger.error("Opcao invalida. Tente novamente")

menu()