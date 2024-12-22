import pygame
import random
pygame.init()
r= 900
l = 700
screen = pygame.display.set_mode((r,l ))
pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/иконка3.png")
pygame.display.set_icon(icon)
target_image = pygame.image.load("img/result_тт.jpg")
nn = 40
tt = 40
target_x = random.randint(0, r-nn)
target_y = random.randint(0, l-tt)



color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x< target_x +nn and target_y <mouse_y <target_y + tt:
                target_x = random.randint(0, l - nn)
                target_y = random.randint(0, l - tt)

    screen.blit(target_image,(target_x, target_y))
    pygame.display.update()

pygame.quit()
