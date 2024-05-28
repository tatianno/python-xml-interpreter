from unittest import TestCase
from unittest.mock import MagicMock
from elements import Task


class TaskTestCase(TestCase):

    def test_task_init(self):
        element = MagicMock()
        element.attrib = {
            'id': 'Activity_03ublnq',
            'name': 'Task1'
        }
        task = Task(**element.attrib)
        self.assertEqual('Activity_03ublnq', task.id)
        self.assertEqual('Task1', task.name)
        self.assertFalse(task.performed)
