from .AbstractSellerCreator import AbstractSellerCreator
import Seller


class WarriorSellerCreator(AbstractSellerCreator):
    def _create_seller(self, seller_type: str):
        seller = None
        if seller_type == "warrior_seller":
            seller = Seller.Armorer()

        return seller
