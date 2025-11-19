import pygame
pygame.init()

class buttons:
    def __inti__(self, y, x, width, height, text, font_size, color, hover_color, font=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont('Arial', self.font_size)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hovered = False

    def 