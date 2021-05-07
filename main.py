import pygame
import os
import math
import random
from points import *
import formular

os.environ['SDL_VIDEO_CENTERED']='1'

width, height = 1920, 1080
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Double Pendulum")
fps = 30
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


mass1 = 40
mass2 = 40
length1 = 200
length2 = 200

angle1 = math.pi/2
angle2 = math.pi/2
angle_velocity1 = 0
angle_velocity2 = 0
angle_acceleration1 = 0
angle_acceleration2 = 0
Gravity = 8
scatter1 = []
scatter2 = []

LIST_LIMIT = 100

#COLORS
BACKGROUND = (20, 20, 20)
SCATTERLINE1 = (255, 255, 255)
SCATTERLINE2 = (255, 255, 0)
MAINPOINT = (0, 255, 0)
SMALLPOINT = (0, 255, 255)
PENDULUMARM = (45, 140, 245)
ARMSTROKE = 10

starting_point = (width//2 , height//3 )

x_offset = starting_point[0]
y_offset = starting_point[1]

run = True

while run:
    clock.tick(fps)

    screen.fill(BACKGROUND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    # calculate the acceleration
    angle_acceleration1 = formular.FirstAcceleration(angle1, angle2, mass1, mass2, length1, length2, Gravity, angle_velocity1, angle_velocity2)
    angle_acceleration2 = formular.SecondAcceleration(angle1, angle2, mass1, mass2, length1, length2, Gravity, angle_velocity1, angle_velocity2)

    x1 = float(length1 * math.sin(angle1)+x_offset)
    y1 = float(length1 * math.cos(angle1)+y_offset)

    x2 = float(x1 + length2 * math.sin(angle2))
    y2 = float(y1 + length2 * math.cos(angle2))

    # the angle varies with respect to the velocity and the velocity with respect to the acceleration
    angle_velocity1 += angle_acceleration1
    angle_velocity2 += angle_acceleration2
    angle1 += angle_velocity1
    angle2 += angle_velocity2

    scatter1.insert(0, (x1, y1))
    scatter2.insert(0, (x2, y2))
    #scatter1.append((x1, y1))
    #scatter2.append((x2, y2))


    for point in scatter2:
        random_color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        plot = Points(point[0], point[1], screen, SCATTERLINE1, scatter2)
        plot.draw()

    if len(scatter1) > LIST_LIMIT:
        scatter1.pop()
    if len(scatter2) > LIST_LIMIT:
        scatter2.pop()

    pygame.draw.line(screen, PENDULUMARM, starting_point, (x1, y1), ARMSTROKE)
    pygame.draw.circle(screen, SMALLPOINT, starting_point, 8)

    if len(scatter1) > 1:
        pygame.draw.lines(screen, SCATTERLINE2, False, scatter1, 1)

    pygame.draw.line(screen, PENDULUMARM, (x1, y1), (x2, y2), ARMSTROKE)

    pygame.draw.circle(screen, SMALLPOINT, (int(x2), int(y2)), 10)
    pygame.draw.circle(screen, MAINPOINT, (int(x1), int(y1)), 20)

    pygame.display.update()

pygame.quit()
