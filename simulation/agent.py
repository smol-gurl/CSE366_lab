class Agent:
   def __init__(self, name, environment):
        self.name = name
        self.environment = environment
        self.position = [0, 0] # Initial position of the agent (x, y)
   def move(self, direction):
"""Move the agent in the specified direction."""
        if direction == "up":
          self.position[1] += 1
        elif direction == "down":
          self.position[1] -= 1
        elif direction == "left":
          self.position[0] -= 1
        elif direction == "right":
          self.position[0] += 1
# Make sure the agent stays within the environment boundaries
       self.position = self.environment.limit_position(self.position)
def status(self):
"""Print the current status of the agent."""
print(f"{self.name} is at position {self.position}.")