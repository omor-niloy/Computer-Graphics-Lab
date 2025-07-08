import pygame
import time

pygame.init()


WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrolling Name")

font = pygame.font.SysFont("Arial", 100, bold=True)
name = "Omor Niloy"
text_color = (255, 255, 255)
bg_color = (0, 0, 0)

text_surface = font.render(name, True, text_color)
text_width = text_surface.get_width()
text_height = text_surface.get_height()
y = (HEIGHT - text_height) // 2

start_x = (WIDTH - text_width) // 2
x = start_x
y = (HEIGHT - text_surface.get_height()) // 2

screen.fill(bg_color)
screen.blit(text_surface, (x, y))
pygame.display.update()


clock = pygame.time.Clock()
speed, sleep_duration = 4, 1

running = True
rounds = 0
while running:
    if 0 <= start_x - x < 4:
        time.sleep(sleep_duration)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x -= speed
    if x + text_width < 0:
        x = WIDTH  
        rounds += 1
    screen.fill(bg_color)
    screen.blit(text_surface, (x, y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
