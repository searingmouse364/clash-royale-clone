import pygame
import os


class Hog_rider(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, type, dimensions):
        super().__init__()
        self.type = type
        self.winDimensions = dimensions
        self.image = pygame.image.load(
            os.path.join("resources", "hogRider.png"))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        if self.type == "blue":
            self.rect.centery -= 5
        else:
            self.rect.centery += 5

        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.top > self.winDimensions[1]:
            self.kill()
