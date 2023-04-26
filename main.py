import random
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from character import *
from condition import *
from item import *
from my_enums import *
from card import *
from snap_area import Snap_Area as sa
from snap_area import Grit_Area as ga
from snap_area import Delete_Area as da
from toolbar import *
from button import *

from tkinter import *
import json
import pygame
from pygame.locals import *


global my_char, root, snap_areas, all_cards

all_items = json.load(open("resources/all_items.json"))

ITEM_TYPES = ["Item", "Condition", "Weapon", "Magic Weapon", "Armor", "Purse", "Spell"]

def list_of_keys(data): 
    list_keys = []
    for key in data.keys(): 
        list_keys.append(key)
    return sorted(list_keys)

ITEMS = list_of_keys(all_items["item"])
CONDITIONS = list_of_keys(all_items["condition"])
WEAPONS = list_of_keys(all_items["weapon"])
# MAGIC_WEAPONS = list_of_keys(all_items["magic_weapon"])
ARMORS = list_of_keys(all_items["armor"])
PURSES = list_of_keys(all_items["purse"])
SPELLS = list_of_keys(all_items["spell"])

MOUSE_NAMES = ["Ada", "Agate", "Agnes", "Aloe", "April", "Azalea", "Bay", "Belladonna", "Blossom", "Brie",
               "Brynn", "Cherry", "Claire", "Crocus", "Dahlia", "Daisy", "Else", "Emerald", "Erin", "Grace",
               "Gwendoline", "Hazel", "Heather", "Hette", "Holly", "Hyacinth", "Iris", "Juniper", "Lavender", "Lily",
               "Magnolia", "Marigold", "Marjoram", "Myrtle", "Odette", "Olive", "Opal", "Pearl", "Pepper", "Poppy",
               "Rosemary", "Rue", "Saffron", "Sandy", "Sassafras", "Shale", "Susan", "Thistle", "Violet", "Willow",
               "Alder", "Ambrose", "Anise", "Anotto", "August", "Avens", "Basil", "Beryl", "Birch", "Boldo",
               "Bill", "Burdock", "Butter", "Cassia", "Chicory", "Clive", "Colby", "Dill", "Dock", "Eared",
               "Edmund", "Elmer", "Ernest", "Fennel", "Festus", "Francis", "Gil", "Hawthron", "Heath", "Horatio",
               "Jack", "Jasper", "Konrad", "Larkspur", "Laurel", "Lorenz", "Mace", "Oliver", "Orin", "Reepcheep",
               "Rowan", "Simon", "Sorrel", "Stilton", "Tarragon", "Warren", "Wattle", "Whitacre", "Wormwood", "Yarrow"]
MOUSE_MATRINAMES = ["Baiter", "Black", "Buckthorne", "Burley", "Butterball", "Catreizen", "Danger", "Deerider", "Grant", "Halva",
                    "Maker", "Pipp", "Seedfall", "Snow", "Summerholme", "Thorne", "Tunneler", "White", "Winterholme", "Witter"]

def get_birthsign(n):
    print("Your disposition is", end = " ")
    match(n):
        case 1:
            print("Brave/Reckless")
            return "star", "Brave/Reckless"
        case 2:
            print("Industrious/Unimaginative")
            return "wheel", "Industrious/Unimaginative"
        case 3:
            print("Inquisitive/Stubborn")
            return "acorn", "Inquisitive/Stubborn"
        case 4:
            print("Generous/Wrathful")
            return "storm", "Generous/Wrathful"
        case 5:
            print("Wise/Mysterious")
            return "moon", "Wise/Mysterious"
        case 6:
            print("Nurturing/Worrying")
            return "mother", "Nurturing/Worrying"

def get_coat(n, m):
    match(n):
        case 1:
            color = "Chocolate"
        case 2:
            color = "Black"
        case 3:
            color = "White"
        case 4:
            color = "Tan"
        case 5:
            color = "Grey"
        case 6:
            color = "Blue"
    match(m):
        case 1:
            pattern = "Solid"
        case 2:
            pattern = "Brindle"
        case 3:
            pattern = "Patchy"
        case 4:
            pattern = "Banded"
        case 5: 
            pattern = "Marbled"
        case 6:
            pattern = "Flecked"
    
    coat = color + " " + pattern
    print("Your coat is ", coat)
    return coat

def get_look(n):
    match(n):
        case 11:
            look = "Scarred body"
        case 12:
            look = "Corpulent body"
        case 13:
            look = "Skeletal body"
        case 14:
            look = "Willowy body"
        case 15:
            look = "Tiny body"
        case 16:
            look = "Massive body"
        case 21:
            look = "War paint"
        case 22:
            look = "Foreign clothes"
        case 23:
            look = "Elegant clothes"
        case 24:
            look = "Patched clothes"
        case 25:
            look = "Fashionable clothes"
        case 26:
            look = "Unwashed clothes"
        case 31:
            look = "Missing ear"
        case 32:
            look = "Lumpy face"
        case 33:
            look = "Beautiful face"
        case 34:
            look = "Round face"
        case 35:
            look = "Delicate face"
        case 36:
            look = "Elongated face"
        case 41:
            look = "Groomed fur"
        case 42:
            look = "Dreadlocks"
        case 43:
            look = "Dyed fur"
        case 44:
            look = "Shaved fur"
        case 45:
            look = "Frizzy fur"
        case 46:
            look = "Silky fur"
        case 51:
            look = "Night black eyes"
        case 52:
            look = "Eye patch"
        case 53:
            look = "Blood red eyes"
        case 54:
            look = "Wise eyes"
        case 55:
            look = "Sharp eyes"
        case 56:
            look = "Luminous eyes"
        case 61:
            look = "Cropped tail"
        case 62:
            look = "Whip-like tail"
        case 63:
            look = "Tuffed tail"
        case 64:
            look = "Stubby tail"
        case 65:
            look = "Prehensile tail"
        case 66:
            look = "Curly tail"
    
    print("Your look is ", look)
    return look

