import itertools
import pygame as pg


pg.init()
screen = pg.display.set_mode((480, 480))
clock = pg.time.Clock()

width, height = screen.get_size()
block_size = 60
# Create a surface onto which we'll blit the rectangles.
background = pg.Surface((width, height))
colors = itertools.cycle((pg.Color('white'), pg.Color('black')))

for y in range(0, height, block_size):
    for x in range(0, width, block_size):
        rect = (x, y, block_size, block_size)
        pg.draw.rect(background, next(colors), rect)
    next(colors)  # Skip the next color.


# Then you can just blit the background in the while loop.
screen.blit(background, (0, 0))
pg.display.flip()
