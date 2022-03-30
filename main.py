import pygame
from towers import Tower
from hog_rider import Hog_rider

pygame.init()


class game():
    def __init__(self, width=0, height=0):
        self.WIDTH = width
        self.HEIGHT = height
        self.wn = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.running = False
        self.characterGroup = pygame.sprite.Group(
            Tower(250, self.HEIGHT - 100, (10, 86, 168)), Tower(250, 0 + 100, (168, 44, 10)))
        self.clock = pygame.time.Clock()
        self.mouse = pygame.mouse

    def game_loop(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.mouse.get_pressed()[0]:
                        if self.mouse.get_pos()[1] > self.HEIGHT/2:
                            self.characterGroup.add(
                                Hog_rider(self.mouse.get_pos()[0], self.mouse.get_pos()[1], "blue", (self.WIDTH, self.HEIGHT)))
                        else:
                            self.characterGroup.add(
                                Hog_rider(self.mouse.get_pos()[0], self.mouse.get_pos()[1], "red", (self.WIDTH, self.HEIGHT)))
            self.wn.fill((10, 168, 58))
            self.characterGroup.draw(self.wn)
            self.characterGroup.update()
            pygame.display.update()


if __name__ == "__main__":
    G = game(500, 900)
    G.game_loop()
