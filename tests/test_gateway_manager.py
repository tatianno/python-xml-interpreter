from unittest import TestCase
from unittest.mock import MagicMock
from elements import ExclusiveGateway
from exceptions import DoesExistsException
from managers import GatewayManager


class GatewayManagerTestCase(TestCase):

    def test_gateway_manager(self):
        element = MagicMock()
        element.attrib = {
            'id': 'Gateway_1s8td71',
            'name': 'a==1'
        }
        exclusive_gateway = ExclusiveGateway(**element.attrib)
        gateway_manager = GatewayManager()
        gateway_manager.set(exclusive_gateway)
        recovery_exclusive_gateway = gateway_manager.get(id='Gateway_1s8td71')
        self.assertEqual(exclusive_gateway.id, recovery_exclusive_gateway.id)
        self.assertTrue(gateway_manager.exists(id='Gateway_1s8td71'))
        gateway_manager.remove(id='Gateway_1s8td71')
        self.assertFalse(gateway_manager.exists(id='Gateway_1s8td71'))
        self.assertRaises(DoesExistsException, gateway_manager.remove, 'Gateway_1s8td71')

    def test_gateway_manager_error_type(self):
        exclusive_gateway = MagicMock()
        exclusive_gateway.attrib = {
            'id': 'Gateway_1s8td71',
            'name': 'a==1'
        }
        gateway_manager = GatewayManager()
        self.assertRaises(TypeError,gateway_manager.set, exclusive_gateway)