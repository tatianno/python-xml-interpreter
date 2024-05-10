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
    
    def test_main_process_set_start_event(self):
        process = MagicMock()
        process.attrib = {
            'id': 'Process_1t8bbxl'
        }
        main_process = MainProcess(**process.attrib)
        element = MagicMock()
        element.attrib = {
            'id': 'StartEvent_0cacn5n',
            'name': 'Start'
        }
        start_event = StartEvent(**element.attrib)
        main_process.set_start_event(start_event)
        self.assertEqual('StartEvent_0cacn5n', main_process.start_event.id)
    
    def test_main_process_set_start_event_type_error(self):
        process = MagicMock()
        process.attrib = {
            'id': 'Process_1t8bbxl'
        }
        main_process = MainProcess(**process.attrib)
        start_event = MagicMock()
        start_event.attrib = {
            'id': 'StartEvent_0cacn5n',
            'name': 'Start'
        }
        self.assertRaises(TypeError, main_process.set_start_event, start_event)