import pygame

class Snap_Area():
    def __init__(self, x, y, size_x = 102, size_y = 102, occupied = False, title="", is_right_edge = False, is_bottom_edge = False, right=None, bottom=None):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.occupied = occupied
        self.title = title
        self.is_right_edge = is_right_edge
        self.is_bottom_edge = is_bottom_edge
        self.right = right
        self.bottom = bottom
        self.is_grit = False


    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_size_x(self, size_x):
        self.size_x = size_x

    def set_size_y(self, size_y):
        self.size_y = size_y\
    
    def set_occupied(self, occupied):
        self.occupied = occupied

    def set_title(self, title):
        self.title = title

    def set_right(self, right):
        self.right = right
    
    def set_bottom(self, bottom):
        self.bottom = bottom

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_size_x(self):
        return self.size_x
    
    def get_size_y(self):
        return self.size_y
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size_x, self.size_y)

    def get_occupied(self):
        return self.occupied
    
    def get_title(self):
        return self.title

    def get_right(self):
        if (self.right == None):
            return False
        return self.right

    def get_bottom(self):
        if (self.bottom == None):
            return False
        return self.bottom

    def get_is_grit(self):
        return self.is_grit

    def add_card(self):
        self.occupied = True
    
    def check_collision(self, rect, card_type):
        tollerance = 45
        if (not self.occupied):
            if (self.x - tollerance < rect.x and self.x + self.size_x + tollerance > rect.x + self.size_x and self.y - tollerance < rect.y and self.y + self.size_y + tollerance > rect.y + self.size_y):
                if (self.is_right_edge and rect.width > rect.height or self.is_bottom_edge and rect.width < rect.height):
                    return False
                # Vary large rectangle
                if (rect.width != rect.height and rect.width > 204):
                    if (self.is_bottom_edge or self.is_right_edge):
                        return False
                    elif (self.right.is_right_edge):
                        return False
                    elif (self.bottom.get_occupied() or self.right.get_occupied() or self.bottom.get_right().get_occupied() or self.right.get_right().get_occupied() or self.right.get_right().get_bottom().get_occupied()):
                        return False
                # Large square
                elif (rect.width == rect.height and rect.width > 102):
                    if (self.is_bottom_edge or self.is_right_edge):
                        return False
                    elif (self.bottom.get_occupied() or self.right.get_occupied() or self.bottom.get_right().get_occupied()):
                        return False
                elif (rect.height > rect.width):
                    if (self.bottom.get_occupied()):
                        return False
                elif (rect.width > rect.height):
                    if (self.right.get_occupied()):
                        return False
                return True
    
    def remove_card(self):
        self.occupied = False
    
    def draw(self, screen):
        tolerance = 45
        # pygame.draw.rect(screen, (255, 0, 0), (self.x - tolerance, self.y - tolerance, self.size_x, self.size_y))
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.size_x, self.size_y))
    
class Grit_Area(Snap_Area):
    def __init__(self, x, y, size_x = 208, size_y = 102, occupied = False):
        super().__init__(x, y, size_x, size_y, occupied, "Grit", True, True, None, None)
        self.is_grit = True

    def add_card(self):
        self.occupied = False
    
    def get_is_grit(self):
        return self.is_grit

    def check_collision(self, rect, card_type = "generic"):
        tollerance = 45
        if (card_type == "condition"):
            if (self.x - tollerance < rect.x and self.x + self.size_x + tollerance > rect.x + rect.width and self.y - tollerance < rect.y and self.y + self.size_y + tollerance > rect.y + rect.height):
                return True
        # return super().check_collision(rect, is_grit)

class Delete_Area(Snap_Area):
    def __init__(self, x, y, size_x = 102, size_y = 102, occupied = False):
        super().__init__(x, y, size_x, size_y, occupied, "Delete", True, True, None, None)    
        self.trash_img = pygame.image.load("resources/trash.png")
        self.trash_img = pygame.transform.scale(self.trash_img, (self.size_x*0.75, self.size_y*0.75))
        alpha = 50
        self.trash_img.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)
        self.trash_img_rect = self.trash_img.get_rect()
        self.trash_img_rect.center = (self.x + self.size_x/2, self.y + self.size_y/2)

    def check_collision(self, rect, card_type = "generic"):
        tollerance = 15
        if (self.x - tollerance < rect.x and self.x + self.size_x + tollerance > rect.x + self.size_x and self.y - tollerance < rect.y and self.y + self.size_y + tollerance > rect.y + self.size_y):
            return True
        # return super().check_collision(rect, is_grit)

    def draw(self, screen):
        surface = pygame.Surface((self.size_x, self.size_y), pygame.SRCALPHA)
        surface.fill((150, 150, 150, 50))
        screen.blit(surface, (self.x, self.y))
        # screen.blit(self.trash_img, (self.x, self.y))

        screen.blit(self.trash_img, self.trash_img_rect)

        # pygame.draw.rect(screen, ((100, 100, 100, 0)), (self.x, self.y, self.size_x, self.size_y))