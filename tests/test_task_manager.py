from unittest import TestCase
from unittest.mock import MagicMock
from elements import Task
from exceptions import DoesExistsException
from managers import TaskManager


class TaskManagerTestCase(TestCase):
    def test_task_manager(self):
        task_element = MagicMock()
        task_element.attrib = {
            'id': 'Activity_03ublnq',
            'name': 'Task1'
        }
        task_manager = TaskManager()
        task = Task(**task_element.attrib)
        task_manager.set(task)
        recovery_task = task_manager.get(id='Activity_03ublnq')
        self.assertEqual(task.id, recovery_task.id)
        self.assertTrue(task_manager.exists(id='Activity_03ublnq'))
        task_manager.remove(id=task.id)
        self.assertFalse(task_manager.exists(id='Activity_03ublnq'))
        self.assertRaises(DoesExistsException, task_manager.remove, 'Activity_03ublnq')

    def test_main_process_type_error_task(self):
        task = MagicMock()
        task.id = 'Activity_03ublnq',
        task_manager = TaskManager()
        self.assertRaises(TypeError,task_manager.set, task)