import pygame
import random
import time
from os import path

pygame.init()

display_width = 800
display_height = 600

car_width = 75
car_height = 89

black = (0, 0, 0)
white = (255, 255, 255)
blue = (66, 134, 244)

crashes = 0
high_score = 0

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Racing Game")
clock = pygame.time.Clock()

carImg = pygame.image.load('Racecar.png')


count = 0


def high_score_check():
    name = 'Scores.txt'
    destination = 'D:\\Dropbox\\Python Files\\Apa\\'
    global high_score
    if not path.isfile(destination + name):
        pass

    else:
        file = open("Scores.txt", "r")
        prev_high_score = file.read()
        if int(prev_high_score) > int(high_score):
            high_score = prev_high_score
        else:
            pass


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(a, b):
    gameDisplay.blit(carImg, (a, b))


def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()


def restart():
    time.sleep(2)
    game_loop()


def message_display(text, font_size, coordsx, coordsy):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    TextSurf, Text_rect = text_objects(text, font)

    if text == "You Crashed":
        Text_rect.center = coordsx, coordsy
        gameDisplay.blit(TextSurf, Text_rect)
        pygame.display.update()
        restart()
    else:
        Text_rect = coordsx, coordsy
        gameDisplay.blit(TextSurf, Text_rect)


def crash():
    global crashes
    global high_score
    crashes += 1
    high_score_check()

    if count > int(high_score):
        high_score = count
    else:
        pass

    message_display('You Crashed', 115, (display_width / 2), (display_height / 2))


def game_loop():

    x = ((display_width * 0.5) - car_width / 2)
    y = (display_height * 0.8)

    x_change = 0
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width - thing_width)
    thing_starty = -600
    thing_speed = 3
    global count
    count = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                name = 'Scores.txt'
                destination = 'D:\\Dropbox\\Python Files\\Apa\\'
                if (path.isfile(destination + name)) or not(path.isfile(destination + name)):
                    f = open(destination + name, 'w')
                    f.write(str(high_score))
                    f.close()

                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        gameDisplay.fill(white)
        x += x_change
        car(x, y)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        if thing_starty + thing_height > y and thing_startx + thing_width > x:
            if thing_startx < x + car_width:
                crash()

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_speed += 0.5
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width - thing_width)
            count += 1

        message_display("Score: {}".format(count), 25, 0, 0)
        message_display('High score: {}'.format(high_score), 25, display_width - 175, 0)

        pygame.display.update()

        clock.tick(60)

high_score_check()
game_loop()
