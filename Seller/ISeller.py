from abc import ABC, abstractmethod


class ISeller(ABC):
    '''
    Abstract class of sellers
    '''

    @abstractmethod
    def load_items_from_json(self):
        '''
        loader functions to load items from json files
        '''

    @abstractmethod
    def display_information_about_armours(self):
        '''
        display informations about available armours from json file
        '''

    @abstractmethod
    def display_information_about_weapons(self):
        '''
        display informations about available weapons from json file
        '''