def get_background(hp, pips):
    match(hp):
        case 1:
            match(pips):
                case 1:
                    background = "Test subject"
                    item1 = generate_item("Magic Missile")
                    item2 = generate_item("Heavy Armor")
                case 2:
                    background = "Kitchen forager"
                    item1 = generate_item("Light Armor")
                    item2 = generate_item("Cookpots")
                case 3:
                    background = "Cage dweller"
                    item1 = generate_item("Be Understood")
                    item2 = generate_item("Bottle of milk", True)
                case 4:
                    background = "Hedge witch"
                    item1 = generate_item("Heal")
                    item2 = generate_item("Incense stick", True)
                case 5:
                    background = "Leatherworker"
                    item1 = generate_item("Light Armor")
                    item2 = generate_item("Leatherworking tools", True)
                case 6:
                    background = "Street tough"
                    item1 = generate_item("Dagger")
                    item2 = generate_item("Flask of coffee", True)
        case 2:
            match(pips):
                case 1:
                    background = "Medicant priest"
                    item1 = generate_item("Restore")
                    item2 = generate_item("Holy symbol", True)
                case 2:
                    background = "Beetleherd"
                    item1 = "Hireling: Loyal Beetle"
                    item2 = generate_item("Pole")
                case 3:
                    background = "Ale brewer"
                    item1 = "Hireling: Drunken torchbearer"
                    item2 = generate_item("Small barrel of ale", True)
                case 4:
                    background = "Fishermouse"
                    item1 = generate_item("Net")
                    item2 = generate_item("Needle")
                case 5:
                    background = "Blacksmith"
                    item1 = Weapon("Hammer", Weapon_Class.medium)
                    item2 = generate_item("Metal file")
                case 6:
                    background = "Wireworker"
                    item1 = generate_item("Wire", True)
                    item2 = generate_item("Electric lantern")
        case 3:
            match(pips):
                case 1:
                    background = "Woodcutter"
                    item1 = generate_item("Axe")
                    item2 = generate_item("Twine", True)
                case 2:
                    background = "Bat cultist"
                    item1 = generate_item("Darkness")
                    item2 = generate_item("Bag of bat teeth", True)
                case 3:
                    background = "Tin miner"
                    item1 = Weapon("Pickaxe", Weapon_Class.medium)
                    item2 = generate_item("Lantern")
                case 4:
                    background = "Trash collector"
                    item1 = Weapon("Trashhook", Weapon_Class.heavy)
                    item2 = generate_item("Mirror", True)
                case 5:
                    background = "Wall rover"
                    item1 = generate_item("Fishhook")
                    item2 = generate_item("Thread")
                case 6:
                    background = "Merchant"
                    item1 = "Hireling: Pack rat"
                    item2 = Item("IOU from Noblemouse", cost=20)
        case 4:
            match(pips):
                case 1:
                    background = "Raft crew"
                    item1 = Weapon("Hammer", Weapon_Class.medium)
                    item2 = generate_item("Wooden spikes")
                case 2:
                    background = "Worm wrangler"
                    item1 = generate_item("Pole")
                    item2 = generate_item("Soap")
                case 3:
                    background = "Sparrow rider"
                    item1 = generate_item("Fishhook")
                    item2 = generate_item("Goggles", True)
                case 4:
                    background = "Sewer guide"
                    item1 = generate_item("Metal file")
                    item2 = generate_item("Thread")
                case 5:
                    background = "Prison guard"
                    item1 = generate_item("Chain", True)
                    item2 = generate_item("Spear")
                case 6:
                    background = "Fungus farmer"
                    item1 = generate_item("Rations")
                    item2 = generate_item("Spore mask", True)
        case 5:
            match(pips):
                case 1:
                    background = "Dam builder"
                    item1 = generate_item("Shovel", True)
                    item2 = generate_item("Wooden spikes")
                case 2:
                    background = "Cartographer"
                    item1 = generate_item("Quill & ink", True)
                    item2 = generate_item("Compass", True)
                case 3:
                    background = "Trap thief"
                    item1 = generate_item("Block of cheese", True)
                    item2 = generate_item("Glue")
                case 4:
                    background = "Vagabond"
                    item1 = generate_item("Tent")
                    item2 = generate_item("Dubious treasure map", True)
                case 5:
                    background = "Grain farmer"
                    item1 = generate_item("Spear")
                    item2 = generate_item("Whistle")
                case 6:
                    background = "Message runner"
                    item1 = generate_item("Bedroll", True)
                    item2 = generate_item("Sealed documents", True)
        case 6:
            match(pips):
                case 1:
                    background = "Troubadour"
                    item1 = generate_item("Musical instrument")
                    item2 = generate_item("Disguise kit", True)
                case 2:
                    background = "Gambler"
                    item1 = generate_item("Set of loaded dice")
                    item2 = generate_item("Mirror")
                case 3:
                    background = "Sap tapper"
                    item1 = generate_item("Bucket")
                    item2 = generate_item("Wooden spikes")
                case 4:
                    background = "Bee keeper"
                    item1 = generate_item("Jar of honey", True)
                    item2 = generate_item("Net")
                case 5:
                    background = "Librarian"
                    item1 = generate_item("Scrap of obscure book", True)
                    item2 = generate_item("Quill & ink", True)
                case 6:
                    background = "Pauper noblemouse"
                    item1 = generate_item("Felt hat", True)
                    item2 = generate_item("Perfume")
    
    print(f"Your background is {background}")
    return background, item1, item2

def generate_character():
    print("Let\'s generate a new Character!")
    name = input("What is your mouse\'s name? ")

    print("For the following attributes, roll 3d6 and add the highest two numbers together. ")
    str = int(input("What is your mouse\'s strength? "))
    dex = int(input("What is your mouse\'s dexterity? "))
    wil = int(input("What is your mouse\'s will and charisma? "))

    hp = input("Now roll a d6 to determine your HP. ")
    pip = input("Now roll a d6 to determine your starting pips. ")

    print("Your background is determined by your HP and Pips.")
    background, item1, item2 = get_background(int(hp), int(pip))
    print("Your background is ", background)
    
    print("Your first item is ", item1)
    print("Your second item is ", item2)

    print("Every adventuring mouse has some starting equipment.")
    print("You get Torches, Rations, the two items from your background and a weapon of your choice.")
    weapon = input("Choose between Needle, Dagger, Axe, Sword, Mace, Sling, Warhammer, Spear, Hookarm and Bow")

    roll = input("Now roll a d6 to determine your birthsign. ")
    birthsign = get_birthsign(int(roll))
    print("Your birthsign is ", birthsign)

    print("Now roll 2d6 to determine your coat color and pattern. ")
    roll1 = input("First roll: ")
    roll2 = input("Second roll: ")
    coat = get_coat(int(roll1), int(roll2))

    print("Now roll a d66 to determine your mouse\'s look. ")
    print("Tip: d66 means d6 * 10 + d6. ")
    roll = input("Roll: ")
    look = get_look(int(roll))

    mychar = Character(name=name, background=background, str=str, dex=dex, wil=wil, hp=hp, pips=pip, birthsign=birthsign, coat=coat, look=look)
    mychar.inventory.add_item(generate_item("Torches"), "back", 0, 2)
    mychar.inventory.add_item(generate_item("Rations"), "back", 1, 2)
    mychar.inventory.add_item(generate_item(weapon), "main", 0, 0)
    
    return mychar

