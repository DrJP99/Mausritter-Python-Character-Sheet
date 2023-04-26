import pygame

grab_hand = (
    "                ", # 1
    "                ", # 2
    "                ", # 3
    "    XX XX XX    ", # 4
    "   X..X..X..XX  ", # 5
    "   X........X.X ", # 6
    "    X.........X ", # 7
    "   XX.........X ", # 8
    "  X...........X ", # 9
    "  X..........X  ", # 10
    "   X.........X  ", # 11
    "    X.......X   ", # 12
    "     X......X   ", # 13
    "     X......X   ", # 14
    "                ", # 15
    "                ", # 16
)

grab_hand_cursor = pygame.cursors.compile(grab_hand, black='X', white='.', xor='o')