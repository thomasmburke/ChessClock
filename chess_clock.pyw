import pygame
from pygame.locals import *
import os, sys

# Designed to load in custom image
def load_image(name, colorkey=None):
    fullName = os.path.join("images", name)
    try:
        image = pygame.image.load(fullName)
    except pygame.error as e:
        print ('Cannot load image:', name)
        print(str(e))
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

# Initialize start of game to 5 minutes
aTime = 300
bTime = 300
aDown = False
bDown = False

# Initialize all pygame imported modules
pygame.init()
# Determin window size of game - for me same size as my image
screen = pygame.display.set_mode((741,461))
# Set title of window
pygame.display.set_caption("Chess Clock")
# Load in images and fonts
clockImage, clockRect = load_image("chess_clock.png")
font = pygame.font.Font("fonts/Roboto-Black.ttf", 34)
# Create a clock object to help keep track of time
clock = pygame.time.Clock()

while True:
    # Determines how often the system looks for input
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == USEREVENT:
            if aTime > 0:
                aTime -= 1
            else:
                pygame.time.set_timer(USEREVENT, 0)
        elif event.type == (USEREVENT + 1):
            if bTime > 0:
                bTime -= 1
            else:
                pygame.time.set_timer(USEREVENT, 0)
        elif event.type == KEYDOWN:
            if event.key == K_a:
                # The other one should turn on immediately
                pygame.time.set_timer(USEREVENT, 0)
                pygame.time.set_timer(USEREVENT+1, 1000)
                bDown = True
                aDown = False
            if event.key == K_b:
                pygame.time.set_timer(USEREVENT+1, 0)
                pygame.time.set_timer(USEREVENT, 1000)
                aDown = True
                bDown = False
            if event.key == K_q:
                aTime += 60 # add a minute from alloted aTime_rect
            if event.key == K_e:
                aTime -= 60 # subtract a minutes
            if event.key == K_w:
                bTime += 60
            if event.key == K_r:
                bTime -= 60
            # If they press the pause button
            if event.key == K_PAUSE or event.key == K_p:
                #pause both timers
                pygame.time.set_timer(USEREVENT+1, 0)
                pygame.time.set_timer(USEREVENT, 0)
    # Formattime into minutes:seconds
    aTime_str = "%d:%02d" % (int(aTime/60),int(aTime%60))
    bTime_str = "%d:%02d" % (int(bTime/60),int(bTime%60) )
    aTime_txt = font.render(aTime_str, 1, (255, 255, 255))
    bTime_txt = font.render(bTime_str, 1, (255, 255, 255))
    aTime_rect = aTime_txt.get_rect()
    aTime_rect.center = (240, 240)
    bTime_rect = bTime_txt.get_rect()
    bTime_rect.center = (510, 240)
    #update image & fonts on the screen
    screen.blit(clockImage, clockRect)
    screen.blit(aTime_txt, aTime_rect)
    screen.blit(bTime_txt, bTime_rect)
    pygame.display.update()
