from abc import ABC, abstractmethod


class AbstractWeaponCreator(ABC):
    '''
    Abstrack class for creators of weapons
    '''
    @abstractmethod
    def _create_weapon(self, weapon_name: str, selected_item_params):
        '''
        Creates weapon
        '''

    def set_weapon_object(self, weapon_name: str, selected_item_params):
        weapon = self._create_weapon(weapon_name, selected_item_params)

        return weapon
