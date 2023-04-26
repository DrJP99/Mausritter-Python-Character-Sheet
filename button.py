import pygame

class My_Button:
    def __init__(self, x, y, size_x = 102, size_y = 102, label="", color = (0, 0, 0), text_color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.label = label
        self.color = color
        self.original_color = color
        self.text_color = text_color
        self.rect = pygame.Rect(self.x, self.y, self.size_x, self.size_y)
        self.font = pygame.font.SysFont("Bahnschrift", 20)
        self.text = self.font.render(self.label, True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center
    
    def set_x(self, x):
        self.x = x
        self.rect.x = x
        self.text_rect.center = self.rect.center

    def set_y(self, y):
        self.y = y
        self.rect.y = y
        self.text_rect.center = self.rect.center

    def set_size_x(self, size_x):
        self.size_x = size_x
        self.rect.width = size_x
        self.text_rect.center = self.rect.center

    def set_size_y(self, size_y):
        self.size_y = size_y
        self.rect.height = size_y
        self.text_rect.center = self.rect.center

    def set_label(self, label):
        self.label = label
        self.text = self.font.render(self.label, True, self.text_color)
        self.text_rect.center = self.rect.center

    def set_color(self, color):
        self.color = color

    def set_text_color(self, text_color):
        self.text_color = text_color

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_size_x(self):
        return self.size_x
    
    def get_size_y(self):
        return self.size_y
    
    def get_rect(self):
        return self.rect
    
    def get_label(self):
        return self.label
    
    def get_color(self):
        return self.color
    
    def get_text_color(self):
        return self.text_color
    
    def pressed(self, mouse_pos, screen):
        if (self.rect.collidepoint(mouse_pos) and screen.get_rect().collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] == 1):
            return True
        else:
            return False
    
    def hover(self, mouse_pos, screen):
        if (self.rect.collidepoint(mouse_pos) and screen.get_rect().collidepoint(mouse_pos)):
            new_color = (self.original_color[0] - 30, self.original_color[1] - 30, self.original_color[2] - 30)
            self.set_color(new_color)
        else:
            self.set_color(self.original_color)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (44, 46, 53), self.rect, 2)
        text = self.font.render(self.label, True, self.text_color)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        screen.blit(self.text, self.text_rect)
