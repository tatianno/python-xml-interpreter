from unittest import TestCase
from unittest.mock import MagicMock
from elements import StartEvent
from processes.main_processes import MainProcess


class MainProcessTestCase(TestCase):
    
    def test_main_process_init(self):
        process = MagicMock()
        process.attrib = {
            'id': 'Process_1t8bbxl'
        }
        main_process = MainProcess(**process.attrib)
        self.assertEqual('Process_1t8bbxl', main_process.id)