import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the paddles' dimensions
paddle_width = 10
paddle_height = 100

# Create the paddles
player_paddle = pygame.Rect(0, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height)
computer_paddle = pygame.Rect(screen_width - paddle_width, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height)

# Define the ball's dimensions
ball_width = 10
ball_height = 10

# Create the ball
ball = pygame.Rect(screen_width / 2 - ball_width / 2, screen_height / 2 - ball_height / 2, ball_width, ball_height)

# Define the ball's movement
ball_speed_x = 5 * random.choice([1, -1])
ball_speed_y = 5 * random.choice([1, -1])

# Set up the clock for FPS
clock = pygame.time.Clock()

# Define the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= 5
    if keys[pygame.K_s] and player_paddle.bottom < screen_height:
        player_paddle.y += 5
    if keys[pygame.K_UP] and computer_paddle.top > 0:
        computer_paddle.y -= 5
    if keys[pygame.K_DOWN] and computer_paddle.bottom < screen_height:
        computer_paddle.y += 5

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for collisions with walls and paddles
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_speed_x *= -1
        ball = pygame.Rect(screen_width / 2 - ball_width / 2, screen_height / 2 - ball_height / 2, ball_width, ball_height)
    if ball.right >= screen_width:
        ball_speed_x *= -1
        ball = pygame.Rect(screen_width / 2 - ball_width / 2, screen_height / 2 - ball_height / 2, ball_width, ball_height)
    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        ball_speed_x *= -1

    # Draw the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, computer_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Update the screen
    pygame.display.flip()

    # Set FPS
    clock.tick(60)
