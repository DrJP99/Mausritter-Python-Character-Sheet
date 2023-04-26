from my_enums import Dice, Weapon_Class, Armor_Class

class Item:
    def __init__(self, name = "", max_durability = 3, durability = 0, size_x = 1, size_y = 1, cost = 0):
        self.name = name
        self.max_durability = max_durability
        self.durability = durability
        self.size_x = size_x
        self.size_y = size_y
        self.cost = cost
        self.type = "item"
    
    def __str__(self) -> str:
        return self.name
    ### SETTERS AND GETTERS ###

    def set_name(self, name):
        self.name = name
    
    def set_max_durability(self, max_durability):
        self.max_durability = max_durability
    
    def increase_durability(self, n = 1):
        if self.durability < self.max_durability:
            self.durability += n
    
    def fix(self):
        self.durability = 0
    
    def set_size_x(self, size_x):
        self.size_x = size_x
    
    def set_size_y(self, size_y):
        self.size_y = size_y
    
    def set_cost(self, cost):
        self.cost = cost
    
    def get_name(self):
        return self.name
    
    def get_max_durability(self):
        return self.max_durability

    def get_durability(self):
        return self.durability

    def get_size_x(self):
        return self.size_x
    
    def get_size_y(self):
        return self.size_y
    
    def get_cost(self):
        return self.cost
    
    def load_json(self, json):
        self.name = json["name"]
        self.max_durability = json["max_durability"]
        self.durability = json["durability"]
        self.size_x = json["size_x"]
        self.size_y = json["size_y"]
        self.cost = json["cost"]
        return self

    def save_json(self):
        json = {}
        json["type"] = self.type
        json["name"] = self.name
        json["max_durability"] = self.max_durability
        json["durability"] = self.durability
        json["size_x"] = self.size_x
        json["size_y"] = self.size_y
        json["cost"] = self.cost
        return json

class Weapon(Item):
    def __init__(self, name = "", weapon_class = Weapon_Class.light, max_durability = 3, size_x = 1, size_y = 1, cost = 0, hitdie = Dice.d6, durability=0):
        super().__init__(name, max_durability, durability, size_x, size_y, cost)
        self.hitdie = hitdie
        self.weapon_class = weapon_class
        self.cost = cost
        self.update_atts(self.weapon_class)
        self.type = "weapon"
    
    def set_hitdie(self, hitdie):
        self.hitdie = hitdie
    
    def get_hitdie(self):
        return self.hitdie
    
    def set_weapon_class(self, weapon_class):
        self.weapon_class = weapon_class
    
    def get_weapon_class(self):
        return self.weapon_class
    
    def update_atts(self, weapon_class):
        match weapon_class:
            case Weapon_Class.light:
                self.hitdie = Dice.d6
                self.cost = 10
                self.size_x = 1
                self.size_y = 1
            case Weapon_Class.medium:
                self.hitdie = [Dice.d6, Dice.d8]
                self.cost = 20
                self.size_x = 1
                self.size_y = 1
            case Weapon_Class.heavy:
                self.hitdie = Dice.d10
                self.cost = 40
                self.size_x = 1
                self.size_y = 2
            case Weapon_Class.improvised:
                self.hitdie = Dice.d6
                self.cost = 0
                self.size_x = 1
                self.size_y = 1
            case Weapon_Class.light_ranged:
                self.hitdie = Dice.d6
                self.cost = 10
                self.size_x = 1
                self.size_y = 1
            case Weapon_Class.heavy_ranged:
                self.hitdie = Dice.d8
                self.cost = 40
                self.size_x = 1
                self.size_y = 2
            case Weapon_Class.ammunition:
                self.hitdie = None
                self.cost = self.cost
                self.size_x = 1
                self.size_y = 1
    
    def load_json(self, json):
        super().load_json(json)
        self.weapon_class = Weapon_Class(json["class"])
        self.update_atts(self.weapon_class)
        return self
    
    def save_json(self):
        json = super().save_json()
        json["class"] = self.weapon_class.value
        if (type(self.hitdie) == list):
            json["hitdie"] = [hitdie.value for hitdie in self.hitdie]
        else:
            json["hitdie"] = self.hitdie.value
        return json

