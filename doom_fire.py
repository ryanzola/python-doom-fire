import pygame as pg
from pygame import gfxdraw
from random import randint

WIN_SIZE = WIDTH, HEIGHT = 1600, 900
STEPS_BETWEEN_COLORS = 9
COLORS = ['black', 'red', 'orange', 'yellow', 'white']
PIXEL_SIZE = 4
FIRE_REPS = 4

class DoomFire:
  def __init__(self, app, width, height):
    self.app = app
    self.width, self.height = width, height
    self.fire_width = self.width // (PIXEL_SIZE * FIRE_REPS)
    self.fire_height = self.height // PIXEL_SIZE
    self.palette = self.get_palette()
    self.fire_array = self.get_fire_array()
    self.fire_surf = pg.Surface([PIXEL_SIZE * self.fire_width, self.height])
    self.fire_surf.set_colorkey('black')

    self.logo = pg.image.load('doom_logo.png').convert_alpha()
    self.logo = pg.transform.scale2x(self.logo)
    self.logo_x, self.logo_y = (width // 2 - self.logo.get_width() // 2, self.height // 3 - self.logo.get_height() // 2)
    self.logo_start_y = self.height

  def draw_logo(self):
    if self.logo_start_y > self.logo_y:
      self.logo_start_y -= 5
    self.app.screen.blit(self.logo, (self.logo_x, self.logo_start_y))

  def do_fire(self):
    for x in range(self.fire_width):
      for y in range(1, self.fire_height):
        color_index = self.fire_array[y][x]
        if color_index:
          rnd = randint(0, 3)
          self.fire_array[y - 1][(x - rnd + 1) % self.fire_width] = color_index - rnd % 2
        else:
          self.fire_array[y - 1][x] = 0

  def draw_fire(self):
    self.fire_surf.fill('black')
    for y, row in enumerate(self.fire_array):
      for x, color_index in enumerate(row):
        if color_index:
          color = self.palette[color_index]
          gfxdraw.box(self.fire_surf, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE), color)
    
    for i in range(FIRE_REPS):
      self.app.screen.blit(self.fire_surf, (self.fire_surf.get_width() * i, 0))

  def get_fire_array(self):
    fire_array = [[0 for i in range(self.fire_width)] for j in range(self.fire_height)]
    for i in range(self.fire_width):
      fire_array[self.fire_height - 1][i] = len(self.palette) - 1

    return fire_array

  def draw_palette(self):
    size = 90
    for i, color in enumerate(self.palette):
      pg.draw.rect(self.app.screen, color, (i * size, self.width // 2, size - 5, size - 5))

  @staticmethod
  def get_palette():
    palette = [(0, 0, 0)]
    for i, color in enumerate(COLORS[:-1]):
      c1, c2 = color, COLORS[i + 1]
      for step in range (STEPS_BETWEEN_COLORS):
        c = pg.Color(c1).lerp(c2, (step + 0.5) / STEPS_BETWEEN_COLORS)
        palette.append(c)
    return palette

  def update(self):
    self.do_fire()
  
  def draw(self):
    # self.draw_palette()
    self.draw_logo()
    self.draw_fire()