from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import sys
import random
#import asyncio
import pygame as pg

# Initialize Pygame and sound
pg.mixer.init()
level_1 = pg.mixer.Sound('track1.mp3')
bullet_sound = pg.mixer.Sound('effect1.mp3')
game_over_effect=pg.mixer.Sound("effect2.mp3")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
WIDTH, HEIGHT = 800, 800
FPS = 60

pg.init()

# Game setup
fps_clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("You Are Your Own Enemy")

# Load assets
img = pg.image.load("Character.png")
enemy1_img = pg.image.load("Enemy.png")
enemy2_img = pg.image.load("Enemy2.png")
bullet_img = pg.image.load("Bullet.png")
background = pg.image.load("Background.png")

# Movement and positioning
move = 50
x, y = 400, 400  # Initial player position
speed = 10
count = 0

# Bullets and enemies
bullets = []  # List of active bullets
enemy_x, enemy_y = random.randint(100, 700), random.randint(100, 700)  # Random enemy position
enemies = [enemy1_img, enemy2_img]

# Timer setup
countdown_time = 30  # Countdown time in seconds
start_ticks = pg.time.get_ticks()  # Get the initial ticks

# Font for text
text_font = pg.font.SysFont("Arial", 30)

# HealthBar class
class HealthBar:
    def __init__(self, width, height, max_hp):
        self.width = width
        self.height = height
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.x = 0  # Default x-coordinate
        self.y = 0  # Default y-coordinate

    def update_position(self, x, y):
        self.x = x
        self.y = y - 20  # Position above the enemy

    def draw(self, surface):
        ratio = self.current_hp / self.max_hp
        pg.draw.rect(surface, "red", (self.x, self.y, self.width, self.height))
        pg.draw.rect(surface, "green", (self.x, self.y, self.width * ratio, self.height))

    def reduce_health(self, amount):
        self.current_hp -= amount
        self.current_hp = max(0, self.current_hp)

# Instantiate the health bar
enemy_health_bar = HealthBar(100, 10, 100)

# Functions
def draw_player(x, y):
    screen.blit(img, (x, y))

def draw_text(text, font, text_col, x, y):
    rendered_text = font.render(text, True, text_col)
    screen.blit(rendered_text, (x, y))

def draw_enemy(x, y):
    screen.blit(enemies[random.randint(0, 1)], (x, y))

def draw_bullets():
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))

def move_bullets():
    global bullets
    for bullet in bullets[:]:  # Iterate over a copy of the list
        bullet[0] -= speed  # Move bullet left
        if bullet[0] < 0:  # Remove bullet if off-screen
            bullets.remove(bullet)

def check_collision():
    global enemy_x, enemy_y, bullets, count, enemy_health_bar
    enemy_rect = pg.Rect(enemy_x, enemy_y, 100, 100)  # Enemy rectangle
    for bullet in bullets[:]:  # Iterate over bullets
        bullet_rect = pg.Rect(bullet[0], bullet[1], bullet_img.get_width(), bullet_img.get_height())  # Bullet rectangle
        if bullet_rect.colliderect(enemy_rect):  # Check collision
            bullets.remove(bullet)  # Remove the bullet
            enemy_health_bar.reduce_health(10)  # Reduce health
            if enemy_health_bar.current_hp == 0:  # If health is zero
                enemy_x = random.randint(100, 600)  # Move enemy to a new position
                enemy_y = random.randint(100, 600)
                enemy_health_bar.current_hp = enemy_health_bar.max_hp  # Reset health
                count += 1
#global game_over, x, y
game_over=False
level_1.play(fade_ms=2000)


# Main game loop
#async def main():

while True:
    screen.blit(background, (0, 0))

    # Calculate remaining time
    elapsed_ticks = pg.time.get_ticks() - start_ticks
    remaining_time = max(0, countdown_time - elapsed_ticks // 1000)  # Convert ms to seconds and subtract

    # Draw the score, timer
    draw_text(f"Score: {count}", text_font, "white", 100, 100)
    draw_text(f"Time Left: {remaining_time}", text_font, "white", 100, 60)

    # Update health bar position and draw


    # Check if time is up
    if remaining_time == 0:
        game_over = True  # Trigger game over
        draw_text("GAME OVER!", text_font, "white", WIDTH // 2 - 100, HEIGHT // 2)
        pg.display.flip()
        pg.time.delay(3000)
        pg.quit()
        sys.exit()

    if not game_over:
        # Draw the score and timer
        draw_text(f"Score: {count}", text_font, "white", 100, 10)
        draw_text(f"Time Left: {remaining_time}", text_font, "white", 100, 60)
        enemy_health_bar.update_position(enemy_x, enemy_y)
        enemy_health_bar.draw(screen)

    # Event handling
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and y > 50:
                y -= move
            elif event.key == pg.K_DOWN and y < HEIGHT - 150:
                y += move
            elif event.key == pg.K_LEFT and x > 0:
                x -= move
            elif event.key == pg.K_RIGHT and x < WIDTH - 100:
                x += move
            elif event.key == pg.K_SPACE:  # Fire bullet
                bullets.append([x + 20, y + 50])  # Add new bullet
                bullet_sound.play()

    # Update game objects
    move_bullets()
    check_collision()

    # Draw game objects
    draw_player(x, y)
    draw_enemy(enemy_x, enemy_y)
    draw_bullets()

    # Display update
    pg.display.flip()
    fps_clock.tick(FPS)
        #await asyncio.sleep(0)
        

#asyncio.run(main())
