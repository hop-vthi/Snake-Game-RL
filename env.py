from typing import Optional
import numpy as np
import gymnasium as gym

class SnakeBoardEnv(gym.Env):
    def __init__(self, Snake, size: int = 15):
        self.size = size
        self.snake = Snake
        self.apple_location = self.random_apple()
        self.seed()

    def _get_obs(self):
        return (
            int(self.apple_location[0] > self.snake.head[0]),
            int(self.apple_location[0] < self.snake.head[0]),
            int(self.apple_location[1] > self.snake.head[1]),
            int(self.apple_location[1] < self.snake.head[1]),
            int(self.df_forward),
            int(self.df_left),
            int(self.df_right),
            self.direction
        )
    def step(self, action):
        # new position of snake
        new_position = self.snake.movement(action)

        # TODO Check if snake reached apple then
        # TODO Update snake
        # TODO Reward
        # TODO Random apple location
        # if self.snake.is_colliding(new_position) or self.out_of_bounds(new_position):


        # TODO Check if snakgit e died or collide with its body
        # TODO Reset snake?
        # TODO update Terminate = 1
        terminated = 0

        # Give reward if it;
        reward = 1 if terminated else 0

        observation = self._get_obs()

        return observation, reward, terminated
    def reset(self, seed: Optional[int] = None, options: Optional[dict] = None):
        super().reset(seed=seed)

        # Randomly place the snake get snake head is enough
        self.snake = self.snake.reset()

        # Randomly place target, ensuring it's different from agent position
        self.apple_location = ....

        observation = self._get_obs()

        return observation

    # Random position of apple (Require: No collide with snake's position)
    def random_apple(self):
        pass

    def out_of_bounds(self):
        pass