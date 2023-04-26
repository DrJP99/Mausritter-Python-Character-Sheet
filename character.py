import json
from inventory import *
import pygame

class Character:
    def __init__(self, name = "", background = "", birthsign = "", coat = "", look = "", str = 0, dex = 0, wil = 0, hp = 0, pips = 0, level = 1, xp = 0, grit = 0, disposition = ""):
        self.name = name
        self.background = background
        self.birthsign = birthsign
        self.disposition = disposition
        self.coat = coat
        self.look = look
        self.str = str
        self.curr_str = str
        self.dex = dex
        self.curr_dex = dex
        self.wil = wil
        self.curr_wil = wil
        self.hp = hp
        self.curr_hp = hp
        self.pips = pips
        self.level = level
        self.xp = xp
        self.grit = grit
        self.inventory = PC_Inventory(pips)
        self.grit_conditions = []
    
    def print(self):
        print("Name: " + self.name)
        print("Background: " + self.background)
        print("Birthsign: " + self.birthsign)
        print("Coat: " + self.coat)
        print("Look: " + self.look)
        print(f"STR: {self.curr_str} / {self.str}")
        print(f"DEX: {self.curr_dex} / {self.dex}")
        print(f"WIL: {self.curr_wil} / {self.wil}")
        print(f"HP:  {self.hp} / {self.curr_hp}")
        print(f"Pips: {self.pips} / 250")
        print(f"Level: {self.level} | XP: {self.xp}")
        print(f"Grit: {self.grit}")
        self.inventory.print()
    
    def get_name(self):
        return self.name
    
    def get_background(self):
        return self.background
    
    def get_birthsign(self):
        return self.birthsign
    
    def get_coat(self):
        return self.coat
    
    def get_look(self):
        return self.look
    
    def get_str(self):
        return self.str
    
    def get_curr_str(self):
        return self.curr_str
    
    def get_dex(self):
        return self.dex
    
    def get_curr_dex(self):
        return self.curr_dex
    
    def get_wil(self):
        return self.wil
    
    def get_curr_wil(self):
        return self.curr_wil
    
    def get_hp(self):
        return self.hp
    
    def get_curr_hp(self):
        return self.curr_hp
    
    def get_pips(self):
        return self.pips
    
    def get_level(self):
        return self.level
    
    def get_xp(self):
        return self.xp
    
    def get_grit(self):
        return self.grit
    
    def get_inventory(self):
        return self.inventory
    
    def set_name(self, name):
        self.name = name

    def set_background(self, background):
        self.background = background

    def set_birthsign(self, birthsign):
        self.birthsign = birthsign

    def set_coat(self, coat):
        self.coat = coat

    def set_look(self, look):
        self.look = look

    def set_str(self, str):
        self.str = str

    def set_curr_str(self, curr_str):
        self.curr_str = curr_str

    def set_dex(self, dex):
        self.dex = dex

    def set_curr_dex(self, curr_dex):
        self.curr_dex = curr_dex

    def set_wil(self, wil):
        self.wil = wil

    def set_curr_wil(self, curr_wil):
        self.curr_wil = curr_wil

    def set_hp(self, hp):
        self.hp = hp

    def set_curr_hp(self, curr_hp):
        self.curr_hp = curr_hp

    def set_pips(self, pips):
        self.pips = pips

    def set_level(self, level):
        self.level = level

    def set_xp(self, xp):
        self.xp = xp
    
    def increase_xp(self, xp):
        self.xp += xp

    def set_grit(self, grit):
        self.grit = grit

    def set_inventory(self, inventory):
        self.inventory = inventory

    def load_json(self, json):
        self.name = json["name"]
        self.background = json["background"]
        self.birthsign = json["birthsign"]
        self.disposition = json["disposition"]
        self.coat = json["coat"]
        self.look = json["look"]
        self.str = json["str"]
        self.curr_str = json["curr_str"]
        self.dex = json["dex"]
        self.curr_dex = json["curr_dex"]
        self.wil = json["wil"]
        self.curr_wil = json["curr_wil"]
        self.hp = json["hp"]
        self.curr_hp = json["curr_hp"]
        self.level = json["level"]
        self.xp = json["xp"]
        self.grit = json["grit"]
        self.inventory.load_json(json["inventory"])
        self.grit_conditions = self.load_grit_from_json(json["gritted"])
        return self
    
    def save_json(self):
        json = {
            "name": self.name,
            "str": self.str,
            "curr_str": self.curr_str,
            "dex": self.dex,
            "curr_dex": self.curr_dex,
            "wil": self.wil,
            "curr_wil": self.curr_wil,
            "hp": self.hp,
            "curr_hp": self.curr_hp,
            "background": self.background,
            "inventory": self.inventory.save_json(),
            "birthsign": self.birthsign,
            "disposition": self.disposition,
            "coat": self.coat,
            "look": self.look,
            "grit": self.grit,
            "level": self.level,
            "xp": self.xp,
            "bank": {
                "pip": 0,
                "items": {}
            },
            "gritted": self.grit_to_json()
        }

        fix_name = self.name.replace(" ", "_")
        path = f"characters/{fix_name}.json"

        print("saving...")
        self.print()
        self.save_file(json, path)

    def load_file(self, path):
        with open(path, "r") as f:
            self.load_json(json.load(f))
    
    def save_file(self, data, path):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    def add_grit(self, condition):
        print(f"adding {condition.name}")
        self.grit_conditions.append(condition)
    
    def remove_grit(self, condition):
        print(f"removing {condition.name}")
        self.grit_conditions.remove(condition)

    def grit_to_json(self):
        my_list = []
        for condition in self.grit_conditions:
            my_list.append(condition.save_json())
        return my_list

    def load_grit_from_json(self, json):
        my_grit = []
        for condition in json:
            my_grit.append(Condition().load_json(condition))
        return my_grit

    def draw(self, screen):
        font = pygame.font.Font("./fonts/Brokenscript OT Cond Bold.ttf", 25)
        text = font.render(self.name, 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topright = (345, 39)
        screen.blit(text, text_rect)

        font = pygame.font.Font("./fonts/Brokenscript OT Cond Bold.ttf", 16)
        text = font.render(self.background, 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topright = (345, 82)
        screen.blit(text, text_rect)

        font = pygame.font.Font("fonts\CaveatBrush-Regular.ttf", 13)
        text = font.render(self.birthsign, 1, (0, 0, 0))
        screen.blit(text, (412, 33))

        text = font.render(self.coat, 1, (0, 0, 0))
        screen.blit(text, (412, 60))

        text = font.render(self.look, 1, (0, 0, 0))
        screen.blit(text, (412, 87))

        font = pygame.font.Font("fonts\CaveatBrush-Regular.ttf", 30)
        text = font.render(f"{self.str}", 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topright = (485, 206)
        screen.blit(text, text_rect)

        text = font.render(f"{self.dex}", 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topright = (485, 251)
        screen.blit(text, text_rect)

        text = font.render(f"{self.wil}", 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topright = (485, 296)
        screen.blit(text, text_rect)

        text = font.render(f"{self.curr_str}", 1, (50, 50, 50))
        screen.blit(text, (520, 206))

        text = font.render(f"{self.curr_dex}", 1, (50, 50, 50))
        screen.blit(text, (520, 251))

        text = font.render(f"{self.curr_wil}", 1, (50, 50, 50))
        screen.blit(text, (520, 296))

        text = font.render(f"{self.hp}", 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topright = (485, 358)
        screen.blit(text, text_rect)

        text = font.render(f"{self.curr_hp}", 1, (50, 50, 50))
        screen.blit(text, (520, 358))

        font = pygame.font.Font("fonts\CaveatBrush-Regular.ttf", 19)
        text = font.render(f"{self.inventory.pip}", 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topright = (520, 436)
        screen.blit(text, text_rect)

        font = pygame.font.Font("fonts\CaveatBrush-Regular.ttf", 30)
        text = font.render(f"{self.level}", 1, (0, 0, 0))
        screen.blit(text, (91, 705))

        text = font.render(f"{self.grit}", 1, (0, 0, 0))
        screen.blit(text, (189, 705))

        text = font.render(f"{self.xp}", 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topright = (100, 755)
        screen.blit(text, text_rect)