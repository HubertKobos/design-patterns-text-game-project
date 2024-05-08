from .IEnemy import IEnemy
import random
import json
import copy

ARMORS_JSON_FILE_PATH = "Equipment/armors.json"
WEAPONS_JSON_FILE_PATH = "Equipment\weapons.json"


class BasicMageEnemy(IEnemy):
    '''
    Basic enemy of a class mage
    '''

    def __init__(self):
        self._is_resurected = False
        print(f"Creating an instance of {__class__.__name__}")

    def get_random_armor(self):
        with open(ARMORS_JSON_FILE_PATH) as json_file:
            json_data = json.load(json_file)
            archer_armors = json_data['archer_armors']
            self.random_armor = random.choice(archer_armors)
            self._armor_durability = int(self.random_armor['durability'])

    @property
    def armor_durability_val(self):
        return self._armor_durability

    @armor_durability_val.setter
    def armor_durability_val(self, inc_dec_val):
        self._armor_durability = self._armor_durability + inc_dec_val

    def get_random_weapon(self):
        with open(WEAPONS_JSON_FILE_PATH) as json_file:
            json_data = json.load(json_file)
            archer_weapons = json_data['archer_weapons']
            self.random_weapon = random.choice(archer_weapons)
            self._weapon_dmg = int(self.random_weapon['dmg'])

    @property
    def weapon_dmg_val(self):
        return self._weapon_dmg

    @weapon_dmg_val.setter
    def weapon_dmg_val(self, inc_dec_val):
        self._weapon_dmg = self._weapon_dmg + inc_dec_val

    def set_weapon_dmg_val(self, inc_dev_val):
        self._weapon_dmg = self._weapon_dmg + inc_dev_val

    @property
    def is_resurected_prop(self):
        return self._is_resurected

    @is_resurected_prop.setter
    def set_is_resurected(self, is_resurected):
        self._is_resurected = is_resurected

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{__class__.__name__} with armor: {self.random_armor['name']} (durability: {self._armor_durability}) and weapon: {self.random_weapon['name']} (dmg: {self.weapon_dmg_val})"


class ExperiencedMageEnemy(IEnemy):
    '''
    Experienced enemy of a class mage
    '''

    def __init__(self):
        self._is_resurected = False
        print(f"Creating an instance of {__class__.__name__}")

    def get_random_armor(self):
        with open(ARMORS_JSON_FILE_PATH) as json_file:
            json_data = json.load(json_file)
            archer_armors = json_data['archer_armors']
            self.random_armor = random.choice(archer_armors)
            self._armor_durability = int(self.random_armor['durability'])

    @property
    def armor_durability_val(self):
        return self._armor_durability

    @armor_durability_val.setter
    def armor_durability_val(self, inc_dec_val):
        self._armor_durability = self._armor_durability + inc_dec_val

    def get_random_weapon(self):
        with open(WEAPONS_JSON_FILE_PATH) as json_file:
            json_data = json.load(json_file)
            archer_weapons = json_data['archer_weapons']
            self.random_weapon = random.choice(archer_weapons)
            self._weapon_dmg = int(self.random_weapon['dmg'])

    @property
    def weapon_dmg_val(self):
        return self._weapon_dmg

    @weapon_dmg_val.setter
    def weapon_dmg_val(self, inc_dec_val):
        self._weapon_dmg = self._weapon_dmg + inc_dec_val

    def set_weapon_dmg_val(self, inc_dev_val):
        self._weapon_dmg = self._weapon_dmg + inc_dev_val

    @property
    def is_resurected_prop(self):
        return self._is_resurected

    @is_resurected_prop.setter
    def set_is_resurected(self, is_resurected):
        self._is_resurected = is_resurected

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{__class__.__name__} with armor: {self.random_armor['name']} (durability: {self._armor_durability}) and weapon: {self.random_weapon['name']} (dmg: {self.weapon_dmg_val})"
