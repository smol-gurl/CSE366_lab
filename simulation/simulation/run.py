# run.py
import pygame
from agent import Agent
from environment import Environment

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agent-Environment Simulation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Environment and Agent
env = Environment(WIDTH, HEIGHT)
agent = Agent(x=WIDTH // 2, y=HEIGHT // 2, speed=5, environment=env)

# Font for displaying position
font = pygame.font.Font(None, 36)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key press
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -1
    elif keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    elif keys[pygame.K_DOWN]:
        dy = 1

    # Move the agent
    agent.move(dx, dy)

    # Fill screen and draw agent
    screen.fill(WHITE)
    agent_pos = agent.get_position()
    pygame.draw.circle(screen, BLUE, agent_pos, 10)

    # Display the agent's position
    position_text = font.render(f"Position: {agent_pos}", True, TEXT_COLOR)
    screen.blit(position_text,(10,10))

    position_text = font.render(f"Position: {agent_pos}", True, TEXT_COLOR)    
    pygame.draw.rect(AGENT_COLOR,(WINDOW_WIDTH //2, WINDOW_HEIGHT//2,30,30,30

    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
