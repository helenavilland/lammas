import pygame
import time


class Snake:
    def __init__(self, start_x, start_y, game):
        self.window_size = game.window_size
        self.size = 20
        self.game = game
        self.location = [(start_x - self.size * i, start_y) for i in range(5)]
        self.dir = (1, 0)
        self.apple = None
        # create a surface object, image is drawn on it.
        self.image1 = pygame.image.load(r'C:\Users\guest37\Downloads\costume1.png')
        self.image1 = pygame.transform.scale(self.image1, (self.size, self.size))
        self.image2 = pygame.image.load(r'C:\Users\guest37\Downloads\costume4.png')
        self.image2 = pygame.transform.scale(self.image2, (self.size, self.size))
        self.image3 = pygame.image.load(r'C:\Users\guest37\Downloads\costume5.png')
        self.image3 = pygame.transform.scale(self.image3, (self.size, self.size))


    def update(self):
        next_loc = (self.location[0][0] + self.dir[0] * self.size, self.location[0][1] + self.dir[1] * self.size)
        self.location.insert(0, next_loc)
        last = self.location.pop()
        self.check_collision()
        if self.apple.x == next_loc[0] and self.apple.y == next_loc[1]:
            self.apple.eat()
            self.location.append(last)
            self.game.grow_apple()

    def render(self, screen):
        for x, y in self.location:
            # copying the image surface object
            # to the display surface object at
            # (0, 0) coordinate.
            if time.time() % 0.6 < 0.2:
                screen.blit(self.image1, (x, y))
            elif time.time() % 0.6 < 0.4:
                screen.blit(self.image2, (x, y))
            else:
                screen.blit(self.image3, (x, y))

    def check_collision(self):
        self.check_walls()
        self.check_body()

    def check_walls(self):
        head = self.location[0]
        if head[0] < 0 or head[1] < 0 or head[0] >= self.window_size[0] or head[1] >= self.window_size[1]:
            self.game.state = "end"

    def check_body(self):
        if len(self.location) != len(set(self.location)):
            self.game.state = "end"
