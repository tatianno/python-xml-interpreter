from elements import ExclusiveGateway
from managers.generic_manager import GenericManager


class GatewayManager(GenericManager):

    def set(self, exclusive_gateway: ExclusiveGateway) -> None:

        if type(exclusive_gateway) != ExclusiveGateway:
            raise TypeError('Only exclusive gateways objects are supported!')
        
        super().set(exclusive_gateway)
    
    def get(self, id: str) -> ExclusiveGateway:
        return super().get(id)