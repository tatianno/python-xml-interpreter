from elements import Task
from managers.generic_manager import GenericManager


class TaskManager(GenericManager):

    def set(self, task: Task) -> None:

        if type(task) != Task:
            raise TypeError('Only Tasks objects are supported!')
        
        super().set(task)
    
    def get(self, id: str) -> Task:
        return super().get(id)