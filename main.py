import pygame as pg, random

# Init Game
pg.init()

# Set display

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
surface_display = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("~~Snake~~")

# Game speed
FPS = 40
clock = pg.time.Clock()

# Set game values
SNAKE_SIZE = 20

head_x = WINDOW_HEIGHT // 2
head_y = WINDOW_HEIGHT // 2 + 100

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
title_text = font.render("~~Snake~~", True, GREEN, DARK_RED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

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
    # Check if the user wants to quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Move the snake
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pg.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pg.K_UP:
                snake_dx = 0
                snake_dy = -1 * SNAKE_SIZE
            if event.key == pg.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    # Update x, y position of the snakes head and make a new coordinate
    head_x += snake_dx
    head_y += snake_dy
    head_cord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    # Check for collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()

        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

    # Fill the surface
    surface_display.fill(WHITE)

    # Blit the HUD
    surface_display.blit(title_text, title_rect)
    surface_display.blit(score_text, score_rect)

    # Blit assets

    head_rect = pg.draw.rect(surface_display, DARK_GREEN, head_cord)
    apple_rect = pg.draw.rect(surface_display, RED, apple_coord)

    # Update Display and tick clock
    pg.display.update()
    clock.tick(FPS)

    clock.tick(FPS)
# End Game
pg.quit()
