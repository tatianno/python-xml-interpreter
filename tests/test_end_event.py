from unittest import TestCase
from unittest.mock import MagicMock
from elements import EndEvent


class EndEventTestCase(TestCase):
    
    def test_end_event_init(self):
        element = MagicMock()
        element.attrib = {
            'id': 'EndEvent_0cacn5n',
            'name': 'Start'
        }
        end_event = EndEvent(**element.attrib)
        self.assertEqual('EndEvent_0cacn5n', end_event.id)
        self.assertEqual('Start', end_event.name)
        self.assertFalse(end_event.performed)