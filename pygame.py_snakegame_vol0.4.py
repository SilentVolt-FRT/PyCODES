import pygame as pg
import sys
from random import randrange

pg.init()

WINDOW = 600
TITLE_SIZE = 30
RANGE = (TITLE_SIZE // 2, WINDOW - TITLE_SIZE // 2, TITLE_SIZE)

get_random_position = lambda: (randrange(*RANGE), randrange(*RANGE))

snake = pg.Rect(0, 0, TITLE_SIZE - 2, TITLE_SIZE - 2)
snake.center = get_random_position()
food = pg.Rect(0, 0, TITLE_SIZE -2, TITLE_SIZE -2)
food.center = get_random_position()

screen = pg.display.set_mode((WINDOW, WINDOW))
clock = pg.time.Clock()

length = 1
segments = [snake.copy()]
snake_dir = (0, 0,)
time, time_step = 0, 110

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -TITLE_SIZE)
            if event.key == pg.K_s:
                snake_dir = (0, -TITLE_SIZE)
            if event.key == pg.K_a:
                snake_dir = (-TITLE_SIZE, 0)
            if event.key == pg.K_d:
                snake_dir = (-TITLE_SIZE, 0)

    screen.fill('black')

    # Move snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[ -length:]

    # Check food collision
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1

    # Check borders
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW:
        snake.center = get_random_position()
        length = 1
        segments = [snake.copy()]

    # Draw food and snake
    pg.draw.rect(screen, (255, 0, 0), food) # Red color in RGB
    for segment in segments:
        pg.draw.rect(screen, (0, 255, 0), segment) # Green color

    pg.display.flip()
    clock.tick(60)