def generate_item(name, custom = False):
    if not custom:
        match(name):
            case "Improvised Weapon":
                item = Weapon(name, Weapon_Class.improvised)
            case "Stones":
                item = Weapon(name, Weapon_Class.ammunition)
            case "Needle":
                item = Weapon(name, Weapon_Class.light)
            case "Dagger":
                item = Weapon(name, Weapon_Class.light)
            case "Arrows":
                item = Weapon(name, Weapon_Class.ammunition)
            case "Axe":
                item = Weapon(name, Weapon_Class.medium)
            case "Sword":
                item = Weapon(name, Weapon_Class.medium)
            case "Mace":
                item = Weapon(name, Weapon_Class.medium)
            case "Sling":
                item = Weapon(name, Weapon_Class.light_ranged)
            case "Warhammer":
                item = Weapon(name, Weapon_Class.heavy)
            case "Spear":
                item = Weapon(name, Weapon_Class.heavy)
            case "Hookarm":
                item = Weapon(name, Weapon_Class.heavy)
            case "Bow":
                item = Weapon(name, Weapon_Class.heavy_ranged)
            case "Heavy Armor":
                item = Armor(name, Armor_Class.heavy)
            case "Light Armor":
                item = Armor(name, Armor_Class.light)
            case "Torches":
                item = Item(name, cost=10)
            case "Lantern":
                item = Item(name, cost=50)
            case "Electric Lantern":
                item = Item(name, cost=200, max_durability=6)
            case "Pin Purse":
                item = Purse()
            case "Rations":
                item = Item(name, cost=5)
            case "Fireball":
                item = Spell(
                    name, 
                    "Shoot a fireball up to 24\". Deal [SUM] + [DICE] damage to all creatures within 6\".",
                    "Burn in the heart of a raging fire for three days and nights.")
            case "Heal":
                item = Spell(
                    name,
                    "Heal [SUM] STR damage and remouved the injured Condition from a creature.",
                    "Cut self for d6 STR damage, sprinkle the spell with the blood.")
            case "Magic Missile":
                item = Spell(
                    name,
                    "Deal [SUM] + [DICE] damage to a creature within sight.",
                    "Drop from a height of at least 30ft. Touch the spell within one Turn.")
            case "Fear":
                item = Spell(
                    name,
                    "Give the Frightened Condition to [DICE] creatures.",
                    "Receive the Frightened Condition from a hostile creature while carrying the spell.")
            case "Darkness":
                item = Spell(
                    name,
                    "Create a [SUM] x 2\" diameter sphere of pure darkness for [DICE] Turns.",
                    "Leave uncovered in a lightless place for three days.")
            case "Restore":
                item = Spell(
                    name,
                    "Remove Exhausted or Frightened Condition from [DICE] + 1 creatures.",
                    "Bury in a peaceful field or riverbank for three days.")
            case "Be Understood":
                item = Spell(
                    name,
                    "Make your meaning clear to [DICE] creatures of another species for [DICE] Turns.",
                    "Give away freely to a creature of another species.")
            case "Ghost Beetle":
                item = Spell(
                    name,
                    "Create an illusory beetle that can carry 6 inventory slots for [DICE] x 6 Turns.",
                    "Bury in a beetle graveyard for three nights.")
            case "Light":
                item = Spell(
                    name,
                    "Force [DICE] creatures to make a WIL save or become stunned. Alternatively, create light as bright as a torch for [SUM] turns.",
                    "Catch in the first light of sunrise and the last light of sunset for three days.")
            case "Invisible Ring":
                item = Spell(
                    name,
                    "Creates [DICE] x 6\" ring of force. It is invisible and immovable. Last [DICE] Turns.",
                    "Build an iron ring the same size as last cast. Pass the spell through it. Dissolces the ring.")
            case "Knock":
                item = Spell(
                    name,
                    "Open a door or container, as if a Save were made with STR score of 10 + [DICE] x 4.",
                    "Put in a locked box, inside a locked box, inside a locked box. Leave for three days.")
            case "Grease":
                item = Spell(
                    name,
                    "Cover [DICE] x 6\" area in slippery, flamable grease. Creatures in the area must make a DEX save or fall prone.",
                    "Rub all over in animal fat. Leave until it putrefies.")
            case "Grow":
                item = Spell(
                    name,
                    "Grow a creature to [DICE] + 1 times its original size for 1 turn.",
                    "Leave in the highest branches of a tall tree for three days.")
            case "Invisibility":
                item = Spell(
                    name,
                    "Make a creature invisible for [DICE] Turns. Any movement reduces duration by 1 Turn.",
                    "Go a day without opening your eyes once, while holding the spell.")
            case "Catnip":
                item = Spell(
                    name,
                    "Turn object into an irresistable lure for cats. Lasts [DICE] Turns.",
                    "Give a cat a gift it truly desires.")
            
            case "Bedroll":
                item = Item(name, cost=10)
            case "Bellows":
                item = Item(name, cost=10)
            case "Blank Book":
                item = Item(name, cost=300)
            case "Reading Book":
                item = Item(name, cost=600)
            case "Bottle":
                item = Item(name, cost=1)
            case "Bucket":
                item = Item(name, cost=5)
            case "Caltrops":
                item = Item(name, cost=10)
            case "Chalk":
                item = Item(name, cost=1)
            case "Chisel":
                item = Item(name, cost=5)
            case "Cookpots":
                item = Item(name, cost=10)
            case "Crowbar":
                item = Item(name, cost=10)
            case "Drill":
                item = Item(name, cost=10)
            case "Glue":
                item = Item(name, cost=5)
            case "Grease":
                item = Item(name, cost=5)
            case "Hammer":
                item = Item(name, cost=10)
            case "Horn":
                item = Item(name, cost=10)
            case "Hourglass":
                item = Item(name, cost=300)
            case "Lockpicks":
                item = Item(name, cost=100)
            case "Metal file":
                item = Item(name, cost=5)
            case "Mirror":
                item = Item(name, cost=200)
            case "Musical instrument":
                item = Item(name, cost=200)
            case "Net":
                item = Item(name, cost=10)
            case "Padlock and key (small)":
                item = Item(name, cost=20)
            case "Perfume":
                item = Item(name, cost=50)
            case "Pick":
                item = Item(name, cost=50)
            case "Set of loaded dice":
                item = Item(name, cost=5)
            case "Shovel":
                item = Item(name, cost=10)
            case "Tent":
                item = Item(name, cost=80)
            case "Waterskin":
                item = Item(name, cost=5)
            case "Whistle":
                item = Item(name, cost=5)
            case "Wooden pole":
                item = Item(name, cost=1)
            case "Wooden spikes":
                item = Item(name, cost=1)

            case "Fishing hook":
                item = Item(name, cost=20)
            case "Incense stick":
                item = Item(name, cost=20)
            case "Lens":
                item = Item(name, cost=200)
            case "Necklace chain":
                item = Item(name, cost=40)
            case "Needle":
                item = Item(name, cost=20)
            case "Matches":
                item = Item(name, cost=20)
            case "Padlock and key (large)":
                item = Item(name, cost=100)
            case "Twine":
                item = Item(name, cost=40)
            case "Soap":
                item = Item(name, cost=10)
            case "Thread":
                item = Item(name, cost=20)
            case "Mouse trap":
                item = Item(name, cost=100)
            case "Poison":
                item = Item(name, cost=100)
            
            case "Oil":
                item = Item(name, cost=10)
            case "Batteries":
                item = Item(name, cost=50)
            
            case _:
                item = Item(name)
        
    else:
        item = Item(name)

    return item

def generate_condition(name, clear="", description=""):
    match(name):
        case "Exhausted":
            condition = Condition(name, "After long rest")
        case "Frightened":
            condition = Condition(name, "After short rest", "WIL save to approach source of fear.")
        case "Hungry":
            condition = Condition(name, "After meal")
        case "Injured":
            condition = Condition(name, "After full rest", "Disadvantage on STR & DEX saves.")
        case "Drained":
            condition = Condition(name, "After full rest", "Disadvantage on WIL saves.")
        case _:
            condition = Condition(name, clear, description)
        
    return condition

def generate_item_json(item_type, name):
    print(f"Generating {item_type} {name}...")
    match item_type.lower():
        case "item":
            max_durability = all_items[item_type][name]["max_durability"]
            durability = all_items[item_type][name]["durability"]
            cost = all_items[item_type][name]["cost"]
            new_item = Item(name, max_durability, durability, 1, 1, cost)
            return new_item
        case "weapon":
            max_durability = all_items[item_type][name]["max_durability"]
            durability = all_items[item_type][name]["durability"]
            cost = all_items[item_type][name]["cost"]
            wc = all_items[item_type][name]["class"].lower()
            wc = wc.replace(" ", "_")
            weapon_class = Weapon_Class[wc]
            
            new_item = Weapon(name, weapon_class, max_durability, cost=cost, durability=durability)
            return new_item
        case "armor":
            max_durability = all_items[item_type][name]["max_durability"]
            durability = all_items[item_type][name]["durability"]
            cost = all_items[item_type][name]["cost"]
            armor_class = Armor_Class[all_items[item_type][name]["class"].lower()]
            protection = all_items[item_type][name]["protection"]
            size_x = all_items[item_type][name]["size_x"]
            size_y = all_items[item_type][name]["size_y"]
            new_item = Armor(name, armor_class, max_durability, durability, size_x, size_y, protection)
            return new_item
        case "spell":
            cost = all_items[item_type][name]["cost"]
            effect = all_items[item_type][name]["effect"]
            recharge = all_items[item_type][name]["recharge"]
            new_item = Spell(name, effect, recharge)
            return new_item
        case "condition":
            clear = all_items[item_type][name]["clear"]
            effect = all_items[item_type][name]["effect"]
            new_item = Condition(name, clear, effect)
            return new_item


