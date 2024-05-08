from .IProfession import IProfession
from Weapons import IWeapon
from Armors import IArmor
import random


class HolyWarriorSpeciality(IProfession):
    '''
    Holy Warrior profession for player
    '''

    def __init__(self):
        self._weapon = None
        self._armor = None

    def attack(self):
        print("You attacked enemy !")
        return self._weapon.dmg_val

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, weapon: IWeapon):
        print(f"You just equipped {weapon} !")
        self._weapon = weapon

    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, armor: IArmor):
        self._armor = armor

    def __str__(self):
        return f"Creating new {__class__.__name__}"
