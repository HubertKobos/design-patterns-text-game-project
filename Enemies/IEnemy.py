from abc import ABC, abstractmethod


class IEnemy(ABC):
    '''
    Enemy interface
    '''

    @abstractmethod
    def get_random_armor(self):
        '''
        Choose random armor for enemy
        '''

    @abstractmethod
    def get_random_weapon(self):
        '''
        Choose random weapon for enemy
        '''

    @abstractmethod
    def clone(self):
        pass
