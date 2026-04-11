from typing import Optional
import numpy as np
import gymnasium as gym

class SnakeBoardEnv(gym.Env):
    def __init__(self, box_dimension, snake):
        self.box_dimension = box_dimension
        self.set_observation_space(box_dimension)  #create_observation_space (including position of snake, apple)
        self.snake = snake

    # Initialize positions - reset()

    # Define what the agent can observe
    def step(self, action):
        pass 
    def reset(self):
    def random_apple(self):
        # No collide with Snake



