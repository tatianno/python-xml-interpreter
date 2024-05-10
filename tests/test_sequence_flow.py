from unittest import TestCase
from unittest.mock import MagicMock
from elements import SequenceFlow


class SequenceFlowTestCase(TestCase):

    def test_sequence_flow_init(self):
        element = MagicMock()
        element.attrib = {
            'id': 'Flow_1ubwtjr',
            'sourceRef': 'StartEvent_0cacn5n',
            'targetRef': 'Activity_03ublnq',
            'name': '1==a'
        }
        sequence_flow = SequenceFlow(**element.attrib)
        self.assertEqual('Flow_1ubwtjr', sequence_flow.id)
        self.assertEqual('StartEvent_0cacn5n', sequence_flow._source_id)
        self.assertEqual('Activity_03ublnq', sequence_flow._target_id)
        self.assertEqual('1==a', sequence_flow._name)

    def test_sequence_flow_init_without_name(self):
        element = MagicMock()
        element.attrib = {
            'id': 'Flow_1ubwtjr',
            'sourceRef': 'StartEvent_0cacn5n',
            'targetRef': 'Activity_03ublnq',
        }
        sequence_flow = SequenceFlow(**element.attrib)
        self.assertEqual('Flow_1ubwtjr', sequence_flow.id)
        self.assertEqual('StartEvent_0cacn5n', sequence_flow._source_id)
        self.assertEqual('Activity_03ublnq', sequence_flow._target_id)