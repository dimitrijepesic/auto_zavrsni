import pygame as pg
from math import sin, cos, radians
import sys
import pygame.sprite as sprite
theClock = pg.time.Clock()
pg.init()
background = pg.image.load('images.png')
background_size = background.get_size()
surface = pg.display.set_mode(background_size)
running = True
width = 1280
height = 720
x1 = 0
y1 = 0
x2 = -width
y2 = 0
surface_rect = surface.get_rect()
pg.display.set_caption('igrica')
pg.display.update()
x = 640
y = 360
brzina = 0
ugaona_brzina = 0
ugao = 0
delta_t = 0
staro_stanje = [False, False, False, False]
def unos(event, staro_stanje):
  novo_stanje = staro_stanje
  if event.type == pg.KEYDOWN:
    if event.key == pg.K_UP:
      novo_stanje[0]=True
    if event.key == pg.K_DOWN:
      novo_stanje[1]=True
    if event.key == pg.K_LEFT:
      novo_stanje[2]=True
    if event.key == pg.K_RIGHT:
      novo_stanje[3]=True
  elif event.type == pg.KEYUP:
    if event.key == pg.K_UP:
      novo_stanje[0]=False
    if event.key == pg.K_DOWN:
      novo_stanje[1]=False
    if event.key == pg.K_LEFT:
      novo_stanje[2]=False
    if event.key == pg.K_RIGHT:
      novo_stanje[3]=False
  return novo_stanje
def brzinaa(novo_stanje):
  brzina = 0
  ugaona_brzina = 0
  if novo_stanje[0] == True:
    brzina = -300
  elif novo_stanje[1] == True:
    brzina = 300
  elif novo_stanje[0]==novo_stanje[1]:
    brzina = 0
  if novo_stanje[2] == True:
    ugaona_brzina = 50
  elif novo_stanje[3] == True:
    ugaona_brzina = -50
  elif novo_stanje[2]==novo_stanje[3]:
    ugaona_brzina = 0
  return brzina, ugaona_brzina
def nacrtaj_auto(x, y, ugao):
  slika = pg.image.load('car.png')
  slika1 = pg.transform.rotate(slika, ugao)
  rect = slika1.get_rect(center=slika.get_rect(topleft=(x, y)).center)
  surface.blit(slika1, rect.topleft)
  return
def fizika(x, y, ugao, brzina, ugaona_brzina, delta_t):
  x_novo = x + int(brzina*delta_t*sin(radians(ugao)))
  y_novo = y + int(brzina*delta_t*cos(radians(ugao)))
  ugao_novi = ugao + (ugaona_brzina*delta_t)
  return x_novo, y_novo, ugao_novi
nacrtaj_auto(x,y,ugao)
sat = pg.time.Clock()
x, y, ugao = fizika(x, y, ugao, brzina, ugaona_brzina, delta_t)
while True:
  otkucaji = 60
  sat.tick(otkucaji)
  for event in pg.event.get():
      if event.type == pg.QUIT:
          pg.quit()
      else:
        staro_stanje = unos(event, staro_stanje)
        brzina, ugaona_brzina = brzinaa(staro_stanje)
  slikaa = pg.image.load('images.png').convert()
  background_rect = slikaa.get_rect()
  surface.blit(slikaa, background_rect)
  x2+=5
  x1+=5
  surface.blit(slikaa,(x1,y1))
  surface.blit(slikaa,(x2,y2))
  if x1>width:
    x1 = -width
  if x2>width:
    x2 = -width
  theClock.tick(10)
  delta_t = (sat.get_time() / 1000) - delta_t
  x, y, ugao = fizika(x,y,ugao, brzina, ugaona_brzina, delta_t)
  nacrtaj_auto(x,y,ugao)
  pg.display.update()
