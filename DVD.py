import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Logo Bouncer")
clock = pygame.time.Clock()

# DVD logo setup (rectangle or image) ended up drawing everything but you can run wild
logo_width, logo_height = 120, 60
x, y = random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)
vx, vy = 3, 3  # Velocity in the X and y directions
angle = 0
rotation_speed = 1

# Colors
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
]
current_color = random.choice(colors)   #We want to be picking these colors at random.


# Trail effect
trail = []
max_trail_length = 20

# Font for "DVD" text
font = pygame.font.SysFont('Arial', 24)

running = True
while running:
    clock.tick(60)  # Limit to 60 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:    
                # Change direction on space press
                vx = random.choice([-5, -4, -3, 3, 4, 5])
                vy = random.choice([-5, -4, -3, 3, 4, 5])

    # Move the logo by incrementing 
    x += vx
    y += vy
    angle += rotation_speed
    
    # Add current position to trail
    trail.append((x, y))
    if len(trail) > max_trail_length:
        trail.pop(0)

    # Bounce off walls with color change
    bounce = False
    if x <= 0 or x + logo_width >= WIDTH:
        vx *= -1
        bounce = True
    if y <= 0 or y + logo_height >= HEIGHT:
        vy *= -1
        bounce = True
    
    if bounce:
        current_color = random.choice(colors)
        rotation_speed = random.uniform(-2, 2)
        

    # Draw everything
    screen.fill((0, 0, 0))  # Black background of course
    
    # Draw trail
    for i, (tx, ty) in enumerate(trail):
        alpha = int(255 * (i / len(trail)))
        trail_color = (alpha, alpha, alpha)
        trail_rect = pygame.Rect(tx, ty, logo_width, logo_height)
        pygame.draw.rect(screen, trail_color, trail_rect, 1)
    
    # Draw the DVD logo
    logo_rect = pygame.Rect(x, y, logo_width, logo_height)
    pygame.draw.rect(screen, current_color, logo_rect)
        
    # Draw "DVD" text on the rectangle
    text = font.render("DVD", True, (0, 0, 0))
    text_rect = text.get_rect(center=logo_rect.center) 
    screen.blit(text, text_rect)
    
    pygame.display.flip()

pygame.quit()