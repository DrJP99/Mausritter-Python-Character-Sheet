import pygame

colour = (230, 231, 232) #or whatever colour you want

class Toolbar:
    def __init__(self, width=0, height=0): #And other customisation options
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,865)
        # self.leftbutton = ButtonClass(50, height)
        # self.rightbutton = ButtonClass(50, height)

    def update(self):
        self.leftbutton.hover() #to animate an effect if the mouse hovers over
        self.rightbutton.hover()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # screen.blit(self.leftbutton.draw(), self.leftbutton.getRect())
        # screen.blit(self.rightbutton.draw(), self.rightbutton.getRect())

    def click(self, pos):
        if self.leftbutton.getRect().collidepoint(pos):
            self.leftbutton.click()

        if self.rightbutton.getRect().collidepoint(pos):
            self.rightbutton.click()

class ButtonClass:
    def __init__(self, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)

    def hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            print("Is hovering over button")

    def click(self):
        print("Clicked button")

    def draw(self):
        return self.image

    def getRect(self):
        return self.rect