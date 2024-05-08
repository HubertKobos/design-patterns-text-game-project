from .AbstractArmorCreator import AbstractArmorCreator
import Armors


class WarriorArmourCreator(AbstractArmorCreator):
    '''
    Concrete creator to create armour of a warrior
    '''

    def _create_armour(self, armour_name: str, params):
        armour = None
        if armour_name == "hauberk":
            armour = Armors.Hauberk(params)
        elif armour_name == "plate_armour":
            armour = Armors.Plate_armour(params)

        return armour
