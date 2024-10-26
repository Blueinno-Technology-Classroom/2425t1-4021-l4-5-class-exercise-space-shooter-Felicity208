import pgzrun
import math
import random

WIDTH = 1024
HEIGHT = 768

player = Actor("playership1_red")
player.x = WIDTH/2
player.bottom = HEIGHT
playerlasers = []
enemies = []
enemylasers = []

player.hp = 10
    

def update():
    if player.hp > 0:
        if keyboard.up:
            player.y -= 5
                
        if keyboard.down:
            player.y += 5
        if keyboard.left:
            player.x -= 5
            if player.x < 0:
                player.x = 0
        if keyboard.right:
            player.x += 5
            if player.x > WIDTH:
                player.x = WIDTH

        player.top = max(0, player.top)
        player.bottom = min(HEIGHT, player.bottom)

        if keyboard.space:
            playerlaser = Actor("laserred05")
            playerlaser.pos = player.pos
            playerlasers.append (playerlaser)

        for l in playerlasers:
            l.y -= 5
            if l.bottom < 0:
                playerlasers.remove(l)
            else:
                for e in enemies:
                    if l.colliderect(e):
                        enemies.remove(e)
                        playerlasers.remove(l)
                        break
        
        #print(len(lasers))


        if random.randint(0, 100) < 5:
            enemy = Actor("enemyblack2")
            enemy.x = random.randint(0, WIDTH)
            enemy.top = 25
            enemies.append (enemy)
            

        for e in enemies:
            if random.randint(0, 500) < 3:
                enemylaser = Actor('lasergreen07')
                enemylaser.pos = e.pos
                enemylasers.append(enemylaser)


        for x in enemylasers:
            x.y += 7
            if x.top > HEIGHT:
                enemylasers.remove(x)
            else:
                if x.colliderect(player):
                    enemylasers.remove(x)
                    player.hp -= 1
    
                

            
    
     

def draw():
    screen.clear()
    for e in enemies:
        e.draw()
    player.draw()
    for l in playerlasers:
        l.draw()
    for x in enemylasers:
        x.draw()
    screen.draw.filled_rect(Rect(0,0, WIDTH, 20), 'red')
    screen.draw.filled_rect(Rect(0,0,WIDTH * player.hp/100, 20), 'green')
    screen.draw.text(f'{player.hp}/100',  center=(WIDTH/2, 10), color = 'white')


pgzrun.go()
