from .AbstractWeaponCreator import AbstractWeaponCreator
import Weapons


class WarriorWeaponCreator(AbstractWeaponCreator):
    '''
    Concrete creator to create warrior weapons 
    '''

    def _create_weapon(self, weapon_name: str, selected_item_params):
        weapon = None
        if weapon_name == "sword":
            weapon = Weapons.Sword(selected_item_params)
        elif weapon_name == "stick":
            weapon = Weapons.Stick(selected_item_params)

        return weapon
