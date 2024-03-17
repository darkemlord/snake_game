import pygame as pg

# Init Game
pg.init()

# Set display

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
surface_display = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("snake game")
# Game speed
FPS = 60
clock = pg.time.Clock()

# Main loop
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # update Display
    pg.display.update()

    clock.tick(FPS)
# End Game
pg.quit()
