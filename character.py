import json
from inventory import *
import pygame
from pygame.locals import *
from my_enums import Dice
from button import My_Button

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

        bh = 46
        bw = 30

        start_y = 201
        start_x = 548
        offset = 0

        self.str_button = Attribute_Buttons(start_x, start_y + offset, bw, bh, "str")
        offset += bh -1
        self.dex_button = Attribute_Buttons(start_x, start_y + offset, bw, bh, "dex")
        offset += bh
        self.wil_button = Attribute_Buttons(start_x, start_y + offset, bw, bh, "wil")
        offset += bh + 15
        self.hp_button = Attribute_Buttons(start_x, start_y + offset, bw, bh, "hp")

        self.att_buttons = [self.str_button, self.dex_button, self.wil_button, self.hp_button]

        self.edit_button = My_Button(74, 790, 50, 25, "Edit")
        self.close_rec = None

        self.edit_xp_box = Text_Box(74, 790, 50, 25, f"0")

    
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
        if (self.xp + xp) <= 0:
            self.xp = 0
        else:
            self.xp += xp

    def set_grit(self, grit):
        self.grit = grit

    def set_inventory(self, inventory):
        self.inventory = inventory

    def increase_attribute(self, attribute, n = 1):
        if attribute == "str":
            if self.curr_str < self.str:
                self.curr_str += n
        elif attribute == "dex":
            if self.curr_dex < self.dex:
                self.curr_dex += n
        elif attribute == "wil":
            if self.curr_wil < self.wil:
                self.curr_wil += n
        elif attribute == "hp":
            if self.curr_hp < self.hp:
                self.curr_hp += n
    
    def decrease_attribute(self, attribute, n = 1):
        if attribute == "str":
            if self.curr_str > 0:
                self.curr_str -= n
        elif attribute == "dex":
            if self.curr_dex > 0:
                self.curr_dex -= n
        elif attribute == "wil":
            if self.curr_wil > 0:
                self.curr_wil -= n
        elif attribute == "hp":
            if self.curr_hp > 0:
                self.curr_hp -= n
    
    def get_att_buttons(self):
        return self.att_buttons

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
        # self.print()
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

    def click_buttons(self, pos):
        for button in self.att_buttons:
            if button.click_increase(pos):
                self.increase_attribute(button.attribute)
            elif button.click_decrease(pos):
                self.decrease_attribute(button.attribute)
    
    def can_level_up(self):
        if (self.level == 1):
            if self.xp < 1000:
                return False
        elif (self.level == 2):
            if self.xp < 3000:
                return False
        elif (self.level == 3):
            if self.xp < 6000:
                return False
        elif (self.level >= 4):
            if self.xp < 6000 + (self.level - 3) * 5000:
                return False
        return True

    def level_up(self, roll_str = 1, roll_dex = 1, roll_wil = 1, roll_hp = 1):
        if self.can_level_up():
            self.level += 1
            if roll_str > self.str:
                self.str += 1
            if roll_dex > self.dex:
                self.dex += 1
            if roll_wil > self.wil:
                self.wil += 1

            if roll_hp > self.hp:
                self.hp = roll_hp
            else:
                self.hp += 1
    
    def get_grit_by_level(level):
        match level:
            case 1:
                return 0
            case 2:
                return 1
            case 3:
                return 2
            case 4:
                return 2
            case _:
                return 3
    
    def get_hitdie_by_level(level):
        if level >= 4:
            n = 4
        else:
            n = level
        
        return n, Dice.d6

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
        screen.blit(text, (510, 206))

        text = font.render(f"{self.curr_dex}", 1, (50, 50, 50))
        screen.blit(text, (510, 251))

        text = font.render(f"{self.curr_wil}", 1, (50, 50, 50))
        screen.blit(text, (510, 296))

        text = font.render(f"{self.hp}", 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topright = (485, 358)
        screen.blit(text, text_rect)

        text = font.render(f"{self.curr_hp}", 1, (50, 50, 50))
        screen.blit(text, (510, 358))

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

        for button in self.att_buttons:
            button.draw(screen)
        
        self.edit_button.draw(screen)
    
    def get_close_rec(self):
        return self.close_rec

    def edit_xp_ui_window(self, screen):
        self.window_rec = pygame.Rect(screen.get_width() / 2 - 200, screen.get_height() / 2 - 150, 400, 200)
        pygame.draw.rect(screen, (255, 255, 255), self.window_rec)
        pygame.draw.rect(screen, (0, 0, 0), self.window_rec, 1)

        self.close_rec = pygame.Rect( self.window_rec.x + self.window_rec.width - 35, self.window_rec.y + 10, 25, 25)
        pygame.draw.rect(screen, (255, 0, 0), self.close_rec)
        
        title_font = pygame.font.Font("./fonts/Brokenscript OT Cond Bold.ttf", 25)
        title_text = title_font.render(f"Edit XP points", 1, (0, 0, 0))
        screen.blit(title_text, (self.window_rec.width / 2 + self.window_rec.x - title_text.get_width() / 2, self.window_rec.y + 10))

        title_rect = title_text.get_rect()
        pygame.draw.line(screen, (0, 0, 0), (self.window_rec.x, self.window_rec.y + title_rect.y + title_rect.height + 15), (self.window_rec.x + self.window_rec.width - 1, self.window_rec.y + title_rect.y + title_rect.height + 15), 1)

        curr_font = pygame.font.SysFont("Bahnschrift", 20)

        curr_text = curr_font.render(f"Current XP: {self.xp}", 1, (0, 0, 0))
        curr_text_rect = curr_text.get_rect()
        curr_text_rect.topleft = (self.window_rec.x + self.window_rec.width / 2 - curr_text_rect.width/2, self.window_rec.y + title_rect.y + title_rect.height + 25)
        screen.blit(curr_text, curr_text_rect)

        self.edit_xp_box.set_size(self.window_rec.width / 2 - 10, self.edit_xp_box.size_y)
        self.edit_xp_box.set_pos(self.window_rec.x + self.window_rec.width / 2 - self.edit_xp_box.size_x / 2, self.window_rec.y + self.window_rec.height / 2)
        self.edit_xp_box.draw(screen)

        self.decrease_btn = My_Button(self.edit_xp_box.x, self.edit_xp_box.y + self.edit_xp_box.size_y + 10, self.edit_xp_box.size_x / 2 - 5, 30, "Remove", text_color=(150, 10, 10))
        self.decrease_btn.draw(screen)

        self.increase_btn = My_Button(self.edit_xp_box.x + self.edit_xp_box.size_x / 2 + 5, self.edit_xp_box.y + self.edit_xp_box.size_y + 10, self.edit_xp_box.size_x / 2 - 5, 30, "Add", text_color=(0, 100, 0))
        self.increase_btn.draw(screen)


    def close_edit_xp_ui(self):
        self.close_rec = None



class Attribute_Buttons:
    def __init__(self, x, y, size_x, size_y, attribute):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

        self.increase_rect = pygame.Rect(x, y, size_x, size_y / 2)
        self.decrease_rect = pygame.Rect(x, y + size_y / 2, size_x, size_y / 2)

        self.attribute = attribute

        self.font = pygame.font.SysFont("Bahnschrift", 20)
    
    def click_increase(self, pos):
        if self.increase_rect.collidepoint(pos):
            return True
        return False

    def click_decrease(self, pos):
        if self.decrease_rect.collidepoint(pos):
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.increase_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.decrease_rect)

        pygame.draw.rect(screen, (0, 0, 0), self.increase_rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), self.decrease_rect, 2)

        plus_text = self.font.render("+", 1, (0, 100, 0))
        plus_text_rect = plus_text.get_rect()
        plus_text_rect.center = (self.x + self.size_x / 2, self.y + self.size_y / 4)
        screen.blit(plus_text, plus_text_rect)

        minus_text = self.font.render("-", 1, (150, 10, 10))
        minus_text_rect = minus_text.get_rect()
        minus_text_rect.center = (self.x + self.size_x / 2, self.y + self.size_y * 3 / 4)
        screen.blit(minus_text, minus_text_rect)

class Text_Box:
    def __init__(self, x, y, size_x, size_y, text):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

        self.rect = pygame.Rect(x, y, size_x, size_y)

        self.text = text

        self.font = pygame.font.SysFont("Bahnschrift", 20)

        self.active = False

    def get_rec(self):
        return self.rect
    
    def get_active(self):
        return self.active

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.active = True
            return True
        else:
            self.active = False
            return False
    
    def write(self, event):
        if self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isdigit():
                if len(self.text) < 10:
                    self.text += event.unicode
    
    def get_value(self):
        return int(self.text)

    def set_value(self, value):
        self.text = str(value)

    def set_size(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.rect = pygame.Rect(self.x, self.y, self.size_x, self.size_y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.size_x, self.size_y)

    def draw(self, screen):
        active_color = (44, 46, 53)
        inactive_color = (0, 0, 0)
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        if self.active:
            color = active_color
        else:
            color = inactive_color

        pygame.draw.rect(screen, color, self.rect, 2)
        text = self.font.render(self.text, 1, color)
        text_rect = text.get_rect()
        text_rect.center = (self.x + self.size_x / 2, self.y + self.size_y / 2)
        screen.blit(text, text_rect)