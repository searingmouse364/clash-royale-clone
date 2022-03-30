import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, color=(0, 0, 0)):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