def snap_area_setup():
    snap_main = sa(31, 472, title="Main")
    snap_off = sa(31, 575, title="Offhand", is_bottom_edge=True)
    snap_body1 = sa(146, 472, title="Body 1", is_right_edge=True)
    snap_body2 = sa(146, 575, title="Body 2", is_bottom_edge=True, is_right_edge=True)
    snap_1 = sa(259, 471, title="Pack 1")
    snap_2 = sa(363, 471, title="Pack 2")
    snap_3 = sa(468, 471, title="Pack 3", is_right_edge=True)
    snap_4 = sa(259, 577, title="Pack 4", is_bottom_edge=True)
    snap_5 = sa(363, 577, title="Pack 5", is_bottom_edge=True)
    snap_6 = sa(468, 577, title="Pack 6", is_bottom_edge=True, is_right_edge=True)

    grit_area = ga(140, 713)

    delete_area = da(31, 325)

    snap_main.set_right(snap_body1)
    snap_main.set_bottom(snap_off)

    snap_off.set_right(snap_body2)

    snap_body1.set_bottom(snap_body2)

    snap_1.set_right(snap_2)
    snap_1.set_bottom(snap_4)

    snap_2.set_right(snap_3)
    snap_2.set_bottom(snap_5)

    snap_3.set_bottom(snap_6)

    snap_4.set_right(snap_5)

    snap_5.set_right(snap_6)

    return [snap_main, snap_off, snap_body1, snap_body2, snap_1, snap_2, snap_3, snap_4, snap_5, snap_6, grit_area, delete_area]

def get_slot_snap(snap_area):
    title = snap_area.title
    match title:
        case "Main":
            location = "main"
            x = 0
            y = 0
        case "Offhand":
            location = "main"
            x = 1
            y = 0
        case "Body 1":
            location = "main"
            x = 0
            y = 1
        case "Body 2":
            location = "main"
            x = 1
            y = 1
        case "Pack 1":
            location = "back"
            x = 0
            y = 0
        case "Pack 2":
            location = "back"
            x = 0
            y = 1
        case "Pack 3":
            location = "back"
            x = 0
            y = 2
        case "Pack 4":
            location = "back"
            x = 1
            y = 0
        case "Pack 5":
            location = "back"
            x = 1
            y = 1
        case "Pack 6":
            location = "back"
            x = 1
            y = 2
        case "Grit":
            location = "grit"
            x = 0
            y = 0
        case "Delete":
            location = "delete"
            x = 0
            y = 0
    
    return location, x, y

def generate_inventory(inventory, snap_areas, grit):
    all_cards = []
    for i in range(0, inventory.main_rows):
        for j in range(0, inventory.main_cols):
            item = inventory.main[i][j]
            if item != None:
                match item.type:
                    case "item":
                        card = Item_Card(item)
                    case "weapon":
                        card = Weapon_Card(item)
                    case "magic weapon":
                        card = Magic_Weapon_Card(item)
                    case "armor":
                        card = Armor_Card(item)
                    case "purse":
                        card = Purse_Card(item)
                    case "spell":
                        card = Spell_Card(item)
                    case "condition":
                        card = Condition_Card(item)
                
                all_cards.append(card)

                match i:
                    case 0:
                        match j:
                            case 0:
                                card.set_x(snap_areas[0].x)
                                card.set_y(snap_areas[0].y)
                            case 1:
                                card.set_x(snap_areas[2].x)
                                card.set_y(snap_areas[2].y)
                    case 1:
                        match j:
                            case 0:
                                card.set_x(snap_areas[1].x)
                                card.set_y(snap_areas[1].y)
                            case 1:
                                card.set_x(snap_areas[3].x)
                                card.set_y(snap_areas[3].y)
        
    for i in range(0, inventory.back_rows):
        for j in range(0, inventory.back_cols):
            item = inventory.back[i][j]
            if item != None:
                match item.type:
                    case "item":
                        card = Item_Card(item)
                    case "weapon":
                        card = Weapon_Card(item)
                    case "magic weapon":
                        card = Magic_Weapon_Card(item)
                    case "armor":
                        card = Armor_Card(item)
                    case "purse":
                        card = Purse_Card(item)
                    case "spell":
                        card = Spell_Card(item)
                    case "condition":
                        card = Condition_Card(item)
                
                all_cards.append(card)

                match i:
                    case 0:
                        match j:
                            case 0:
                                card.set_x(snap_areas[4].x)
                                card.set_y(snap_areas[4].y)
                            case 1:
                                card.set_x(snap_areas[5].x)
                                card.set_y(snap_areas[5].y)
                            case 2:
                                card.set_x(snap_areas[6].x)
                                card.set_y(snap_areas[6].y)
                    case 1:
                        match j:
                            case 0:
                                card.set_x(snap_areas[7].x)
                                card.set_y(snap_areas[7].y)
                            case 1:
                                card.set_x(snap_areas[8].x)
                                card.set_y(snap_areas[8].y)
                            case 2:
                                card.set_x(snap_areas[9].x)
                                card.set_y(snap_areas[9].y)
    
    i = 0
    for condition in grit:
        card = Condition_Card(condition)
        card.snap_to(snap_areas[10])
        card.set_x(snap_areas[10].x + i)
        all_cards.append(card)
        i += 50

    return all_cards

def load_character(filename):
    global my_char, all_cards, snap_areas
    ### Load character from file, generates inventory cards and resets snap areas
    my_char = Character()
    my_char.load_file(filename)
    all_cards = generate_inventory(my_char.inventory, snap_areas, my_char.grit_conditions)
    snap_areas = snap_area_setup()

def buttons_setup():
    buttons = []
    buttons.append(My_Button(490, 840, 100, 25, "Save", (230, 231, 232), (44, 46, 53)))
    buttons.append(My_Button(390, 840, 100, 25, "Open", (230, 231, 232), (44, 46, 53)))
    buttons.append(My_Button(290, 840, 100, 25, "New Card", (230, 231, 232), (44, 46, 53)))
    buttons.append(My_Button(190, 840, 100, 25, "New Char", (230, 231, 232), (44, 46, 53)))

    return buttons



