import logging

from src.add import add
from db.db import DataBaseService


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def menu():
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
        print("4 - Excluir")
        print("5 - ...")
        print("6 - Sair")

        a = int(input("\n"))

        match a:
            case 1: add()
            case 2: add()
            case 3: add()
            case 4: add()
            case 5: add()
            case 6: 
                DataBaseService.close_connection()
                exit()
            case _: logger.error("Opcao invalida. Tente novamente")

DataBaseService.connect()
menu()