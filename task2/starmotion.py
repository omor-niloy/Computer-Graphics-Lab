import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Growing Star Animation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 255)

# Star settings
center = (WIDTH // 2, HEIGHT // 2)
max_size = 200  # max size before reset
growth_rate = 1  # how fast the star grows
size = 1  # initial size

def draw_star(surface, center, size, color):
    """Draw a simple 5-pointed star centered at `center` with radius `size`."""
    points = []
    for i in range(10):
        angle = i * (2 * math.pi / 10)
        radius = size if i % 2 == 0 else size / 2
        x = center[0] + radius * math.cos(angle - math.pi / 2)
        y = center[1] + radius * math.sin(angle - math.pi / 2)
        points.append((x, y))
    pygame.draw.polygon(surface, color, points)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Draw the growing star
    draw_star(screen, center, size, YELLOW)
    size += growth_rate

    # Reset when star reaches max size
    if size > max_size:
        size = 1

    pygame.display.flip()
    clock.tick(30)
