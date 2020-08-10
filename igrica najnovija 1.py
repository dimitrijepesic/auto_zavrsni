import pygame as pg
from math import sin, cos, radians
pg.init()
width = 1280
height = 720
surface = pg.display.set_mode((width, height))
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
  brzina = 0
  ugaona_brzina = 0
  for event in pg.event.get():
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_UP or event.key == pg.K_DOWN:
            brzina = 5
            ugaona_brzina = 0
          elif event.key == pg.K_LEFT:
            brzina = 0
            ugaona_brzina = 4
          elif event.key == pg.K_RIGHT:
            brzina = 0
            ugaona_brzina = -4
        elif event.type == pg.KEYUP:
          brzina = 0
          ugaona_brzina = 0
  return brzina, ugaona_brzina

def nacrtaj_auto(x, y, ugao):
  slika = pg.image.load('car.png')
  slika1 = pg.transform.rotate(slika, ugao)
  surface.blit(slika1, (x,y))
  return
def fizika(x, y, ugao, brzina, ugaona_brzina, delta_t):
  x_novo = x + (brzina*delta_t*sin(ugao))
  y_novo = y + (brzina*delta_t*cos(ugao))
  ugao_novi = ugao + (ugaona_brzina*delta_t)
  return x_novo, y_novo, ugao_novi
nacrtaj_auto(x,y,ugao)
x, y, ugao = fizika(x, y, ugao, brzina, ugaona_brzina, delta_t)
while True:
  sat = pg.time.Clock()
  otkucaji = 60
  for event in [pg.event.wait()] + pg.event.get():
      if event.type == pg.QUIT:
          pg.quit()
      else:
          delta_t = sat.get_time() / 1000
          brzina, ugaona_brzina = ulaz(event)
          x, y, ugao = fizika(x,y,ugao, brzina, ugaona_brzina, delta_t)
          nacrtaj_auto(x,y,ugao)
          sat.tick(otkucaji)
  pg.display.update()
