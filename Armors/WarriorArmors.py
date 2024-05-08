from .IArmor import IArmor


class Hauberk(IArmor):

    def __init__(self, params):
        pass

    @property
    def durability_val(self):
        return self.durability

    @durability_val.setter
    def durability_val(self, inc_dcr_value: int):
        self.durability = self.durability + inc_dcr_value


class Plate_armour(IArmor):

    def __init__(self, params):
        pass

    @property
    def durability_val(self):
        return self.durability

    @durability_val.setter
    def durability_val(self, inc_dcr_value: int):
        self.durability = self.durability + inc_dcr_value
