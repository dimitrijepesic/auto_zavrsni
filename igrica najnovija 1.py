import pygame as pg
from math import sin, cos, radians
pg.init()
width = 1280
height = 720
surface = pg.display.set_mode((width, height))
surface_rect = surface.get_rect()
pg.display.set_caption('igrica')
surface.fill(pg.Color('black'))
pg.display.update()
x = 640
y = 360
brzina = 0
ugaona_brzina = 0
ugao = 0
delta_t = 0
def ulaz(event):
  global brzina, ugaona_brzina
  if event.type == pg.KEYDOWN:
    if event.key == pg.K_UP:
      brzina = -500
    elif event.key == pg.K_DOWN:
      brzina = 500
    elif event.key == pg.K_LEFT:
      ugaona_brzina = -400
    elif event.key == pg.K_RIGHT:
      ugaona_brzina = 400
  elif event.type == pg.KEYUP:
    brzina = 0
    ugaona_brzina = 0
  return brzina, ugaona_brzina
def nacrtaj_auto(x, y, ugao):
  surface.fill(pg.Color('black'))
  slika = pg.image.load('car.png')
  slika1 = pg.transform.rotate(slika, ugao)
  rect = slika1.get_rect()
  rect.center = slika1.center
  surface.blit(slika1, rect.center)
  return
def fizika(x, y, ugao, brzina, ugaona_brzina, delta_t):
  x_novo = x + int(brzina*delta_t*sin(ugao))
  y_novo = y + int(brzina*delta_t*cos(ugao))
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
        brzina, ugaona_brzina = ulaz(event)
  delta_t = sat.get_time() / 1000
  x, y, ugao = fizika(x,y,ugao, brzina, ugaona_brzina, delta_t)
  nacrtaj_auto(x,y,ugao)
  pg.display.update()
