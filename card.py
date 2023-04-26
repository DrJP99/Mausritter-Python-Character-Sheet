import math
import pygame
from item import *
from condition import *
from snap_area import *
from cursor import grab_hand_cursor




class Card:
    def __init__(self, title = ""):
        self.x = 0
        self.y = 0
        self.title = title
        self.new_title = title

        self.size_x = 102
        self.size_y = 102

        self.dragging = False
        self.can_drag = True

        self.is_snapped = False

        self.blocked = []
        self.blocking = []

        self.type = "generic"
        self.close_rec = None
        self.window_rec = None

        self.allowed_area_x = 590
        self.allowed_area_y = 840

        self.title_font = pygame.font.Font("./fonts/Brokenscript OT Cond Bold.ttf", 13)
        self.class_font = pygame.font.SysFont("Bahnschrift", 12)
        self.star_font = pygame.font.SysFont("Simsun", 12)

        self.max_purse_font = pygame.font.SysFont("Bahnschrift", 15)
        self.purse_font = pygame.font.Font("fonts\CaveatBrush-Regular.ttf", 15)

        self.description_font = pygame.font.SysFont("Bahnschrift", 9, italic=True)
        self.clear_font = pygame.font.SysFont("Bahnschrift", 9)
        self.clear_title_font = pygame.font.SysFont("Bahnschrift", 10, bold=True)

    def __str__(self):
        return f"{self.title}"
        
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title
    
    def set_size_x(self, size_x):
        self.size_x = size_x

    def set_size_y(self, size_y):
        self.size_y = size_y

    def get_size_x(self):
        return self.size_x
    
    def get_size_y(self):
        return self.size_y

    def get_type(self):
        return self.type

    def is_wide(self):
        return self.size_x > self.size_y and self.size_x > 102

    def is_tall(self):
        return self.size_x < self.size_y and self.size_y > 102
    
    def is_large_square(self):
        return self.size_x == self.size_y and self.size_x > 102
    
    def is_very_wide(self):
        return self.size_x > self.size_y and self.size_x > 204

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size_x, self.size_y)

    def check_inside_rect(self, rect, x, y):
        return pygame.Rect.collidepoint(rect, x, y)
    
    def check_inside(self, x, y):
        if self.check_inside_rect(self.get_rect(), x, y):
            for block in self.blocked:
                if self.check_inside_rect(block, x, y):
                    return False
            return True
    
    def title_too_long(self, size_x, font):
        res = ""
        for letter in self.title:
            if font.size(res + letter + "...")[0] < size_x:
                res += letter
            else:
                res += "..."
                break
        return res


    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size_x, self.size_y))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.size_x, self.size_y), 1)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 27), (self.x + self.size_x - 1, self.y + 27))

        offset = 0
        if (self.type == "spell"):
            symbol_text = self.star_font.render("★", True, (0,0,0))
            symbol_rect = symbol_text.get_rect()
            symbol_rect.topleft = (self.x + 5, self.y + 6)
            screen.blit(symbol_text, symbol_rect)
            offset = symbol_rect.width + 2
        
        title = self.title_too_long(self.size_x - 10 - offset, self.title_font)
            
        # if (len(self.title) > 15):
        #     title = self.title[:15] + "..."
        text = self.title_font.render(title, 1, (0, 0, 0))
        rect = pygame.Rect(self.x + 5, self.y + 5, self.size_x - 10, 20)
        rect.update(self.x + 5, self.y + 5, self.size_x - 10, 20)
        screen.blit(text, (self.x + 5 + offset, self.y + 5))

    
    def draw_ui_window(self, screen):
        pause_back = pygame.Surface((screen.get_width(), screen.get_height()))
        pause_back.set_alpha(75)
        pause_back.fill((225, 225, 225))
        screen.blit(pause_back, (0, 0))

        self.window_rec = pygame.Rect(screen.get_width() / 2 - 200, screen.get_height() / 2 - 150, 400, 300)
        pygame.draw.rect(screen, (255, 255, 255), self.window_rec)
        pygame.draw.rect(screen, (0, 0, 0), self.window_rec, 1)

        self.close_rec = pygame.Rect( self.window_rec.x + self.window_rec.width - 35, self.window_rec.y + 10, 25, 25)
        pygame.draw.rect(screen, (255, 0, 0), self.close_rec)
        
        title_font = pygame.font.Font("./fonts/Brokenscript OT Cond Bold.ttf", 25)
        title_text = title_font.render(self.title, 1, (0, 0, 0))
        screen.blit(title_text, (self.window_rec.width / 2 + self.window_rec.x - title_text.get_width() / 2, self.window_rec.y + 10))

        title_rect = title_text.get_rect()
        pygame.draw.line(screen, (0, 0, 0), (self.window_rec.x, self.window_rec.y + title_rect.y + title_rect.height + 15), (self.window_rec.x + self.window_rec.width - 1, self.window_rec.y + title_rect.y + title_rect.height + 15), 1)

        offset = 55
        original_offset = offset
        font = pygame.font.SysFont("Bahnschrift", 14)

        type_text = font.render(f"Type: {self.type.title()}", True, (0, 0, 0))
        type_rect = type_text.get_rect()
        screen.blit(type_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += type_rect.height + 5

        return offset, original_offset

    def get_close_rec(self):
        return self.close_rec

    def close_ui_window(self):
        pygame.display.update()
        self.close_rec = None
        self.window_rec = None

    def snap_to(self, snap_area):
        if (not snap_area.get_is_grit()):
            self.x = snap_area.get_x()
            self.y = snap_area.get_y()
            self.is_snapped = True
            self.snapped_to = snap_area
        elif (snap_area.get_is_grit() and self.type == "condition"):
            self.is_snapped = True
            self.snapped_to = snap_area
            self.y = snap_area.get_y()
            if (self.x < snap_area.get_x()):
                self.x = snap_area.get_x()
            elif (self.x > snap_area.get_x() + snap_area.get_size_x() - self.size_x):
                self.x = snap_area.get_x() + snap_area.get_size_x() - self.size_x
    
    def get_snap_area(self):
        return self.snapped_to

    def get_is_snapped(self):
        return self.is_snapped
    
    def drag(self):
        if (pygame.mouse.get_pressed()[0] and not self.check_inside(*pygame.mouse.get_pos())):
            self.can_drag = False
        
        if (not pygame.mouse.get_pressed()[0] and not self.can_drag):
            self.can_drag = True

        if (pygame.mouse.get_pressed()[0] and not self.dragging and self.can_drag):
            if (self.check_inside(*pygame.mouse.get_pos())):
                self.dragging = True
                self.start_d_x = pygame.mouse.get_pos()[0] - self.x
                self.start_d_y = pygame.mouse.get_pos()[1] - self.y
        
        if (not pygame.mouse.get_pressed()[0]):
            self.dragging = False


        if (self.dragging):
                self.x = pygame.mouse.get_pos()[0] - self.start_d_x
                self.y = pygame.mouse.get_pos()[1] - self.start_d_y

                if self.x < 0:
                    self.x = 0
                if self.y < 0:  
                    self.y = 0
                if self.x + self.size_x > self.allowed_area_x:
                    self.x = self.allowed_area_x - self.size_x
                if self.y + self.size_y > self.allowed_area_y:
                    self.y = self.allowed_area_y - self.size_y
                # pygame.mouse.set_cursor((16, 16), (0, 0), *grab_hand_cursor)
                # print(f"x: {self.x}, y: {self.y}")

    
    def gets_dragged(self):
        return self.dragging
    
    def remove_snap(self):
        self.is_snapped = False
        self.snapped_to = None
    
    def add_blocked(self, rect = pygame.Rect(0, 0, 0, 0)):
        # new_x = rect.x
        # new_y = rect.y
        # new_width = rect.width
        # new_height = rect.height
        # if(rect.x + rect.width > self.x + self.size_x):
        #     new_width = self.x + self.size_x - rect.x
        # if(rect.y + rect.height > self.y + self.size_y):
        #     new_height = self.y + self.size_y - rect.y
        # if(rect.x < self.x):
        #     new_x = self.x
        # if(rect.y < self.y):
        #     new_y = self.y
        new_rect = pygame.Rect.clip(self.get_rect(), rect)
        # print(f"Adding blocked area: {new_x}, {new_y}, {new_width + new_x}, {new_height + new_y}")
        self.blocked.append(new_rect)
    
    def remove_blocked(self, rect = pygame.Rect(0, 0, 0, 0)):
        if(rect.x + rect.width > self.x + self.size_x):
            rect.width = self.x + self.size_x - rect.x
        if(rect.y + rect.height > self.y + self.size_y):
            rect.height = self.y + self.size_y - rect.y
        if(rect.x < self.x):
            rect.x = self.x
        if(rect.y < self.y):
            rect.y = self.y
        self.blocked.remove(rect)
    
    def clear_blocked(self):
        self.blocked = []

    def block(self, card):
        self.blocking.append(card)
    
    def remove_blocking(self, card):
        print(f"removing {card} from {self.get_title()}")
        self.blocking.remove(card)
    
    def clear_blocking(self):
        self.blocking = []
    
    def is_blocking(self):
        return self.blocking

    def delete(self):
        del self


class Item_Card(Card):
    def __init__(self, item = Item()):
        super().__init__(item.get_name())
        self.item = item
        self.max_durability = item.get_max_durability()
        self.durability = item.get_durability()

        self.size_x *= self.item.get_size_x()
        self.size_y *= self.item.get_size_y()

        self.type = "item"

        self.durability_rect = pygame.Rect(self.x, self.y + 27, 50, math.ceil(self.max_durability / 3) * 15 + 5)
        if (self.max_durability == 0):
            self.durability_rect = pygame.Rect(0, 0, 0, 0)

    def set_item(self, item):
        self.item = item
    
    def get_item(self):
        return self.item
    
    def check_inside(self, x, y):
        if (self.durability_rect.collidepoint(x, y)):
            return False
        else:
            return super().check_inside(x, y)

    def drag(self):
        super().drag()
        self.durability_rect.x = self.x
        self.durability_rect.y = self.y + 27

    def set_max_durability(self, max_durability):
        self.max_durability = max_durability
        self.weapon.set_max_durability(max_durability)

    def set_durability(self, durability):
        self.durability = durability
        self.weapon.set_durability(durability)
    
    def get_max_durability(self):
        return self.max_durability
    
    def get_durability(self):
        return self.durability
    
    def increase_durability(self, n = 1):
        if self.durability < self.max_durability:
            self.item.increase_durability(n)
            self.durability += n
    
    def fix(self):
        self.item.fix()
        self.durability = 0

    def click_durability(self, pos):
        for block in self.blocked:
            if (block.collidepoint(pos)):
                return False
        if (self.durability_rect.collidepoint(pos)):
            # uses = math.floor((pos[0] - self.x - 10) / 15) + (math.floor((pos[1] - self.y - 40) / 15) * 3) + 1
            # print(f"Uses: {uses}")
            # if uses <= self.durability:
            #     self.durability = uses
            if (self.durability < self.max_durability):
                self.durability += 1
                self.item.increase_durability()
                # print(f"Durability: {self.durability}")
                return True
        return False

    def right_click_durability(self, pos):
        for block in self.blocked:
            if (block.collidepoint(pos)):
                return False
        if (self.durability_rect.collidepoint(pos)):
            if (self.durability > 0):
                self.durability -= 1
                self.item.decrease_durability()
                # print(f"Durability: {self.durability}")
                return True
        return False

    def draw(self, screen):
        super().draw(screen)
        # font = pygame.font.SysFont("Arial", 20)
        j = 0
        for i in range(self.max_durability):
            if (i < self.durability):
                color = (10, 10, 10)
            else:
                color = (250, 250, 250)
            r = math.floor(i / 3)
            if i % 3 == 0:
                j = 0
            pygame.draw.circle(screen, color, (self.x + 10 + (j * 15), self.y + 37 + (r * 15)), 5)
            pygame.draw.circle(screen, (0, 0, 0), ((self.x + 10 + (j * 15)), (self.y + 37 + (r * 15))), 5, 1)
            j += 1

        if (self.max_durability != 0):
            pygame.draw.rect(screen, (0, 0, 0), self.durability_rect, 1)

    def draw_ui_window(self, screen):
        offset, original_offset = super().draw_ui_window(screen)
        font = pygame.font.SysFont("Bahnschrift", 14)

        max_uses_text = font.render(f"Max uses: {self.max_durability}", True, (0, 0, 0))
        max_uses_rect = max_uses_text.get_rect()
        screen.blit(max_uses_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += max_uses_rect.height + 5

        uses_text = font.render(f"Current uses: {self.durability}", True, (0, 0, 0))
        uses_rect = uses_text.get_rect()
        screen.blit(uses_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += uses_rect.height + 5

        cost_text = font.render(f"Cost: {self.item.get_cost()}p", True, (0, 0, 0))
        cost_rect = cost_text.get_rect()
        screen.blit(cost_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += cost_rect.height + 5

        return offset, original_offset

class Weapon_Card(Item_Card):
    def __init__(self, weapon = Weapon()):
        super().__init__(weapon)
        self.weapon = weapon
        self.weapon_class = weapon.get_weapon_class().value
        if (type(weapon.get_hitdie()) == list):
            self.hitdie = f"d{weapon.get_hitdie()[0].value}/d{weapon.get_hitdie()[1].value}"
        elif (weapon.get_hitdie() == None):
            self.hitdie = f""
        else:
            self.hitdie = f"d{weapon.get_hitdie().value}"
        
        self.type = "weapon"

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_weapon(self):
        return self.weapon
    
    def set_weapon_class(self, weapon_class):
        self.weapon_class = weapon_class

    def set_hitdie(self, hitdie):
        self.hitdie = hitdie

    def get_weapon_class(self):
        return self.weapon_class
    
    def get_hitdie(self):
        return self.hitdie
    
    def draw(self, screen):
        super().draw(screen)
        hitdice_string = f"{self.hitdie}"
        text = self.class_font.render(hitdice_string, 1, (0, 0, 0))
        text_h = self.class_font.size(hitdice_string)[1]
        screen.blit(text, (self.x + 5, self.y + self.size_y - 5 - text_h * 2))

        class_string = f"{self.weapon_class}"
        text = self.class_font.render(class_string, 1, (0, 0, 0))
        text_h = self.class_font.size(class_string)[1]
        screen.blit(text, (self.x + 5, self.y + self.size_y - 5 - text_h))
    
    def draw_ui_window(self, screen):
        offset, original_offset = super().draw_ui_window(screen)
        font = pygame.font.SysFont("Bahnschrift", 14)

        weapon_class_text = font.render(f"Weapon class: {self.weapon_class.title()}", True, (0, 0, 0))
        weapon_class_rect = weapon_class_text.get_rect()
        screen.blit(weapon_class_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += weapon_class_rect.height + 5

        match self.weapon_class.title():
            case "Light":
                hand = "Main paw/off paw"
            case "Medium":
                hand = "Main paw/Both paws"
            case "Heavy":
                hand = "Both paws"
            case "Light Ranged":
                hand = "Main paw"
            case "Heavy Ranged":
                hand = "Both paws"
            case "Ammunition":
                hand = "Body slot"
        
        hand_text = font.render(f"In: {hand}", True, (0, 0, 0))
        hand_rect = hand_text.get_rect()
        screen.blit(hand_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += hand_rect.height + 5

        offset = original_offset

        damage_text = font.render(f"Damage: {self.hitdie} damage", True, (0, 0, 0))
        damage_rect = damage_text.get_rect()
        screen.blit(damage_text, (self.window_rec.x + self.window_rec.width / 2 + 10, self.window_rec.y + offset))
        offset += damage_rect.height + 5

        return offset, original_offset


class Magic_Weapon_Card(Weapon_Card):
    def __init__(self, magic_weapon = Magic_Weapon()):
        super().__init__(magic_weapon)
        self.weapon_ability = magic_weapon.get_ability()
        self.type = "magic_weapon"
    
    def set_weapon_ability(self, weapon_ability):
        self.weapon_ability = weapon_ability

    def get_weapon_ability(self):
        return self.weapon_ability
    
    def draw(self, screen):
        super().draw(screen)

class Armor_Card(Item_Card):
    def __init__(self, armor = Armor()):
        super().__init__(armor)
        self.armor = armor
        self.armor_class = armor.get_armor_class().value
        self.defence = armor.get_defence()
        self.type = "armor"

    def set_armor(self, armor):
        self.armor = armor

    def get_armor(self):
        return self.armor
    
    def set_armor_class(self, armor_class):
        self.armor_class = armor_class

    def set_defence(self, defence):
        self.defence = defence

    def get_armor_class(self):
        return self.armor_class
    
    def get_defence(self):
        return self.defence
    
    def draw(self, screen):
        super().draw(screen)
        armor_class_string = f"{self.armor_class}"
        text = self.class_font.render(armor_class_string, 1, (0, 0, 0))
        text_h = self.class_font.size(armor_class_string)[1]
        screen.blit(text, (self.x + 5, self.y + self.size_y - 5 - text_h))

        armor_protection = f"Protection: {self.defence}"
        text = self.class_font.render(armor_protection, 1, (0, 0, 0))
        text_h = self.class_font.size(armor_protection)[1]
        screen.blit(text, (self.x + 5, self.y + self.size_y - 5 - text_h * 2))
    
    def draw_ui_window(self, screen):
        offset, original_offset = super().draw_ui_window(screen)
        font = pygame.font.SysFont("Bahnschrift", 14)

        class_text = font.render(f"Armor class: {self.armor_class}", True, (0, 0, 0))
        class_rect = class_text.get_rect()
        screen.blit(class_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += class_rect.height + 5

        protection_text = font.render(f"Protection: {self.defence}", True, (0, 0, 0))
        protection_rect = protection_text.get_rect()
        screen.blit(protection_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += protection_rect.height + 5

        offset = original_offset

        match (self.armor_class.title()):
            case "Light":
                hand = "Off paw and a body slot"
            case "Heavy":
                hand = "Two body slots"

        hand_text = font.render(f"In: {hand}", True, (0, 0, 0))
        hand_rect = hand_text.get_rect()
        screen.blit(hand_text, (self.window_rec.x + self.window_rec.width / 2 + 10, self.window_rec.y + offset))



class Purse_Card(Item_Card):
    def __init__(self, purse = Purse()):
        super().__init__(purse)
        self.purse = purse
        self.curr_pip = purse.get_pip()
        self.max_pip = purse.get_max_pip()
        self.type = "purse"

    def set_purse(self, purse):
        self.purse = purse

    def get_purse(self):
        return self.purse

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.rect(screen, (0, 0, 0), (self.x + 5, self.y + self.size_y - 33, self.size_x - 10, 28), 1)

        max_pip_str = f"/ {self.max_pip}"
        text = self.max_purse_font.render(max_pip_str, 1, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.bottomright = (self.x + self.size_x - 10, self.y + self.size_y - 10)
        screen.blit(text, text_rect)

        curr_text = self.purse_font.render(f"{self.curr_pip}", 1, (0, 0, 0))
        curr_text_rect = curr_text.get_rect()
        curr_text_rect.bottomright = (self.x + self.size_x - 13 - text_rect.width, self.y + self.size_y - 9)
        screen.blit(curr_text, curr_text_rect)
    
    def draw_ui_window(self, screen):
        offset, original_offset = super().draw_ui_window(screen)
        font = pygame.font.SysFont("Bahnschrift", 14)

        max_pip_text = font.render(f"Max pip: {self.max_pip}", True, (0, 0, 0))
        max_pip_rect = max_pip_text.get_rect()
        screen.blit(max_pip_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += max_pip_rect.height + 5
    
class Spell_Card(Item_Card):
    def __init__(self, spell = Spell()):
        super().__init__(spell)
        self.spell = spell
        self.type = "spell"
    
    def set_spell(self, spell):
        self.spell = spell
    
    def get_spell(self):
        return self.spell
    
    def draw(self, screen):
        super().draw(screen)

    def draw_ui_window(self, screen):
        offset, original_offset = super().draw_ui_window(screen)
        font = pygame.font.SysFont("Bahnschrift", 14)

        offset = original_offset

        effect_text = f"Effect: {self.spell.get_effect()}"
        effect_height = text_wrap(effect_text, font, (0,0,0), self.window_rec.x + 10 + self.window_rec.width / 2, self.window_rec.y + offset, screen, self.window_rec.width / 2 - 20)
        # screen.blit(effect_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += effect_height + 5

        recharge_text = f"Recharge: {self.spell.get_recharge()}"
        recharge_height = text_wrap(recharge_text, font, (0,0,0), self.window_rec.x + 10 + self.window_rec.width / 2, self.window_rec.y + offset, screen, self.window_rec.width / 2 - 20)
        # screen.blit(recharge_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += recharge_height + 5

        if (offset > self.window_rec.height - 50):
            print("true")
            self.window_rec.height = offset + 50

class Condition_Card(Card):
    def __init__(self, condition = Condition()):
        super().__init__(condition.get_name())
        self.condition = condition
        self.description = condition.get_description()
        self.clear = condition.get_clear()
        self.type = "condition"

        print (self.description)

    def set_condition(self, condition):
        self.condition = condition

    def get_condition(self):
        return self.condition
    
    def set_description(self, description):
        self.description = description

    def set_clear(self, clear):
        self.clear = clear

    def get_description(self):
        return self.description
    
    def get_clear(self):
        return self.clear
    
    def draw(self, screen):
        super().draw(screen)
        description_string = f"{self.description}"
        # text = class_font.render(description_string, 1, (0, 0, 0))
        # text_h = class_font.size(description_string)[1]
        # screen.blit(text, (self.x + 5, self.y + self.size_y - 5 - text_h))
        text_wrap(description_string, self.description_font, (0, 0, 0), self.x + 5, self.y + 32, screen, self.size_x - 10)

        clear_string = f"{self.clear}"
        text = self.clear_font.render(clear_string, 1, (0, 0, 0))
        text_h = self.clear_font.size(clear_string)[1]
        text_rect = text.get_rect()
        text_rect.bottomleft = (self.x + 5, self.y + self.size_y - 5)
        screen.blit(text, text_rect)

        clear_str = "Clear:"
        clear_text = self.clear_title_font.render(clear_str, 1, (0, 0, 0))
        screen.blit(clear_text, (self.x + 5, self.y + self.size_y - 5 - 2 * text_rect.height))

    def draw_ui_window(self, screen):
        offset, original_offset = super().draw_ui_window(screen)
        font = pygame.font.SysFont("Bahnschrift", 14)


        description_text = f"Description: {self.description}"
        description_height = text_wrap(description_text, font, (0,0,0), self.window_rec.x + 10, self.window_rec.y + offset, screen, self.window_rec.width - 20)
        # screen.blit(description_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += description_height + 5

        clear_text = f"Clear: {self.clear}"
        clear_height = text_wrap(clear_text, font, (0,0,0), self.window_rec.x + 10, self.window_rec.y + offset, screen, self.window_rec.width - 20)
        # screen.blit(clear_text, (self.window_rec.x + 10, self.window_rec.y + offset))
        offset += clear_height + 5




def text_wrap(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (x, ty))

        y_offset += fh
    
    return y_offset