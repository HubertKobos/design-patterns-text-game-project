from abc import ABC, abstractmethod


class AbstractArmorCreator(ABC):
    '''
    Abstrack class for creators of armours
    '''
    @abstractmethod
    def _create_armour(self, armour_name: str, selected_item_params):
        '''
        Creates armour object
        '''

    def set_armour_object(self, armour_name: str, selected_item_params):
        armour = self._create_armour(armour_name, selected_item_params)

        return armour
