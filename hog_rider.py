import pygame
import os


class Hog_rider(pygame.spirte.Sprite):
    def __init__(self, pos_x, pos_y):
        self.image = pygame.image.load(
            os.path.join("resources", "hogRider.png"))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.centery += 5
