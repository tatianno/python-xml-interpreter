from unittest import TestCase
from unittest.mock import MagicMock
from elements import StartEvent


class StartEventTestCase(TestCase):
    
    def test_start_event_init(self):
        element = MagicMock()
        element.attrib = {
            'id': 'StartEvent_0cacn5n',
            'name': 'Start'
        }
        start_event = StartEvent(**element.attrib)
        self.assertEqual('StartEvent_0cacn5n', start_event.id)
        self.assertEqual('Start', start_event.name)
        self.assertFalse(start_event.performed)