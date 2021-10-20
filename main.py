import pgzrun
import random

from pgzero.keyboard import keyboard
from pgzero.actor import Actor

czas = 120
score = 0
WIDTH = 1000
HEIGHT = 700
gracz = Actor('enemy',(500,HEIGHT-70-46))

bomba = [Actor('bomb', (random.randint(30, WIDTH - 30), -600)),
              Actor('bomb', (random.randint(30, WIDTH - 30), -400)),
              Actor('bomb', (random.randint(30, WIDTH - 30), -200)),
              Actor('bomb', (random.randint(30, WIDTH - 30), -100)),
              Actor('bomb', (random.randint(30, WIDTH - 30), -150))]


moneta = Actor('coin', (random.randint(30,WIDTH-30), 0))
def odejmijSekune():
    global czas
    if czas>=1:
        czas -= 1
    else:
        czas = 0

def draw():
    screen.fill((208, 244, 247))
    for i in range(WIDTH//70+1):
        screen.blit('grass',(i*70, 630))
    for i in bomba:
        i.draw()
    moneta.draw()
    gracz.draw()
    screen.draw.text(str(czas), (50, 30), color="orange", fontsize = 60, fontname = "font")
    screen.draw.text(str(score), (WIDTH-100, 30), color='orange', fontsize = 60, fontname = 'font')

def update():
    global score
    global czas
    if czas > 0:
        if keyboard.RIGHT and gracz.x<WIDTH-35:
            gracz.x += 5
        if keyboard.LEFT and gracz.x>35:
            gracz.x -= 5
        for i in bomba:
            i.y += 4
        for i in bomba:
            if gracz.collidepoint(i.pos):
                score -= 1
                czas -= 15
                i.y = -50
                i.x = random.randint(30, WIDTH - 30)
            if i.y > 600:
                i.y = -50
                i.x = random.randint(30, WIDTH - 30)
        moneta.y += 3
        if gracz.collidepoint(moneta.pos):
            moneta.y = -300
            moneta.x = random.randint(30,WIDTH-30)

            score += 1
        if moneta.y > 600:
            moneta.y = -100
            moneta.x = random.randint(30,WIDTH-30)
            score -= 1


clock.schedule_interval(odejmijSekune, 1)
pgzrun.go()