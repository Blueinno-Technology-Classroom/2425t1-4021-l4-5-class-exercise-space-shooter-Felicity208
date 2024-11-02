import pgzrun
import math
import random
import time
from pgzhelper import * 


WIDTH = 1024
HEIGHT = 768

background = Actor('blue')
player = Actor("playership1_red")
player.x = WIDTH/2
player.bottom = HEIGHT
playerlasers = []
enemies = []
enemylasers = []

player.hp = 100
    

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
            sounds.sfx_laser2.play()
            playerlaser = Actor("laserred05")
            playerlaser.pos = player.pos
            if enemies:
                playerlaser.point_towards(random.choice(enemies))
            else:
                playerlaser.angle = 90
            playerlasers.append (playerlaser)

        for l in playerlasers:
            l.move_forward(7)
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
            enemy_skin = random.choice(['enemyblack1', 'enemyred4' , 'enemygreen2', 'enemyblue2'])
            enemy = Actor(enemy_skin)
            enemy.x = random.randint(0, WIDTH)
            enemy.top = 25
            enemies.append (enemy)
            

        for e in enemies:
            if random.randint(0, 100) < 5:
                enemylaser = Actor('lasergreen13')
                enemylaser.pos = e.pos
                enemylaser.point_towards(player)
                enemylasers.append(enemylaser)
            e.point_towards(player)
            e.move_forward(5)
            if e.collide_pixel(player):
                enemies.remove(e)
                player.hp -= 1 


        for x in enemylasers:
            x.move_forward(7)
            if x.top > HEIGHT:
                 enemylasers.remove(x)
            else:
                if x.colliderect(player):
                    enemylasers.remove(x)
                    player.hp -= 1
                    sounds.mech_ohno.play()
                    if player.hp == 0:
                        time.sleep (0.3)
                        sounds.gun_shoot.play()

            
    
     

def draw():
    if player.hp > 0:
        screen.clear()
        background.draw()
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
    else:
        screen.clear()
        screen.draw.text('Game Over', center = (WIDTH/2, HEIGHT/2), fontsize = 100)
    


pgzrun.go()
