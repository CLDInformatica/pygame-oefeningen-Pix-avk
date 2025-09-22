'''
Gegeven is een oefenprogramma. Beantwoord de volgende vragen:

  - Wat gebeurt er als je met je muis over het stukje tekst heen gaat?
      het print "collision"
  - Wat gebeurt er als je op het stukje tekst klikt?
      het print "tekst ingedrukt"
  - Wat gebeurt er als je het stukje tekst loslaat na inklikken?
      het print "tekst losgelaten"
  - Wat gebeurt er als je je muis stil laat staan op het stukje tekst? (MOUSEMOTION)
      het print herhaardelijk "collision"


Doe nu zelf het volgende:

  // - Verwijder de prints, deze maken je programma traag
  // - Zorg dat het stukje tekst telkens een klein stukje naar rechts verschuift als je erop klikt
  // - Maak een nieuwe tekst surface met de tekst: Gewonnen!
  // - Als het stukje tekst de rechterkant van het scherm haalt blit dan dit nieuwe stukje tekst "Gewonnen!" naar het scherm
  // - Je hebt nu je eerste speelbare mini-game gemaakt!

EXTRA:

Maak het spel leuker door mooie achtergronden en plaatjes te gebruiken. Zo wordt het een echt spel!

Slides: https://docs.google.com/presentation/d/1tnd7la5uNy5jzyHuBGmD2M-jPWfoy2RBY6XqtKHJ1zY/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Rects en de muis')
test_font = pygame.font.Font(None, 50)
testfont2 = pygame.font.Font(None, 25)

clock = pygame.time.Clock()

background_surface = pygame.Surface((400, 300))
background_surface.fill("white")

tekst_surface = test_font.render("Stukje tekst!", False, "green")
tekst_rect = tekst_surface.get_rect(center = (200, 150))

tekstsur2 = test_font.render("Gewonnen!", False, "green")
tekstrect2 = tekstsur2.get_rect(center = (200, 400))

tekstsur3 = testfont2.render("Opnieuw", False, "grey")
tekstrect3 = tekstsur2.get_rect(center = (260, 400))



while True:
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
      
    if event.type == pygame.MOUSEBUTTONDOWN:
      if tekst_rect.collidepoint(event.pos):
        tekst_rect.right += 5

    if tekst_rect.left == 400:
      tekstrect2.center = 200, 150
      tekstrect3.center = 260, 200

    if event.type == pygame.MOUSEBUTTONDOWN:
      if tekstrect3.collidepoint(event.pos):
        tekst_rect.center = 200, 150
        tekstrect2.center = 200, 400
        tekstrect3.center = 260, 400

  screen.blit(background_surface, (0, 0))
  screen.blit(tekstsur2, tekstrect2)
  screen.blit(tekst_surface, tekst_rect)
  screen.blit(tekstsur3, tekstrect3)
  
  

  pygame.display.update()
  clock.tick(60)