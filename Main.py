'''
input:
Digits of pi (d)

output:

Two Blocks
Bounce off eachother
Bounce off the wall
    Collision Detection

transfer energy according to mass
    afterVel1  = (mass1 - mass2)/(mass1 + mass2) * velocity1
    afterVel2  = (mass1 * 2)/(mass1 + mass2) * velocity1

Count collisions
'''
import pygame
pygame.init()
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0, 0, 0))
clock = pygame.time.Clock()  # set up clock
x1 = 300
x2 = 600
v1 = 0
v2 = -0.25
digits = 2
mass1 = 1
mass2 = 100 ** (digits - 1)
collisions = 0

while 1:
    sqr1 = pygame.Rect(x1, 700, 100,100)
    sqr2 = pygame.Rect(x2, 600, 200, 200)
    if sqr2.left <= sqr1.right:
         collisions +=1
         v1Temp = v1
         v2Temp = v2
         
         
         #v1  = (((mass1 - mass2)/(mass1 + mass2)) * v1Temp) + (((mass2 * 2)/(mass1 + mass2)) * v2Temp)
         #v2  = (((mass1 * 2)/(mass1 + mass2)) * v1Temp) - (((mass1 - mass2)/(mass1 + mass2)) * v2Temp)
         print(f"Collsions: {collisions}")
    if sqr1.left <= 0:
        v1 *= -1
    x1 += v1
    x2 += v2
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),sqr1)
    pygame.draw.rect(screen,(255,255,255), sqr2)
    pygame.display.flip()   
    