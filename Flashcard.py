from turtle import left
import pygame, sys
#handles music

pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

#Title and Icon change (flaticon.com has icons available)
pygame.display.set_caption("MEGA Vocabulary Flashcards")
icon = pygame.image.load("cardbackfinal.png")
pygame.display.set_icon(icon)

#background
background = pygame.image.load("bglogo.png")

def vocab_set

running = True
while running:
    #background screen color - rgb site: https://www.w3schools.com/colors/colors_rgb.asp
    screen.fill((120,10,0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()