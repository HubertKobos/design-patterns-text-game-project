from abc import ABC, abstractmethod


class IProfession(ABC):
    '''
    Enemy interface
    '''
    @abstractmethod
    def attack(self):
        '''
        Attack enemy
        '''

    @abstractmethod
    def weapon(self):
        '''
        Set what weapon will player fight with
        '''

    @abstractmethod
    def armor(self):
        '''
        Set player armor
        '''
