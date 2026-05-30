import pygame
import random

pygame.init()

W = 600                                      
screen = pygame.display.set_mode((W, W)) 
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

CELL = 20  
SPEED = 10

BG_COLOR     = (20, 20, 20)
SNAKE_COLOR  = (0, 200, 80)
HEAD_COLOR   = (0, 255, 120)
FOOD_COLOR   = (230, 33, 33)


def random_food():
    '''Return a random (x, y) position aligned to the grid.'''
    x = random.randrange(0, W, CELL)
    y = random.randrange(0, W, CELL)
    return (x, y)

#  Initial game state
snake = [(200, 200)]
direction = (CELL, 0)
food = random_food()

score = 0
font = pygame.font.SysFont("monospace", 18)

running = True

#  Main game loop
while running:
    clock.tick(SPEED)
    # ────────── 1. Handle events ─────────────────
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Change direction based on arrow keys
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            if event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, +CELL)
            if event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            if event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (+CELL, 0)

    # ────── 2. Move the snake ─────────  New head position = old head + current direction
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    # ────── 3. Check food collision ──────────
    if head == food:
        score += 1   
        food = random_food()
        
    else:
        snake.pop()

    # ─────── 4. Collision detection ───────────
    
    if (head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= W):
        running = False

    if head in snake[1:]:
        running = False

    # ──────── 5. Draw everything ────────────
    screen.fill(BG_COLOR)

    # Draw each body segment
    for i, segment in enumerate(snake):
        color = HEAD_COLOR if i == 0 else SNAKE_COLOR
        pygame.draw.rect(screen, color,(*segment, CELL - 1, CELL-1))

    # Draw food
    pygame.draw.rect(screen, FOOD_COLOR, (*food, CELL - 1, CELL - 1))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (220, 220, 220))
    screen.blit(score_text, (8, 8))

    pygame.display.flip()

#  Game over screen
screen.fill(BG_COLOR)
over_font  = pygame.font.SysFont("monospace", 32, bold=True)
small_font = pygame.font.SysFont("monospace", 20)

over_text  = over_font.render("GAME OVER", True, (255, 60, 60))
score_text = small_font.render(f"Final Score: {score}", True, (220, 220, 220))
quit_text  = small_font.render("Press any key to quit", True, (140, 140, 140))

screen.blit(over_text,  (W // 2 - over_text.get_width()  // 2, W // 2 - 60))
screen.blit(score_text, (W // 2 - score_text.get_width() // 2, W // 2))
screen.blit(quit_text,  (W // 2 - quit_text.get_width()  // 2, W // 2 + 40))
pygame.display.flip()



waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            waiting = False
pygame.quit()