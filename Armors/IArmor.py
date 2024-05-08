from abc import ABC, abstractmethod


class IArmor(ABC):
    '''
    Armor interface
    '''
    @abstractmethod
    def durability_val(self):
        '''
        Each armour has it's property durability 
        '''