def new_character_gui():
    global my_char, all_cards, snap_areas

    def get_random_name():
        f_name = random.choice(MOUSE_NAMES)
        m_name = random.choice(MOUSE_MATRINAMES)
        return f_name + " " + m_name

    def get_random_stat():
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        roll_3 = random.randint(1, 6)

        return roll_1 + roll_2 + roll_3 - min(roll_1, roll_2, roll_3)

    def get_d6():
        return random.randint(1, 6)


    root = Tk()
    root.title("Make a mouse")
    root.geometry('450x850')
    root.resizable(False, False)
    global item_1, item_2
    item_1 = ""
    item_2 = ""
    def generate_background_and_items(hp, pips):
        global item_1, item_2
        if (type(hp) != int) or (type(pips) != int):
            return "Invalid HP or Pips"
        elif (hp < 1) or (hp > 6) or (pips < 1) or (pips > 6):
            return "HP and pips must be between 1 and 6"
        background, item_1, item_2 = get_background(hp, pips)
        item1_str = ""
        item2_str = ""
        if (type(item_1) == str):
            item1_str = item_1
        else:
            item1_str = item_1.get_name()
        if (type(item_2) == str):
            item2_str = item_2
        else:
            item2_str = item_2.get_name()
        back_entry.config(text=background)
        back_text = f"Your background is what your mouse was before becoming an adventurer. As a {background} you recieve {item1_str} and {item2_str}. Additionally, every adventurer starts with a bundle of torches and rations plus your choice of weapon."
        back_title.config(text=back_text)
        back_val.set(background)
        return background

    birthsign_val = StringVar(value="")
    disposition_val = StringVar(value="")
    def set_birthsign(roll):
        birthsign, dispo = get_birthsign(roll)
        birthsign_val.set(birthsign.title())
        birthsign_show.config(text=birthsign.title())
        disposition_val.set(dispo)
        disposition_show.config(text=dispo)
    
    def generate_coat(roll1, roll2):
        coat = get_coat(roll1, roll2)
        coat_show.config(text=f"Your coat: {coat}")
        return coat
    
    def generate_detail(roll):
        detail = get_look(roll)
        detail_show.config(text=f"{detail}")
        return detail

    ipadding = {'padx': 10, 'pady': 5}

    content = Frame(root)
    content.grid(row=0, column=0, sticky=NSEW)

    # Name
    name_lbl = ttk.Label(content, text="Choose a name appropriate for a brave mouse:")
    name_lbl.grid(**ipadding, row=0, column=0, columnspan=3, sticky=NSEW)
    name_val = StringVar(value="")
    name_entry = ttk.Entry(content, textvariable=name_val)
    name_entry.grid(**ipadding, row=1, column=0, columnspan=2, sticky="ew")

    random_name_btn = ttk.Button(content, text="Random Name", command=lambda: name_val.set(get_random_name()))
    random_name_btn.grid(**ipadding, row=1, column=2, sticky="ew")

    # STATS

    stats_lbl = ttk.Label(content, text="Roll 3d6 and add the two highest values together, choose which stat to give each value (you can swap any two values):",
                      justify=LEFT, wraplength=400)
    stats_lbl.grid(**ipadding, row=3, column=0, columnspan=3, sticky=NSEW)

    str_lbl = ttk.Label(content, text="STR:")
    str_lbl.grid(**ipadding, row=4, column=0, sticky="ew")
    
    dex_lbl = ttk.Label(content, text="DEX:")
    dex_lbl.grid(**ipadding, row=4, column=1, sticky="ew")

    wil_lbl = ttk.Label(content, text="WIL:")
    wil_lbl.grid(**ipadding, row=4, column=2, sticky="ew")

    str_val = IntVar(value=0)
    str_entry = ttk.Entry(content, textvariable=str_val)
    str_entry.grid(**ipadding, row=5, column=0, sticky="")

    dex_val = IntVar(value=0)
    dex_entry = ttk.Entry(content, textvariable=dex_val)
    dex_entry.grid(**ipadding, row=5, column=1, sticky="")

    wil_val = IntVar(value=0)
    wil_entry = ttk.Entry(content, textvariable=wil_val)
    wil_entry.grid(**ipadding, row=5, column=2, sticky="")

    str_random = ttk.Button(content, text="Random", command=lambda: str_val.set(get_random_stat()))
    str_random.grid(**ipadding, row=6, column=0, sticky="ew")

    dex_random = ttk.Button(content, text="Random", command=lambda: dex_val.set(get_random_stat()))
    dex_random.grid(**ipadding, row=6, column=1, sticky="ew")

    wil_random = ttk.Button(content, text="Random", command=lambda: wil_val.set(get_random_stat()))
    wil_random.grid(**ipadding, row=6, column=2, sticky="ew")

    # HP, pips, background
    back_lbl = ttk.Label(content, text="Roll d6 for your HP and d6 for your starting pips, your background will be generated from those values:", justify=LEFT, wraplength=400)
    back_lbl.grid(**ipadding, row=7, column=0, columnspan=3, sticky=NSEW)

    hp_lbl = ttk.Label(content, text="HP:")
    hp_lbl.grid(**ipadding, row=8, column=0, sticky="ew")

    pips_lbl = ttk.Label(content, text="Pips:")
    pips_lbl.grid(**ipadding, row=8, column=1, sticky="ew")

    back_lbl = ttk.Label(content, text="Background:")
    back_lbl.grid(**ipadding, row=8, column=2, sticky="ew")

    hp_val = IntVar(value=0)
    hp_entry = ttk.Entry(content, textvariable=hp_val)
    hp_entry.grid(**ipadding, row=9, column=0, sticky="ew")

    pips_val = IntVar(value=0)
    pips_entry = ttk.Entry(content, textvariable=pips_val)
    pips_entry.grid(**ipadding, row=9, column=1, sticky="ew")

    back_val = StringVar(value="")
    back_entry = ttk.Label(content, text=back_val.get())
    back_entry.grid(**ipadding, row=9, column=2, sticky="ew")

    hp_random = ttk.Button(content, text="Random", command=lambda: hp_val.set(get_d6()))
    hp_random.grid(**ipadding, row=10, column=0, sticky="ew")

    pips_random = ttk.Button(content, text="Random", command=lambda: pips_val.set(get_d6()))
    pips_random.grid(**ipadding, row=10, column=1, sticky="ew")

    back_generate = ttk.Button(content, text="Generate", command=lambda: back_val.set(generate_background_and_items(hp_val.get(), pips_val.get())))
    back_generate.grid(**ipadding, row=10, column=2, sticky="ew")

    back_title = ttk.Label(content, text="Your background is what your mouse was before becoming an adventurer.", justify=LEFT, wraplength=400)
    back_title.grid(**ipadding, row=11, column=0, columnspan=3, sticky="nswe")

    weapon_lbl = ttk.Label(content, text="Choose a weapon:")
    weapon_lbl.grid(**ipadding, row=12, column=0, sticky="ew")

    weapon_val = StringVar(value=WEAPONS[0])
    weapon_picker = ttk.OptionMenu(content, weapon_val, *WEAPONS)
    weapon_picker.grid(**ipadding, row=12, column=1, columnspan=2, sticky="ew")

    # Details

    birthsign_lbl = ttk.Label(content, text="Roll a d6 to get your birthsign and disposition:")
    birthsign_lbl.grid(**ipadding, row=13, column=0, columnspan=2, sticky="ew")

    birthsign_get = ttk.Button(content, text="Generate", command=lambda: set_birthsign(birthsign_roll.get()))
    birthsign_get.grid(**ipadding, row=13, column=2, sticky="ew")


    birthsign_roll = IntVar(value=0)
    birthsign_entry = ttk.Entry(content, textvariable=birthsign_roll)
    birthsign_entry.grid(**ipadding, row=14, column=0, sticky="ew")


    my_birthsign = ttk.Label(content, text="Your birthsign:")
    my_birthsign.grid(**ipadding, row=14, column=1, sticky="ew")

    my_disposition = ttk.Label(content, text="Your disposition:")
    my_disposition.grid(**ipadding, row=14, column=2, sticky="ew")

    birthsign_random = ttk.Button(content, text="Random", command=lambda: birthsign_roll.set(get_d6()))
    birthsign_random.grid(**ipadding, row=15, column=0, sticky="ew")

    birthsign_show = ttk.Label(content, text=birthsign_val.get())
    birthsign_show.grid(**ipadding, row=15, column=1, sticky="ew")

    disposition_show = ttk.Label(content, text=disposition_val.get(), wraplength=125)
    disposition_show.grid(**ipadding, row=15, column=2, sticky="ew")

    coat_roll_1 = IntVar(value=0)
    coat_roll_2 = IntVar(value=0)
    coat_val = StringVar(value="")
    coat_lbl = ttk.Label(content, text="Roll 2d6 for your coat:")
    coat_lbl.grid(**ipadding, row=16, column=0, columnspan=3, sticky="ew")

    coat_entry_1 = ttk.Entry(content, textvariable=coat_roll_1)
    coat_entry_1.grid(**ipadding, row=17, column=0, sticky="ew")

    coat_entry_2 = ttk.Entry(content, textvariable=coat_roll_2)
    coat_entry_2.grid(**ipadding, row=17, column=1, sticky="ew")

    coat_generate = ttk.Button(content, text="Generate", command=lambda: coat_val.set(generate_coat(coat_roll_1.get(), coat_roll_2.get())))
    coat_generate.grid(**ipadding, row=17, column=2, sticky="ew")

    coat_random_1 = ttk.Button(content, text="Random", command=lambda: coat_roll_1.set(get_d6()))
    coat_random_1.grid(**ipadding, row=18, column=0, sticky="ew")

    coat_random_2 = ttk.Button(content, text="Random", command=lambda: coat_roll_2.set(get_d6()))
    coat_random_2.grid(**ipadding, row=18, column=1, sticky="ew")

    coat_show = ttk.Label(content, text="Your coat:", wraplength=125)
    coat_show.grid(**ipadding, row=18, column=2, sticky="ew")

    detail_label = ttk.Label(content, text="Roll d66 for your details (d66 means d6 * 10 + d6):", wraplength=400)
    detail_label.grid(**ipadding, row=19, column=0, columnspan=3, sticky="ew")

    detail_roll = IntVar(value=0)
    detail_entry = ttk.Entry(content, textvariable=detail_roll)
    detail_entry.grid(**ipadding, row=20, column=0, sticky="ew")

    detail_random = ttk.Button(content, text="Random", command=lambda: detail_roll.set(get_d6()*10 + get_d6()))
    detail_random.grid(**ipadding, row=20, column=1, sticky="ew")

    detail_val = StringVar(value="")
    generate_detail_btn = ttk.Button(content, text="Generate", command=lambda: detail_val.set(generate_detail(detail_roll.get())))
    generate_detail_btn.grid(**ipadding, row=20, column=2, sticky="ew")

    detail_show_lbl = ttk.Label(content, text="Your look:")
    detail_show_lbl.grid(**ipadding, row=21, column=0, columnspan=2, sticky="e")

    detail_show = ttk.Label(content, text=detail_val.get(), wraplength=125)
    detail_show.grid(**ipadding, row=21, column=2, sticky="ew")

    def save_character():
        right = 0
        if (max(str_val.get(), dex_val.get(), wil_val.get()) <= 9):
            right = 1
        elif (max(str_val.get(), dex_val.get(), wil_val.get()) <= 7):
            right = 2

        if (right > 0):
            extra = Toplevel(root)
            extra.geometry("300x100")
            extra.resizable(False, False)
            extra.title("You have the right to extra items")
            new_content = ttk.Frame(extra)
            new_content.grid(row=0, column=0, sticky="nsew")

            extra_lbl = ttk.Label(new_content, text=f"You have the right to {right} items", justify="center")
            extra_lbl.grid(**ipadding, row=0, column=0, columnspan=3, sticky="ew")

            extra.columnconfigure(0, weight=1)
            extra.rowconfigure(0, weight=1)
            new_content.columnconfigure(0, weight=3)
        
        else:
            new_char = Character(name_val.get(), back_val.get(), birthsign_val.get(), coat_val.get(), detail_val.get(),
                                 str_val.get(), dex_val.get(), wil_val.get(), hp_val.get(), pips_val.get(), disposition=disposition_val.get())
            new_char.inventory.add_item(generate_item("Torches"), "back", 0, 2)
            new_char.inventory.add_item(generate_item("Rations"), "back", 1, 2)
            new_char.inventory.add_item(generate_item_json("weapon", weapon_val.get()), "main", 0, 0)
            if (type(item_1) != str):
                new_char.inventory.add_item(item_1, "back", 0, 1)
            if (type(item_2) != str):
                new_char.inventory.add_item(item_2, "back", 1, 1)
            new_char.save_json()
            file = "characters/" + new_char.name.replace(" ", "_") + ".json"
            load_character(file)
            root.destroy()

    def cancel_character():
        root.destroy()


    ok_btn = ttk.Button(content, text="Save", command=lambda: save_character())
    ok_btn.grid(**ipadding, row=22, column=2, sticky="ew")

    cancel_btn = ttk.Button(content, text="Cancel", command=lambda: cancel_character())
    cancel_btn.grid(**ipadding, row=22, column=1, sticky="ew")


    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.columnconfigure(0, weight=3)
    content.rowconfigure(22, weight=5)
    ttk.Style().theme_use('clam')
    root.mainloop()



