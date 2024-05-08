from .IWeapon import IWeapon
import random


class Sword(IWeapon):

    def __init__(self, params):
        self.name = params[1]
        self.gold_value = int(params[2])
        self.dmg = int(params[3])
        self.durability = int(params[4])

    @property
    def dmg_val(self):
        return self.dmg

    @dmg_val.setter
    def dmg_val(self, inc_dcr_value: int):
        self.dmg = self.dmg + inc_dcr_value

    @property
    def durability_val(self):
        return self.durability

    @durability_val.setter
    def durability_val(self, inc_dcr_value: int):
        self.durability = self.durability + inc_dcr_value

    def __str__(self):
        return f"{self.name} dmg: {self.dmg}, durability: {self.durability}, value: {self.gold_value}"


class Stick(IWeapon):

    def __init__(self, params):
        self.name = params[1]
        self.gold_value = int(params[2])
        self.dmg = int(params[3])
        self.durability = int(params[4])

    @property
    def dmg_val(self):
        return self.dmg

    @dmg_val.setter
    def dmg_val(self, inc_dcr_value: int):
        self.dmg = self.dmg + inc_dcr_value

    @property
    def durability_val(self):
        return self.durability

    @durability_val.setter
    def durability_val(self, inc_dcr_value: int):
        self.durability = self.durability + inc_dcr_value

    def __str__(self):
        return f"{self.name} dmg: {self.dmg}, durability: {self.durability}, value: {self.gold_value}"
