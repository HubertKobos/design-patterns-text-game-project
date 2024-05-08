from abc import ABC, abstractmethod


class AbstractProfessionCreator(ABC):
    '''
    Abstrack class for creators of professions
    '''
    @abstractmethod
    def _create_profession(self, speciality_name: str):
        '''
        Creates profession
        '''

    def set_profession_object(self, speciality_name: str):
        profession = self._create_profession(speciality_name)

        return profession