def button_func(button):
    match button:
        case "Save":
            my_char.save_json()
        case "Open":
            # root = Tk()
            # root.title("Slect a file")
            # root.geometry('350x200')
            # root.resizable(False, False)
            # btn = Button(root, text="Click Me", command= lambda: select_file(root))
            # btn.grid(column=2, row=0)
            # root.mainloop()
            char_file = select_file()
            if (char_file != ""):
                load_character(char_file)
        case "New Card":
            root = Tk()
            root.title("Create New Card")
            root.geometry('450x200')
            root.resizable(False, False)
            try:
                root.bind_all("<Button-1>", lambda event: event.widget.focus_set())
            except:
                pass
            
            type_lbl = Label(root, text="Type:")
            type_lbl.grid(column=0, row=0)

            clicked_type = StringVar()
            # clicked_type.set(ITEM_TYPES[0])
            global custom, clicked_name, item_name
            custom = False
            clicked_name = StringVar()
            clicked_type.set(ITEM_TYPES[0])
            item_name = ""

            WEAPON_CLASSES = ["Light", "Medium", "Heavy", "Improvised", "Ammunition"]
            ARMOR_CLASSES  = ["Light", "Heavy"]

            purse_val = StringVar(value=0)
            max_purse_val = StringVar(value=250)

            durability_val = StringVar(value=3)
            
            description_val = StringVar(value="")
            clear_val = StringVar(value="")

            clicked_class = StringVar()

            size_x_val = StringVar(value=1)
            size_y_val = StringVar(value=1)

            additional_widgets = []
            def not_in_list_fill(event):
                global custom, clicked_name, item_name
                for i in range(0, len(additional_widgets)):
                    old_widget = additional_widgets[i]
                    old_widget.destroy()
                    old_widget = None
                additional_widgets.clear()
                item_name = event.widget.get()
                print(item_name)

                if not event.widget.get() in event.widget["values"] and event.widget.get() != "":
                    custom = True
                    if (clicked_type.get() != "Condition"):
                        # ok_btn.config(state="disabled")

                        durablitity_lbl = Label(root, text="Durability:")
                        durablitity_lbl.grid(column=0, row=3)
                        additional_widgets.append(durablitity_lbl)

                        # durability_val = StringVar(value=3)
                        durability_spin = Spinbox(root, from_=0, to=9, textvariable=durability_val, width=3)
                        durability_spin.grid(column=0, row=4)
                        additional_widgets.append(durability_spin)

                        if (clicked_type.get() == "Item"):
                            size_x_lbl = Label(root, text="Horizontal slots:")
                            size_x_lbl.grid(column=1, row=3)
                            additional_widgets.append(size_x_lbl)

                            # size_x_val = StringVar(value=1)
                            size_x_spin = Spinbox(root, from_=1, to=3, textvariable=size_x_val, width=3)
                            size_x_spin.grid(column=1, row=4)
                            additional_widgets.append(size_x_spin)

                            size_y_lbl = Label(root, text="Vertical slots:")
                            size_y_lbl.grid(column=2, row=3)
                            additional_widgets.append(size_y_lbl)

                            # size_y_val = StringVar(value=1)
                            size_y_spin = Spinbox(root, from_=1, to=2, textvariable=size_y_val, width=3)
                            size_y_spin.grid(column=2, row=4)
                            additional_widgets.append(size_y_spin)

                        if (clicked_type.get() == "Weapon" or clicked_type.get() == "Armor") and event.widget.get() != "":
                            match clicked_type.get():
                                case "Weapon":
                                    list_classes = WEAPON_CLASSES
                                case "Armor":
                                    list_classes = ARMOR_CLASSES
                            class_lbl = Label(root, text="Class:")
                            class_lbl.grid(column=1, row=3)
                            additional_widgets.append(class_lbl)

                            # clicked_class = StringVar()
                            clicked_class.set(list_classes[0])

                            class_menu = OptionMenu(root, clicked_class, *list_classes)
                            class_menu.grid(column=1, row=4)
                            class_menu.configure(width=30)
                            additional_widgets.append(class_menu)
                            if (clicked_type.get() == "Armor"):
                                protection_lbl = Label(root, text="Protection:")
                                protection_lbl.grid(column=2, row=3)
                                additional_widgets.append(protection_lbl)

                                protection_val = StringVar(value=1)
                                protection_spin = Spinbox(root, from_=0, to=9, textvariable=protection_val, width=3)
                                protection_spin.grid(column=2, row=4)
                                additional_widgets.append(protection_spin)
                        
                    if (clicked_type.get() == "Condition" and event.widget.get() != ""):
                        decription_lbl = Label(root, text="Description:")
                        decription_lbl.grid(column=0, row=3, columnspan=3)
                        additional_widgets.append(decription_lbl)

                        # description_val = StringVar(value="")
                        description_entry = Entry(root, textvariable=description_val)
                        description_entry.grid(column=0, row=4, columnspan=3, sticky="ew")
                        additional_widgets.append(description_entry)

                        clear_lbl = Label(root, text="Cleared by:")
                        clear_lbl.grid(column=0, row=5, columnspan=3)
                        additional_widgets.append(clear_lbl)

                        # clear_val = StringVar(value="")
                        clear_entry = Entry(root, textvariable=clear_val)
                        clear_entry.grid(column=0, row=6, columnspan=3, sticky="ew")
                        additional_widgets.append(clear_entry)
                            

                
                elif event.widget.get() != "":
                    custom = False
                    ok_btn.config(state="normal")

            item_widgets = []        
            def select_type(clicked_type):
                global custom, clicked_name, item_name
                for i in range(0, len(item_widgets)):
                    old_widget = item_widgets[i]
                    old_widget.destroy()
                    old_widget = None
                for i in range(0, len(additional_widgets)):
                    old_widget = additional_widgets[i]
                    old_widget.destroy()
                    old_widget = None
                item_widgets.clear()

                name_list = []

                match(clicked_type.lower()):
                    case "item":
                        name_list = ITEMS
                    case "weapon":
                        name_list = WEAPONS
                    case "magic weapon":
                        pass
                    case "armor":
                        name_list = ARMORS
                    case "purse":
                        pass
                    case "spell":
                        name_list = SPELLS
                    case "condition":
                        name_list = CONDITIONS
                
                if (clicked_type.lower() != "purse" and clicked_type.lower() != "magic weapon"):
                    
                    name_lbl = Label(root, text="Name:")
                    name_lbl.grid(column=1, row=0)
                    item_widgets.append(name_lbl)

                    clicked_name = StringVar()
                    clicked_name.set(name_list[0])

                    name_menu = Combobox(root, width=30, textvariable=clicked_name)
                    name_menu['values'] = name_list
                    name_menu.grid(column=1, row=1, columnspan=2)
                    name_menu.bind("<FocusOut>", not_in_list_fill)
                    name_menu.bind("<Return>", not_in_list_fill)
                    name_menu.bind("<<ComboboxSelected>>", not_in_list_fill)
                    item_widgets.append(name_menu)
                    print(f"All widgets: {item_widgets}")
                
                if (clicked_type.lower() == "purse"):
                    purse_lbl = Label(root, text="Pips in purse:")
                    purse_lbl.grid(column=1, row=0)
                    item_widgets.append(purse_lbl)

                    max_purse_val = StringVar(value=250)

                    purse_val = StringVar(value=0)
                    purse_spin = Spinbox(root, from_=0, to=max_purse_val, textvariable=purse_val, width=3)
                    purse_spin.grid(column=1, row=1)
                    item_widgets.append(purse_spin)

                    max_purse_lbl = Label(root, text="Max pips:")
                    max_purse_lbl.grid(column=2, row=0)
                    item_widgets.append(max_purse_lbl)

                    max_purse_spin = Spinbox(root, from_=0, to=6000, textvariable=max_purse_val, width=3)
                    max_purse_spin.grid(column=2, row=1)
                    item_widgets.append(max_purse_spin)
                    ok_btn.config(state="normal")

            select_type(clicked_type.get())
            type_menu = OptionMenu(root, clicked_type, *ITEM_TYPES, command=select_type)
            type_menu.grid(column=0, row=1)
            type_menu_width = len(max(*ITEM_TYPES, key=len))
            type_menu.config(width=type_menu_width + 4)

            
            

            def click_cancel():
                root.destroy()
            
            def click_ok():
                item_name = clicked_name.get()
                match (clicked_type.get().lower()):
                    case "item":
                        if not custom:
                            all_cards.append(Item_Card(generate_item_json("item", item_name)))
                        else:
                            all_cards.append(Item_Card(Item(item_name, max_durability=int(durability_val.get()), size_x=int(size_x_val.get()), size_y=int(size_y_val.get()))))
                    case "weapon":
                        if not custom:
                            all_cards.append(Weapon_Card(generate_item_json("weapon", item_name)))
                        else:
                            wc = clicked_class.get().lower()
                            wc = wc.replace(" ", "_")
                            weapon_class = Weapon_Class[wc]
                            all_cards.append(Weapon_Card(Weapon(item_name, weapon_class, max_durability=int(durability_val.get()))))
                            print(f"{durability_val.get()}")
                            print(f"{all_cards[-1].get_item().get_max_durability()}")
                    case "magic weapon":
                        pass
                    case "armor":
                        if not custom:
                            all_cards.append(Armor_Card(generate_item_json("armor", item_name)))
                    case "purse":
                        all_cards.append(Purse_Card(Purse(int(purse_val.get()), int(max_purse_val.get()))))
                    case "spell":
                        if not custom:
                            all_cards.append(Spell_Card(generate_item_json("spell", item_name)))
                    case "condition":
                        if not custom:
                            all_cards.append(Condition_Card(generate_item_json("condition", item_name)))
                        else:
                            all_cards.append(Condition_Card(Condition(item_name, clear_val.get(), description_val.get())))
                

                root.destroy()
                        
            root.grid_rowconfigure(8, weight=1)

            cancel_btn = Button(root, text="Cancel", command=click_cancel)
            cancel_btn.grid(column=0, row=8, sticky="swe")

            ok_btn = Button(root, text="OK", command=click_ok, state="normal", width=30)
            ok_btn.grid(column=1, row=8, sticky="swe", columnspan=4)

            
            root.mainloop()

        case "New Char":
            new_character_gui()

