import pygame
from towers import Tower


pygame.init()


class game():
    def __init__(self, width=0, height=0):
        self.wn = pygame.display.set_mode((width, height))
        self.running = False
        self.characterGroup = pygame.sprite.Group(
            Tower(250, 400, (0, 255, 0)), Tower(250, 100, (0, 255, 0)))

    def game_loop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            self.wn.fill((0, 0, 0))
            self.characterGroup.draw(self.wn)
            pygame.display.update()


if __name__ == "__main__":
    G = game(500, 500)
    G.game_loop()
