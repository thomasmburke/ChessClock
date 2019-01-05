import pygame
from pygame.locals import *
import os, sys


def load_image(name, colorkey=None):
    fullname = os.path.join("images", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


time_a = 0
time_b = 0
a_on = False
b_on = False


pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Chess Clock")

background = pygame.Surface(screen.get_size())
rect = background.fill((0, 0, 0))

clock_image, clock_rect = load_image("chess_clock.png")

clock = pygame.time.Clock()

font = pygame.font.Font("fonts/Roboto-Black.ttf", 34)

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == USEREVENT:
            if time_a > 0:
                time_a -= 1
            else:
                pygame.time.set_timer(USEREVENT, 0)
        elif event.type == (USEREVENT + 1):
            if time_b > 0:
                time_b -= 1
            else:
                pygame.time.set_timer(USEREVENT, 0)
        elif event.type == KEYDOWN:
            if event.key == K_a:
                if not a_on:
                    # Set for 1 second (1000 milliseconds)
                    pygame.time.set_timer(USEREVENT, 1000)
                    a_on = True
                else:
                    # The other one should turn on immediately
                    pygame.time.set_timer(USEREVENT, 0)
                    pygame.time.set_timer(USEREVENT+1, 1000)
                    b_on = True
                    a_on = False
            if event.key == K_b:
                if not b_on:
                    pygame.time.set_timer(USEREVENT+1, 1000)
                    b_on = True
                else:
                    pygame.time.set_timer(USEREVENT+1, 0)
                    pygame.time.set_timer(USEREVENT, 1000)
                    a_on = True
                    b_on = False
            if event.key == K_q:
                time_a += 60 # add a minute from alloted time_a_rect
            if event.key == K_z:
                time_a -= 60 # subtract a minutes
            if event.key == K_g:
                time_b += 60
            if event.key == K_n:
                time_b -= 60
            if event.key == K_PAUSE or event.key == K_p:
                #pause both timers
                pygame.time.set_timer(USEREVENT+1, 0)
                pygame.time.set_timer(USEREVENT, 0)
    # Formattime into minutes:seconds
    time_a_str = "%d:%02d" % (int(time_a/60),int(time_a%60))
    time_b_str = "%d:%02d" % (int(time_b/60),int(time_b%60) )
    time_a_txt = font.render(time_a_str, 1, (255, 255, 255))
    time_b_txt = font.render(time_b_str, 1, (255, 255, 255))
    time_a_rect = time_a_txt.get_rect()
    time_a_rect.center = (310, 310)
    time_b_rect = time_b_txt.get_rect()
    time_b_rect.center = (525, 310)
    screen.blit(background, rect)
    screen.blit(clock_image, clock_rect)
    screen.blit(time_a_txt, time_a_rect)
    screen.blit(time_b_txt, time_b_rect)
    pygame.display.update()
