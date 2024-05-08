from abc import ABC, abstractmethod


class AbstractSellerCreator(ABC):
    @abstractmethod
    def _create_seller(self, seller_type: str):
        '''
        create a seller
        '''

    def set_seller_object(self, seller_type: str):
        seller = self._create_seller(seller_type)

        return seller
