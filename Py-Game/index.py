import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 60
PLAYER_SPEED = 5

# Platform settings
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 10

# Coin settings
COIN_SIZE = 15

# Set the display size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("High-Tech Platformer Game")

# Load assets
player_image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_image.fill(BLUE)

coin_image = pygame.Surface((COIN_SIZE, COIN_SIZE))
coin_image.fill(GREEN)

# Font for the score
font = pygame.font.SysFont('Arial', 25)

# Clock to control game speed
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
        self.change_x = 0
        self.change_y = 0
        self.jump_power = 10
        self.gravity = 0.5
        self.is_jumping = False

    def update(self):
        # Apply gravity
        self.change_y += self.gravity

        # Move left/right
        self.rect.x += self.change_x

        # Prevent player from going off-screen
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        # Check if player hits the ground
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.change_y = 0
            self.is_jumping = False

        # Move up/down (jump)
        self.rect.y += self.change_y

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.change_y = -self.jump_power

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create player
player = Player()

# Create platforms
platforms = pygame.sprite.Group()
for i in range(5):
    platform = Platform(random.randint(0, SCREEN_WIDTH - PLATFORM_WIDTH), random.randint(200, SCREEN_HEIGHT - 50))
    platforms.add(platform)

# Create coins
coins = pygame.sprite.Group()
for i in range(3):
    coin = Coin(random.randint(0, SCREEN_WIDTH - COIN_SIZE), random.randint(100, SCREEN_HEIGHT - 100))
    coins.add(coin)

# Add player to the sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(platforms)
all_sprites.add(coins)

# Main game loop
running = True
score = 0

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                player.change_x = PLAYER_SPEED
            if event.key == pygame.K_SPACE:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.change_x = 0
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.change_x = 0

    # Update the player and platform positions
    all_sprites.update()

    # Check for collisions with platforms
    platform_hits = pygame.sprite.spritecollide(player, platforms, False)
    if platform_hits and player.change_y > 0:
        player.rect.bottom = platform_hits[0].rect.top
        player.change_y = 0
        player.is_jumping = False

    # Check for collisions with coins
    coin_hits = pygame.sprite.spritecollide(player, coins, True)
    for coin in coin_hits:
        score += 10  # Increase score when collecting coins

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Render the score on the screen
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, [10, 10])

    # Refresh the screen
    pygame.display.flip()

    # Set frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
