# agent.py
import pygame

class Agent:
    def __init__(self, x, y, speed, environment):
        self.x = x
        self.y = y
        self.speed = speed
        self.environment = environment  # Link to the environment

    def move(self, dx, dy):
        # Increase speed each time the agent moves
        if dx != 0 or dy != 0:  # Only increase speed if there's movement
            self.speed += 0.1  # Increment speed by a small amount

        # Calculate new position based on direction and current speed
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed

        # Constrain the position within the environment's boundaries
        self.x = max(0, min(new_x, self.environment.width - 20))  # Adjust for rectangle width
        self.y = max(0, min(new_y, self.environment.height - 20))  # Adjust for rectangle height

    def get_position(self):
        return int(self.x), int(self.y)