class Magic_Weapon(Weapon):
    def __init__(self, name = "", weapon_class = Weapon_Class.light, ability = "", durability = 0, size_x = 1, size_y = 1):
        super().__init__(name, weapon_class, durability, size_x, size_y)
        self.ability = ability
        self.magic = True
        self.cost = -1
        self.type = "magic weapon"
    
    def set_magic(self, magic):
        self.magic = magic
    
    def get_magic(self):
        return self.magic
    
    def set_ability(self, ability):
        self.ability = ability
    
    def get_ability(self):
        return self.ability

    def load_json(self, json):
        super().load_json(json)
        self.ability = json["ability"]
        self.magic = json["magic"]
        return self

    def save_json(self):
        json = super().save_json()
        json["ability"] = self.ability
        json["magic"] = self.magic
        return json
        
class Armor(Item):
    def __init__(self, name = "", armor_class = Armor_Class.light, max_durability = 3, durability = 0, size_x = 1, size_y = 1, defence = 1):
        super().__init__(name, max_durability, durability, size_x, size_y)
        self.armor_class = armor_class
        self.size_x = size_x
        self.size_y = size_y
        self.defence = defence
        self.update_atts(self.armor_class)
        self.type = "armor"
    
    def set_defence(self, defence):
        self.defence = defence
    
    def get_defence(self):
        return self.defence

    def set_armor_class(self, armor_class):
        self.armor_class = armor_class
    
    def get_armor_class(self):
        return self.armor_class

    def update_atts(self, armor_class):
        match armor_class:
            case Armor_Class.light:
                self.defence = 1
                self.cost = 150
                self.size_x = 2
                self.size_y = 1
            case Armor_Class.heavy:
                self.defence = 1
                self.cost = 500
                self.size_x = 1
                self.size_y = 2

    def load_json(self, json):
        super().load_json(json)
        self.armor_class = Armor_Class(json["class"])
        self.update_atts(self.armor_class)
        return self

    def save_json(self):
        json = super().save_json()
        json["class"] = self.armor_class.value
        json["defence"] = self.defence
        return json

class Purse(Item):
    def __init__(self, pip = 0, max_pip = 250):
        super().__init__("Pip purse", 0, 0, 1, 1)
        self.pip = pip
        self.max_pip = max_pip
        self.cost = pip
        self.type = "purse"
        
    def set_pip(self, pip):
        self.pip = pip
        self.cost = pip
    
    def get_pip(self):
        return self.pip

    def set_max_pip(self, max_pip):
        self.max_pip = max_pip
    
    def get_max_pip(self):
        return self.max_pip

    def increase_pip(self, pip):
        if self.pip + pip <= self.max_pip:
            self.pip += pip
        else:
            residual = self.pip + pip - self.max_pip
            self.pip = self.max_pip
            print("All those pips can\'t fit in your purse! You have {} pips left over.".format(residual))
        self.cost = self.pip
    
    def decrease_pip(self, pip):
        if self.pip - pip >= 0:
            self.pip -= pip
        else:
            print("You don\'t have that many pips in your purse!")
        self.cost = self.pip
    
    def load_json(self, json):
        super().load_json(json)
        self.pip = json["pip"]
        self.max_pip = json["max_pip"]
        return self

    def save_json(self):
        json = super().save_json()
        json["pip"] = self.pip
        json["max_pip"] = self.max_pip
        return json


class Spell(Item):
    def __init__(self, name = "", effect = "", recharge = ""):
        super().__init__(name, 3, 0, 1, 1)
        self.effect = effect
        self.recharge = recharge
        self.cost = -1
        self.type = "spell"
    
    def set_effect(self, effect):
        self.effect = effect

    def get_effect(self):
        return self.effect

    def set_recharge(self, recharge):
        self.recharge = recharge
    
    def get_recharge(self):
        return self.recharge

    def load_json(self, json):
        super().load_json(json)
        self.effect = json["effect"]
        self.recharge = json["recharge"]
        return self

    def save_json(self):
        json = super().save_json()
        json["effect"] = self.effect
        json["recharge"] = self.recharge
        return json