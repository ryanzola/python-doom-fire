import pygame as pg
import sys
from doom_fire import DoomFire

WIN_SIZE = WIDTH, HEIGHT = 1600, 900
STEPS_BETWEEN_COLORS = 9
COLORS = ['black', 'red', 'orange', 'yellow', 'white']
PIXEL_SIZE = 4
FIRE_REPS = 4
FIRE_WIDTH = WIDTH // (PIXEL_SIZE * FIRE_REPS)
FIRE_HEIGHT = HEIGHT // PIXEL_SIZE


class App:
    def __init__(self):
        pg.init()
        info = pg.display.Info()
        width, height = info.current_w, info.current_h
        self.screen = pg.display.set_mode((width, height), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.doom_fire = DoomFire(self, width, height)

    def update(self):
        self.doom_fire.update()
        self.clock.tick(60)
        pg.display.set_caption(f'{ self.clock.get_fps():.1f}')

    def draw(self):
        self.screen.fill('black')
        self.doom_fire.draw()
        pg.display.flip()

    def run(self):
      while True:
        for event in pg.event.get():
          if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
        self.update()
        self.draw()

if __name__ == '__main__':
    app = App()
    app.run()