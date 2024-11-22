import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)


pygame.init()


gameDisplay = display.set_mode(SCREEN_SIZE)


gameDisplay.fill(Color('lightblue'))




draw.rect(gameDisplay, Color('red'), Rect(50, 50, 45, 300))

draw.rect(gameDisplay, Color('red'), Rect(200, 50, 45, 300))

draw.rect(gameDisplay, Color('red'), Rect(50, 180, 150, 45))

draw.rect(gameDisplay, Color('blue'), Rect(350, 200, 45, 150))

draw.circle(gameDisplay, Color('gold'), (370, 130),30)



display.flip()


input("Press enter to exit")