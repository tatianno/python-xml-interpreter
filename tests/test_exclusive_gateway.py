from unittest import TestCase
from unittest.mock import MagicMock
from elements import ExclusiveGateway


class ExclusiveGatewayTestCase(TestCase):
    
    def test_exclusive_gateway_init(self):
        element = MagicMock()
        element.attrib = {
            'id': 'Gateway_1s8td71'
        }
        exclusive_gateway = ExclusiveGateway(**element.attrib)
        self.assertEqual('Gateway_1s8td71', exclusive_gateway.id)
        self.assertFalse(exclusive_gateway.performed)