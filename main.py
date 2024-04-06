import pygame as pg

# Init Game
pg.init()

# Set display

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
surface_display = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("~~Snake~~")

# Game speed
FPS = 60
clock = pg.time.Clock()

# Set game values
SNAKE_SIZE = 20

head_x = WINDOW_HEIGHT // 2
head_y = WINDOW_HEIGHT // 2

snake_dx = 0
snake_dy = 0

score = 0

# Set Colors

GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
RED = (255, 0, 0)
DARK_RED = (150, 0, 0)
WHITE = (255, 255, 255)

# Set fonts

font = pg.font.SysFont("gabriola", 48)

# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARK_GREEN)
title_rect = title_text.get_rect()
title_rect.center(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

score_text = font.render("Score: " + str(score), True, GREEN, DARK_RED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAME OVER", True, RED, DARK_GREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any key to play again", True, RED, DARK_GREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Set sounds and music
pick_up_sound = pg.mixer.Sound("pick_up_sound.wav")

# Set images
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pg.draw.rect(surface_display, RED, apple_coord)

head_cord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pg.draw.rect(surface_display, GREEN, head_cord)

body_coord = []

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
