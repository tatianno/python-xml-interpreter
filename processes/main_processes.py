from elements import StartEvent
from managers import TaskManager


class MainProcess:
    
    def __init__(self, id: str, *args, **kwargs):
        self.id = id
        self.tasks = TaskManager()
        self.start_event: StartEvent = None
    
    def set_start_event(self, start_event: StartEvent):

        if type(start_event) != StartEvent:
            raise TypeError('Only start event objects are supported!')
        
        self.start_event = start_event

