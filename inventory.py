from item import *
from condition import Condition

class Inventory:
    def __init__(self):
        self.main_rows = 2
        self.main_cols = 1

        self.back_rows = 2
        self.back_cols = 2

        self.main = [[None for i in range(self.main_cols)] for j in range(self.main_rows)]
        self.back = [[None for i in range(self.back_cols)] for j in range(self.back_rows)]

        self.occupied_main = [[False for i in range(self.main_cols)] for j in range(self.main_rows)]
        self.occupied_back = [[False for i in range(self.back_cols)] for j in range(self.back_rows)]
        
        self.generate_matrix()

    
    def generate_matrix(self):
        for i in range(self.main_rows):
            for j in range(self.main_cols):
                self.main[i][j] = None
                self.occupied_main[i][j] = False
        
        for i in range(self.back_rows):
            for j in range(self.back_cols):
                self.back[i][j] = None
                self.occupied_back[i][j] = False

    def check_main(self, x, y):
        try:
            return self.occupied_main[x][y]
        except IndexError:
            print(f"Index out of range (Position: {x}, {y})")
            return True

    def check_back(self, x, y):
        try:
            return self.occupied_back[x][y]
        except IndexError:
            print("Index out of range")
            return True

    def add_item(self, Item, location, x, y):
        print(f"Adding item {Item.name} to {location} at {x}, {y}")
        match location:
            case "main":
                if not self.check_main(x, y):
                    if (Item.size_x == 2 and Item.size_y == 1 and not self.check_main(x, y + 1)):
                        self.main[x][y] = Item
                        self.occupied_main[x][y] = True
                        self.occupied_main[x][y + 1] = True
                        return True
                    elif (Item.size_x == 1 and Item.size_y == 2 and not self.check_main(x + 1, y)):
                        self.main[x][y] = Item
                        self.occupied_main[x][y] = True
                        self.occupied_main[x + 1][y] = True
                        return True
                    elif (Item.size_x == 1 and Item.size_y == 1):
                        self.main[x][y] = Item
                        self.occupied_main[x][y] = True
                        return True
            case "back":
                if not self.check_back(x, y):
                    if (Item.size_x == 2 and Item.size_y == 1 and not self.check_back(x, y + 1)):
                        self.back[x][y] = Item
                        self.occupied_back[x][y] = True
                        self.occupied_back[x][y + 1] = True
                        return True
                    elif (Item.size_x == 1 and Item.size_y == 2 and not self.check_back(x + 1, y)):
                        self.back[x][y] = Item
                        self.occupied_back[x][y] = True
                        self.occupied_back[x + 1][y] = True
                        return True
                    elif (Item.size_x == 1 and Item.size_y == 1):
                        self.back[x][y] = Item
                        self.occupied_back[x][y] = True
                        return True
                    print("Already occupied")
                print("Already occupied")
        return False
    
    def add_condition(self, condition, location, x, y):
        print(f"Adding condition {condition.name} to {location} at {x}, {y}")
        match location:
            case "main":
                if not self.check_main(x, y):
                    if (condition.size_x == 2 and condition.size_y == 1 and not self.check_main(x, y + 1)):
                        self.main[x][y] = condition
                        self.occupied_main[x][y] = True
                        self.occupied_main[x][y + 1] = True
                        return True
                    elif (condition.size_x == 1 and condition.size_y == 2 and not self.check_main(x + 1, y)):
                        self.main[x][y] = condition
                        self.occupied_main[x][y] = True
                        self.occupied_main[x + 1][y] = True
                        return True
                    elif (condition.size_x == 1 and condition.size_y == 1):
                        self.main[x][y] = condition
                        self.occupied_main[x][y] = True
                        return True
            case "back":
                if not self.check_back(x, y):
                    if (condition.size_x == 2 and condition.size_y == 1 and not self.check_back(x, y + 1)):
                        self.back[x][y] = condition
                        self.occupied_back[x][y] = True
                        self.occupied_back[x][y + 1] = True
                        return True
                    elif (condition.size_x == 1 and condition.size_y == 2 and not self.check_back(x + 1, y)):
                        self.back[x][y] = condition
                        self.occupied_back[x][y] = True
                        self.occupied_back[x + 1][y] = True
                        return True
                    elif (condition.size_x == 1 and condition.size_y == 1):
                        self.back[x][y] = condition
                        self.occupied_back[x][y] = True
                        return True
                    print("Already occupied")
                print("Already occupied")
        return False
    
    def remove_item(self, Item, location, x, y):
        print(f"Removing {Item.name} from {location} at {x}, {y}")
        match location:
            case "main":
                if (Item.size_x == 2 and Item.size_y == 1):
                    self.main[x][y] = None
                    self.occupied_main[x][y] = False
                    self.occupied_main[x][y + 1] = False
                    return True
                elif (Item.size_x == 1 and Item.size_y == 2):
                    self.main[x][y] = None
                    self.occupied_main[x][y] = False
                    self.occupied_main[x + 1][y] = False
                    return True
                elif (Item.size_x == 1 and Item.size_y == 1):
                    self.main[x][y] = None
                    self.occupied_main[x][y] = False
                    return True
            case "back":
                if (Item.size_x == 2 and Item.size_y == 1):
                    self.back[x][y] = None
                    self.occupied_back[x][y] = False
                    self.occupied_back[x][y + 1] = False
                    return True
                elif (Item.size_x == 1 and Item.size_y == 2):
                    self.back[x][y] = None
                    self.occupied_back[x][y] = False
                    self.occupied_back[x + 1][y] = False
                    return True
                elif (Item.size_x == 1 and Item.size_y == 1):
                    self.back[x][y] = None
                    self.occupied_back[x][y] = False
                    return True
    
    def remove_condition(self, condition, location, x, y):
        print(f"Removing {condition.name} from {location} at {x}, {y}")
        match location:
            case "main":
                if (condition.size_x == 2 and condition.size_y == 1):
                    self.main[x][y] = None
                    self.occupied_main[x][y] = False
                    self.occupied_main[x][y + 1] = False
                    return True
                elif (condition.size_x == 1 and condition.size_y == 2):
                    self.main[x][y] = None
                    self.occupied_main[x][y] = False
                    self.occupied_main[x + 1][y] = False
                    return True
                elif (condition.size_x == 1 and condition.size_y == 1):
                    self.main[x][y] = None
                    self.occupied_main[x][y] = False
                    return True
            case "back":
                if (condition.size_x == 2 and condition.size_y == 1):
                    self.back[x][y] = None
                    self.occupied_back[x][y] = False
                    self.occupied_back[x][y + 1] = False
                    return True
                elif (condition.size_x == 1 and condition.size_y == 2):
                    self.back[x][y] = None
                    self.occupied_back[x][y] = False
                    self.occupied_back[x + 1][y] = False
                    return True
                elif (condition.size_x == 1 and condition.size_y == 1):
                    self.back[x][y] = None
                    self.occupied_back[x][y] = False
                    return True
        
    
    def load_item(self, json):
        match (json["type"]):
            case "item":
                return Item().load_json(json)
            case "weapon":
                return Weapon().load_json(json)
            case "magic weapon":
                return Magic_Weapon().load_json(json)
            case "armor":
                return Armor().load_json(json)
            case "purse":
                return Purse().load_json(json)
            case "spell":
                return Spell().load_json(json)
            case "condition":
                return Condition().load_json(json)


    def print(self):
        print("Main:\t")
        for i in range(self.main_rows):
            for j in range(self.main_cols):
                if self.main[i][j] != None:
                    print(self.main[i][j].get_name())
                else:
                    print("---")
            print("\n")
        print("Back:\t")
        for i in range(self.back_rows):
            for j in range(self.back_cols):
                if self.back[i][j] != None:
                    print(self.back[i][j].get_name())
                else:
                    print("---")
            print("\n")
    



