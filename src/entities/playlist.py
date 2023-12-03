import uuid
from datetime import datetime


class PlaylistEntity:
    def __init__(self):
        self.id = uuid.uuid4()
        self.name = str(input("\nDigite o nome: "))
        self.creation_date = datetime.now()
        self.execution_time = 0
