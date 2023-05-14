
pip install pygame

import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.display.set_caption('Snake Game')

class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.direction = (0, -1)

    def move(self):
        head = self.elements[0].copy()
        head[0] += self.direction[0] * 20
        head[1] += self.direction[1] * 20
        self.elements.insert(0, head)
        self.elements.pop()

    def grow(self):
        self.size += 1
        self.elements.append(self.elements[-1])

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, GREEN, pygame.Rect(element[0], element[1], 20, 20))

class Food:
    def __init__(self):
        self.position = [random.randint(1, (WIDTH//20)-1)*20, random.randint(1, (HEIGHT//20)-1)*20]

    def draw(self):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], 20, 20))

snake = Snake()
food = Food()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, 1):
                snake.direction = (0, -1)
            if event.key == pygame.K_DOWN and snake.direction != (0, -1):
                snake.direction = (0, 1)
            if event.key == pygame.K_LEFT and snake.direction != (1, 0):
                snake.direction = (-1, 0)
            if event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                snake.direction = (1, 0)

    snake.move()

    if snake.elements[0] == food.position:
        snake.grow()
        food = Food()

    if (snake.elements[0] in snake.elements[1:] or
            not 0 <= snake.elements[0][0] < WIDTH or
            not 0 <= snake.elements[0][1] < HEIGHT):
        pygame.quit()
        sys.exit()

    screen.fill(WHITE)
    snake.draw()
    food.draw()
    pygame.display.flip()

    clock.tick(10)


