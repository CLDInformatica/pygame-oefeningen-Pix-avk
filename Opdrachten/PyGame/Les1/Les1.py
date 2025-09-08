'''
Maak het plaatje dat in dit mapje staat na.

Slides: 
https://docs.google.com/presentation/d/1YwoUdeWABUYJkSfNzzZzDbCKvCVmWoo9Z5Uu7f_Y_K4/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Eerste game!')
clock = pygame.time.Clock()
running = True

surface = pygame.Surface((800, 400))
surface.fill("blue")

y1 = pygame.Surface((30, 30))
y1.fill("yellow")

g1 = pygame.Surface((50, 190))
g1.fill("green")

g2 = pygame.Surface((50, 100))
g2.fill("green")

g3 = pygame.Surface((50, 70))
g3.fill("green")

g4 = pygame.Surface((50, 300))
g4.fill("green")

g5 = pygame.Surface((50, 270))
g5.fill("green")

g6 = pygame.Surface((50, 70))
g6.fill("green")

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(surface, (0, 0))
  screen.blit(y1, (80, 200))
  screen.blit(g1, (220, 0))
  screen.blit(g2, (220, 320))
  screen.blit(g3, (400, 0))
  screen.blit(g4, (400, 160))
  screen.blit(g5, (580, 0))
  screen.blit(g6, (580, 340))

  pygame.display.update()
  clock.tick(60)