def select_file():
    filetypes = [("Json", '*.json')]

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir="characters/",
        filetypes=filetypes
    )

    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )

    return filename


def main():
    global my_char, snap_areas, all_cards
    # mychar = generate_character()
    # mychar.print()
    pygame.init()
    flags = DOUBLEBUF
    surface = pygame.display.set_mode((590, 865), flags)
    surface.set_alpha(None)
    pygame.display.set_caption('Character Sheet')
    toolbar = Toolbar(590, 25)

    bg = pygame.image.load('resources\character_sheet.png').convert()
    bg = pygame.transform.scale(bg, (590, 840))

    running  = True
    paused = False

    my_char = Character()
    my_char.load_file("characters/Elmer_Black.json")

    # pygame.mouse.set_visible(False)
    closed_cursor_img = pygame.image.load('resources\closed_hand_cursor.png')
    closed_cursor_img = pygame.transform.scale(closed_cursor_img, (16, 16))
    closed_cursor_rect = closed_cursor_img.get_rect()

    snap_areas = snap_area_setup()
    all_cards = generate_inventory(my_char.inventory, snap_areas, my_char.grit_conditions)

    purse = Purse_Card(Purse(1234))
    spell = Spell_Card(generate_item("Fireball"))
    exhausted = Condition_Card(generate_condition("Frightened"))

    # all_cards.append(purse)
    # all_cards.append(spell)
    # all_cards.append(exhausted)

    buttons = buttons_setup()
    

    # myCard = Weapon_Card(generate_item("Sword"))
    # large_card = Weapon_Card(generate_item("Warhammer"))
    # armor_card = Armor_Card(generate_item("Light Armor"))

    # all_cards.append(myCard)
    # all_cards.append(large_card)
    # all_cards.append(armor_card)

    color = (235, 235, 235)
    
    FPS = 90
    clock = pygame.time.Clock()

    my_char.print()

    pygame.display.update()
    opened_card = None
    while running:  
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if opened_card != None:
                        opened_card.close_ui_window()
                        opened_card = None
                        paused = False
                    else:
                        running = False
                if event.key == pygame.K_s:
                    my_char.save_json()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for card in all_cards:
                    if (card.get_type() != "condition" and not paused):
                        if event.button == 1:
                            card.click_durability(pygame.mouse.get_pos())
                        if event.button == 3:
                            card.right_click_durability(pygame.mouse.get_pos())
                if event.button == 1:
                    # print("Left click")
                    for button in buttons:
                        if (button.pressed(pygame.mouse.get_pos(), surface) and not paused):
                            button_func(button.get_label())
                    if opened_card != None:
                        if pygame.Rect.collidepoint(opened_card.get_close_rec(), pygame.mouse.get_pos()):
                            opened_card.close_ui_window()
                            opened_card = None
                            paused = False
                if event.button == 3:
                    for cards in reversed(all_cards):
                        if (cards.check_inside(*pygame.mouse.get_pos()) and opened_card == None):
                            paused = True
                            opened_card = cards
                            cards.draw_ui_window(surface)




        if (not paused):
                    
            surface.blit(bg, (0, 0))
            my_char.draw(surface)
            toolbar.draw(surface)

            for button in buttons:
                button.draw(surface)
                button.hover(pygame.mouse.get_pos(), surface)

            for area in snap_areas:
                if (area.get_title() == "Delete"):
                    area.draw(surface)


            for i in range(len(all_cards)):
                all_cards[i].drag()
                all_cards[i].draw(surface)
                # if (all_cards[i].get_type() != "condition" and pygame.event.get(pygame.MOUSEBUTTONDOWN)):
                #     all_cards[i].click_durability(pygame.mouse.get_pos())

                for j in range(i + 1, len(all_cards)):
                    if all_cards[j].get_rect().colliderect(all_cards[i].get_rect()):
                        # print(f"Collision between {all_cards[i].get_title()} and {all_cards[j].get_title()}")
                        all_cards[i].add_blocked(all_cards[j].get_rect())
                        all_cards[j].block(all_cards[i])
                        # print(f"Blocked: {all_cards[i].get_blocked()}")

                for area in snap_areas:
                    if (area.check_collision(all_cards[i].get_rect(), all_cards[i].get_type()) and not all_cards[i].gets_dragged()):
                        # print(f"Snap {all_cards[i].get_title()} to {area.get_title()}")
                        if (not all_cards[i].get_is_snapped()):
                            ### Add item to inventory slot
                            loc, x, y = get_slot_snap(area)
                            if (area.get_is_grit()):
                                my_char.add_grit(all_cards[i].get_condition())
                            elif (area.get_title() == "Delete"):
                                card = all_cards.pop(i)
                                card.delete()
                                i = 0
                                break
                            elif (all_cards[i].type == "condition"):
                                my_char.inventory.add_condition(all_cards[i].condition, loc, x, y)
                            else:
                                my_char.inventory.add_item(all_cards[i].item, loc, x, y)
                            
                            if (all_cards[i].is_very_wide()):
                                area.get_bottom().add_card()
                                area.get_right().add_card()
                                area.get_right().get_bottom().add_card()
                                area.get_right().get_right().add_card()
                                area.get_right().get_right().get_bottom().add_card()
                            elif (all_cards[i].is_large_square()):
                                area.get_bottom().add_card()
                                area.get_right().add_card()
                                area.get_right().get_bottom().add_card()
                            elif (all_cards[i].is_tall()):
                                area.get_bottom().add_card()
                            elif (all_cards[i].is_wide()):
                                area.get_right().add_card()

                            area.add_card()
                            all_cards[i].snap_to(area)
                            ### Move card to bottom of pile
                            # for card in all_cards:
                            #     print(card.get_title() + ', ', end="")

                        ### We don't want to send the card to the bottom of the pile if it's a grit area
                        if (not area.get_is_grit()):
                            card = all_cards[i]
                            all_cards.pop(i)
                            all_cards.insert(0, card)
                # In case there are no more cards after deletion
                try:
                    if all_cards[i].gets_dragged():
                        if (all_cards[i].get_is_snapped()):


                            for card in all_cards:
                                card.clear_blocked()

                            a = all_cards[i].get_snap_area()
                            a.remove_card()
                            all_cards[i].remove_snap()
                            if (all_cards[i].is_very_wide()):  
                                a.get_bottom().remove_card()
                                a.get_right().remove_card()
                                a.get_right().get_bottom().remove_card()
                                a.get_right().get_right().remove_card()
                                a.get_right().get_right().get_bottom().remove_card()
                            elif (all_cards[i].is_large_square()):
                                a.get_bottom().remove_card()
                                a.get_right().remove_card()
                                a.get_right().get_bottom().remove_card()
                            elif (all_cards[i].is_tall()):
                                a.get_bottom().remove_card()
                            elif (all_cards[i].is_wide()):
                                a.get_right().remove_card()
                                

                            ### Remove item from inventory slot
                            loc, x, y = get_slot_snap(a)
                            if (a.get_is_grit()):
                                my_char.remove_grit(all_cards[i].get_condition())
                            elif (all_cards[i].type == "condition"):
                                my_char.inventory.remove_condition(all_cards[i].condition, loc, x, y)
                            else:
                                my_char.inventory.remove_item(all_cards[i].item, loc, x, y)
                            

                        all_cards[i].clear_blocking()
                        for card in all_cards:
                            card.clear_blocked()

                            ### Redraw cards to avoid visual glitch
                            all_cards[0].draw(surface)
                            try:
                                all_cards[i+1].draw(surface)
                            except:
                                pass
                            all_cards[i].draw(surface)

                        card = all_cards[i]
                        all_cards.append(card)
                        all_cards.pop(i)
                        
                        # Trail effect
                        # for redraw_card in all_cards:
                        #     redraw_card.draw(surface)
                    #     pygame.mouse.set_visible(False)
                    #     closed_cursor_rect.center = pygame.mouse.get_pos()
                    #     surface.blit(closed_cursor_img, closed_cursor_rect)
                    # else:
                    #     pygame.mouse.set_visible(True)
                except:
                    pass
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()