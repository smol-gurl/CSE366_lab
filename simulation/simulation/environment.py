# environment.py

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def limit_position(self, x, y):
        # Ensures the agent remains within the environment's boundaries
        x = max(0, min(x, self.width))
        y = max(0, min(y, self.height))
        return x, y
