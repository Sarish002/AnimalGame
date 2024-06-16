import random
import sqlite3
import pygame
import time

timelim = 150

tiles = 7
j = 0
d = 0
Time = sqlite3.connect('Score.db')
Timmy = Time.cursor()

Timmy.execute('SELECT * FROM score')
rec = Timmy.fetchall()

i = random.randint(0, 11)
listing = ['Deer.png', 'Fox.png',
           'Rabbit.png', 'Pig.png', 'Rooster.png',
           'Goat.png', 'Dinosaur.png', 'Fish.png',
           'Rhino.png',
           'Turtle.png',
           'Dog.png',
           'Raccoon.png']

pygame.init()
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption('Tiger and Deer!')

Clock = pygame.time.Clock()
running = True

start = time.time()
TextFont = pygame.font.Font('VarelaRound-Regular.otf', 60)

JungleSong = pygame.mixer.music.load('song-of-jungle-155814.mp3')
pygame.mixer.music.play(-1, 0.0)
x = 0

Tiger = pygame.transform.scale(pygame.image.load(random.choice(['Tiger.png',
                                                                'Lion.png',
                                                                'Leopard.png',
                                                                'Cheetah.png'])), (224, 224))

Deer = pygame.transform.scale(pygame.image.load(listing[i]), (224, 224))

TigerRect = Tiger.get_rect()
TigerRect.center = (80, 300)
DeerRect = Deer.get_rect()
DeerRect.center = (random.randint(200, 687), random.randint(160, 687))
p = 0
while p == 0:
    if DeerRect.center == TigerRect.center:
        DeerRect.center = (random.randint(200, 687), random.randint(160, 687))

    else:
        break

Image = pygame.transform.scale(pygame.image.load('down.png'), (224, 224))

ImageRect = Image.get_rect()
ImageRect.center = (1376, 666)

OTextFont = pygame.font.Font('Xiomara-wWLw.ttf', 25)
ATextFont = OTextFont

z = rec[0][0]
STextFont = TextFont
scroll = 0
pygame.display.flip()
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False

    elapsed_time = time.time() - start
    m = timelim - int(elapsed_time)

    screen.fill((255, 255, 255))
    Keys = pygame.key.get_pressed()

    Text = TextFont.render('Points: {}'.format(x), True, '#000000')
    TextRect = Text.get_rect()
    TextRect.center = (750, 80)

    if Keys[pygame.K_UP] and TigerRect.y > 20:
        TigerRect.y -= 10

    elif Keys[pygame.K_DOWN] and TigerRect.y < 630:
        TigerRect.y += 10

    elif Keys[pygame.K_RIGHT] and TigerRect.x < 1350:
        TigerRect.x += 10

    elif Keys[pygame.K_LEFT] and TigerRect.x > 36.5:
        TigerRect.x -= 10

    elif TigerRect.colliderect(DeerRect):

        p = 0
        while p == 0:
            if DeerRect.center == TigerRect.center:
                DeerRect.center = (random.randint(200, 687), random.randint(200, 687))

            else:
                break

        if i == 0:
            x += 20
            sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
            sound.play()

        elif i == 1:
            x += 30
            sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
            sound.play()

        elif i == 2:
            x += 15
            sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
            sound.play()

        elif i == 3:
            x += 10
            sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
            sound.play()

        elif i == 4:
            x += 12.5
            sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
            sound.play()

        elif i == 5:
            x += 25
            sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
            sound.play()

        elif i == 6:
            x += 100
            pysound = pygame.mixer.Sound('bonus-points-190035.mp3')
            pysound.play()

        elif i == 7:
            x += 35
            sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
            sound.play()

        elif i == 8:
            x += 50
            pysound = pygame.mixer.Sound('bonus-points-190035.mp3')
            pysound.play()

        elif i == 9:
            x += 10
            sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
            sound.play()

        elif i == 10:
            x += 20.25
            sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
            sound.play()

        elif i == 11:
            x += 20.75
            sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
            sound.play()

        i = random.randint(0, 11)
        listing = ['Deer.png', 'Fox.png',
                   'Rabbit.png', 'Pig.png', 'Rooster.png',
                   'Goat.png', 'Dinosaur.png', 'Fish.png',
                   'Rhino.png',
                   'Turtle.png',
                   'Dog.png',
                   'Raccoon.png']

        Deer = pygame.transform.scale(pygame.image.load(listing[i]), (224, 224))
        DeerRect = Deer.get_rect()
        DeerRect.center = (random.randint(200, 997), random.randint(200, 687))

        j += 1

    OText = OTextFont.render('High Score: {}'.format(z), True, 'black')
    OTextRect = OText.get_rect()
    OTextRect.center = (200, 50)

    SText = STextFont.render('Animals: {} '.format(j), True, 'black')
    STextRect = SText.get_rect()
    STextRect.center = (750, 150)

    if x >= rec[0][0]:
        z = x
    seconds = (timelim - int(elapsed_time)) // 60
    minutes = (timelim - int(elapsed_time)) % 60
    AText = ATextFont.render(f'Time: {seconds:02}:{minutes:02}', True, 'black')
    ATextRect = AText.get_rect()
    ATextRect.center = (1300, 50)
    screen.blit(AText, ATextRect)

    if m == 0:
        time.sleep(2)
        pygame.mixer.music.stop()
        pythons = pygame.mixer.Sound('level-complete-winner-piano-om-fx-1-00-06.mp3')
        pythons.play()
        running = False

    screen.blit(Tiger, TigerRect)
    screen.blit(Deer, DeerRect)
    screen.blit(SText, STextRect)
    screen.blit(Text, TextRect)
    screen.blit(Image, ImageRect)
    screen.blit(OText, OTextRect)

    y = Clock.tick(60) / 1000
    pygame.display.update()

if x >= rec[0][0]:
    pythonsound = pygame.mixer.Sound('cute-interface-sound-2-application-modern-shiny-SBA-300421199-preview.mp3')
    pythonsound.play()
    Timmy.execute('UPDATE score SET scorer=:a', {'a': int(x)})
    Time.commit()
    Time.close()

