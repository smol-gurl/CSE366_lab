from agent import Agent
from environment import Environment
def main():
    # Create an environment with dimensions 10x10
    env = Environment(width=10, height=10)
    env.display()
    # Create an agent within the environment
    agent = Agent(name="Agent A", environment=env)
    agent.status()
    # Simulate agent movement
    movements = ["up", "up", "right", "down", "left", "left", "up", "right"]

    for move in movements:
        print(f"Moving {move}...")
        agent.move(move)
        agent.status()