import pygame, sys

#Setup geral
pygame.init()
clock = pygame.time.Clock()

#Set do tamanho da tela do Pong
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#Retângulos do Pong
ball = pygame.Rect(screen_width/2-15, screen_height/2 - 15, 30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10/140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#Loop para fechar o tela
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)