class PC_Inventory(Inventory):
    def __init__(self, pip=0):
        super().__init__()
        self.pip = pip
        self.max_pip = 250

        self.main_rows = 2
        self.main_cols = 2

        self.back_rows = 2
        self.back_cols = 3

        self.main = [[None for i in range(self.main_cols)] for j in range(self.main_rows)]
        self.back = [[None for i in range(self.back_cols)] for j in range(self.back_rows)]

        self.occupied_main = [[False for i in range(self.main_cols)] for j in range(self.main_rows)]
        self.occupied_back = [[False for i in range(self.back_cols)] for j in range(self.back_rows)]

        self.generate_matrix()
        

    def set_pip(self, pip):
        self.pip = pip
    
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

    def decrease_pip(self, pip):
        if self.pip - pip >= 0:
            self.pip -= pip
        else:
            print("You don\'t have that many pips!")
    

            

    def load_json(self, json):
        self.pip = json["pip"]
        if (json["main"] != None):
            item = self.load_item(json["main"])
            self.add_item(item, "main", 0, 0)
        else:
            self.occupied_main[0][0] = False
        if (json["off"] != None):
            item = self.load_item(json["off"])
            self.add_item(item, "main", 1, 0)
        else:
            self.occupied_main[1][0] = False
        if (json["body_1"] != None):
            item = self.load_item(json["body_1"])
            print(f"body_1: {item.get_name()} at {0}, {1}")
            self.add_item(item, "main", 0, 1)
        else:
            self.occupied_main[0][1] = False
        if (json["body_2"] != None):
            item = self.load_item(json["body_2"])
            self.add_item(item, "main", 1, 1)
        else:
            self.occupied_main[1][1] = False
        if (json["back_1"] != None):
            item = self.load_item(json["back_1"])
            self.add_item(item, "back", 0, 0)
        else:
            self.occupied_back[0][0] = False
        if (json["back_2"] != None):
            item = self.load_item(json["back_2"])
            self.add_item(item, "back", 0, 1)
        else:
            self.occupied_back[0][1] = False
        if (json["back_3"] != None):
            item = self.load_item(json["back_3"])
            self.add_item(item, "back", 0, 2)
        else:
            self.occupied_back[0][2] = False
        if (json["back_4"] != None):
            item = self.load_item(json["back_4"])
            self.add_item(item, "back", 1, 0)
        else:
            self.occupied_back[1][0] = False
        if (json["back_5"] != None):
            item = self.load_item(json["back_5"])
            self.add_item(item, "back", 1, 1)
        else:
            self.occupied_back[1][1] = False
        if (json["back_6"] != None):
            item = self.load_item(json["back_6"])
            self.add_item(item, "back", 1, 2)
        else:
            self.occupied_back[1][2] = False
        
        return item

    def save_json(self):
        json = {
            "pip": self.pip,
            "main": self.main[0][0].save_json() if self.main[0][0] != None else None,
            "off": self.main[1][0].save_json() if self.main[1][0] != None else None,
            "body_1": self.main[0][1].save_json() if self.main[0][1] != None else None,
            "body_2": self.main[1][1].save_json() if self.main[1][1] != None else None,
            "back_1": self.back[0][0].save_json() if self.back[0][0] != None else None,
            "back_2": self.back[0][1].save_json() if self.back[0][1] != None else None,
            "back_3": self.back[0][2].save_json() if self.back[0][2] != None else None,
            "back_4": self.back[1][0].save_json() if self.back[1][0] != None else None,
            "back_5": self.back[1][1].save_json() if self.back[1][1] != None else None,
            "back_6": self.back[1][2].save_json() if self.back[1][2] != None else None
        }

        return json

class NPC_Inventory(Inventory):
    def __init__(self):
        super().__init__()