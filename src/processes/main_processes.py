from managers import GenericManager


class MainProcess:
    
    def __init__(self, id: str, *args, **kwargs):
        self.id = id
        self.objects = GenericManager()

