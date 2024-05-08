from abc import ABC, abstractmethod


class IWeapon(ABC):
    '''
    Weapon interface
    '''

    @abstractmethod
    def dmg_val(self):
        '''
        Each weapon has it's property deamage 
        '''

    @abstractmethod
    def durability_val(self):
        '''
        Each weapon has it's property durability 
        '''
