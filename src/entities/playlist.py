import uuid
from datetime import datetime


class PlaylistEntity:
    def __init__(self):
        self.id = uuid.uuid4()
        self.name = str(input("\nDigite o nome da playlist: "))
        self.creation_date = datetime.now()
        self.execution_time = datetime.strptime("00:00", '%M:%S')
