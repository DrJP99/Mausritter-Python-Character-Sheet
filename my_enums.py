from enum import Enum

class Dice(Enum):
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100

class Weapon_Class(Enum):
    light = "Light"
    medium = "Medium"
    heavy = "Heavy"
    improvised = "Improvised"
    light_ranged = "Light Ranged"
    heavy_ranged = "Heavy Ranged"
    ammunition = "Ammunition"

class Armor_Class(Enum):
    light = "Light"
    heavy = "Heavy"
