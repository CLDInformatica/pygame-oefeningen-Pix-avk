'''
Gegeven zijn: een horror font dat "voetbal game" op het scherm zet en een plaatje van een bal.

We gaan de game aanpassen zodat het er beter uit ziet.

Doe het volgende:

  // - Download een toepasselijk font en maak hiermee een scoreboard
  - Download 2 plaatjes van voetballers en zet deze tegenover elkaar op het scherm
  // - Zet de bal in het midden van de scherm

Extra tijd:

  - Voeg 2 goals toe (links en rechts)
  - Voeg een toepasselijke achtergrond toe
  - Schrijf de namen van de spelers ergens op het scherm

Slides: https://docs.google.com/presentation/d/1c4C94q8OcMGCIFefVo18Xac4WIFJacq5Eutj1gY6rCg/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Voetbal game!')
clock = pygame.time.Clock()
running = True
test_font = pygame.font.Font("Opdrachten/PyGame/Les2/fonts/horror.ttf", 50)
font2 = pygame.font.Font("Opdrachten/PyGame/Les2/fonts/ka1.ttf", 20)


voetbal_surface = pygame.image.load("Opdrachten/PyGame/Les2/graphics/voetbal.png")
speler_surface1 = pygame.image.load("Opdrachten/PyGame/Les2/graphics/voetbal3.png")
tekst_surface = test_font.render("Voetbal game", False, "green")
tekst_surface2 = font2.render("0 // 1", False, "green")



while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(speler_surface1, (0, 20))
  screen.blit(tekst_surface, (280, 100))
  screen.blit(tekst_surface2, (350, 50))
  screen.blit(voetbal_surface, (355, 280))
  

  
  pygame.display.update()
  clock.tick(60)
