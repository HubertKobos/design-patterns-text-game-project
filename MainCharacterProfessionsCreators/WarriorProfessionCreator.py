from .AbstractProfessionCreator import AbstractProfessionCreator
import WarriorProfessionSpecialities


class WarriorProfessionCreator(AbstractProfessionCreator):
    '''
    Concrete creator to create enemy of type warrior
    '''

    def _create_profession(self, speciality_name: str):
        speciality = None
        if speciality_name == "dark_warrior":
            speciality = WarriorProfessionSpecialities.DarkWarriorSpeciality()
        elif speciality_name == "holy_warrior":
            speciality = WarriorProfessionSpecialities.HolyWarriorSpeciality()

        return speciality
