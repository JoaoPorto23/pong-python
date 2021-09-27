import pygame, sys

#Setup geral
pygame.init()
clock = pygame.time.Clock()

#Set do tamanho da tela do Pong
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')