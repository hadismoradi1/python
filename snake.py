import pygame
import sys
import random

# ---------- تنظیمات ----------
WIDTH, HEIGHT = 600, 400
TILE = 20  # اندازه هر خانه
FPS_START = 10  # سرعت اولیه
FONT_NAME = "arial"

# رنگ‌ها (RGB)
BLACK = (20, 20, 20)
WHITE = (240, 240, 240)
GREEN = (0, 200, 90)
RED = (230, 60, 60)
GRID = (35, 35, 35)
YELLOW = (250, 210, 60)

# ---------- توابع کمکی ----------
def draw_grid(surf):
    for x in range(0, WIDTH, TILE):
        pygame.draw.line(surf, GRID, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE):
        pygame.draw.line(surf, GRID, (0, y), (WIDTH, y))

def new_food(snake):
    while True:
        fx = random.randrange(0, WIDTH // TILE) * TILE
        fy = random.randrange(0, HEIGHT // TILE) * TILE
        if (fx, fy) not in snake:
            return (fx, fy)

def draw_text(surf, text, size, color, center):
    font = pygame.font.SysFont(FONT_NAME, size)
    img = font.render(text, True, color)
    rect = img.get_rect(center=center)
    surf.blit(img, rect)

# ---------- بازی ----------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake 🐍")
    clock = pygame.time.Clock()

    def reset():
        snake = [(WIDTH//2, HEIGHT//2),
                 (WIDTH//2 - TILE, HEIGHT//2),
                 (WIDTH//2 - 2*TILE, HEIGHT//2)]
        direction = (TILE, 0)  # حرکت به راست
        food = new_food(snake)
        score = 0
        fps = FPS_START
        return snake, direction, food, score, fps

    snake, direction, food, score, fps = reset()
    game_over = False

    while True:
        # رویدادها
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if game_over and event.key in (pygame.K_r, pygame.K_RETURN):
                    snake, direction, food, score, fps = reset()
                    game_over = False
                # کنترل‌ها
                if not game_over:
                    if event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-TILE, 0):
                        direction = (TILE, 0)
                    elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (TILE, 0):
                        direction = (-TILE, 0)
                    elif event.key in (pygame.K_UP, pygame.K_w) and direction != (0, TILE):
                        direction = (0, -TILE)
                    elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -TILE):
                        direction = (0, TILE)

        screen.fill(BLACK)
        draw_grid(screen)

        if not game_over:
            # حرکت مار
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)

            # برخورد با دیوار
            if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
                game_over = True
            # برخورد با خودش
            elif new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                # خوردن غذا
                if new_head == food:
                    score += 1
                    food = new_food(snake)
                    fps = min(25, FPS_START + score // 2)  # کم‌کم سریع‌تر
                else:
                    snake.pop()

        # رسم غذا
        pygame.draw.rect(screen, RED, (*food, TILE, TILE))

        # رسم مار
        for i, (x, y) in enumerate(snake):
            color = GREEN if i == 0 else (0, 170, 80)
            pygame.draw.rect(screen, color, (x, y, TILE, TILE))
            pygame.draw.rect(screen, BLACK, (x, y, TILE, TILE), 1)

        # امتیاز
        draw_text(screen, f"Score: {score}", 22, YELLOW, (60, 18))

        if game_over:
            draw_text(screen, "Game Over!", 48, WHITE, (WIDTH//2, HEIGHT//2 - 20))
            draw_text(screen, "Press R to Restart  |  ESC to Quit", 24, WHITE, (WIDTH//2, HEIGHT//2 + 20))

        pygame.display.flip()
        clock.tick(fps)
if __name__ == "__main__":
    main()