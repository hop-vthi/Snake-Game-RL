from typing import Optional
import numpy as np
import gymnasium as gym
from snake import Snake

class SnakeBoardEnv(gym.Env):
    def __init__(self, snake : Snake, size, seed):
        self.size = size
        self.snake: Snake = snake # type annotate
        self.apple_location = self.random_apple()
        self.seed = seed
        self.action_space = gym.spaces.Discrete(3);
        self.observation_space = gym.spaces.MultiDiscrete([2, 2, 2, 2, 2, 4]) # check below

    def _get_obs(self):
        df_forward, df_left, df_right = self.snake.check_danger_flag()
        # observation order
        # relative position between apple and snake head (x axis)
        # relative position between apple and snake head (y axis)
        # danger ahead flag
        # danger left flag
        # danger right flag
        # snake head direction 
        return np.array([
            True if self.apple_location[0] > self.snake.body[0][0] else False, 
            True if self.apple_location[1] > self.snake.body[0][1] else False,
            df_forward,
            df_left,
            df_right,
            self.snake.direction
        ])

    # action must be either 0, 1 or 2 
    def step(self, action):
        # new position of snake
        new_position, _ = self.snake.movement(action)

        # If snake reached apple then
        # Informs the snake that it has eaten an apple
        # Give it a good reward
        # Generate new apple location
        if new_position[0] == self.apple_location[0] and new_position[1] == self.apple_location[1]:
            self.snake.check_apple(True)
            reward = 10
            self.apple_location = self.random_apple()
            observation = self._get_obs();
            return (observation, reward, False, False, {})
        # If the snake collided with its body or it goes out of bound
        # Give it bad reward
        # Terminate the game
        elif self.snake.is_collision(new_position[0], new_position[1]) or self.out_of_bounds(new_position):
            reward = -5
            return ([], reward, True, False, {})
        # Nothing special happened, snake continue to live 
        # No reward
        # Informs the snake that it didn't eat an apple
        else:
            reward = 0
            self.snake.check_apple(False)
            observation = self._get_obs();
            return (observation, reward, False, False, {})

    def reset(self, *, seed: Optional[int] = None, options: Optional[dict] = None):
        super().reset(seed=seed)

        # Randomly place the snake get snake head is enough
        self.snake.reset()

        # Randomly place target, ensuring it's different from agent position
        self.apple_location = self.random_apple()

        # get initial observation
        observation = self._get_obs()

        return (observation, {})


    # Random position of apple (Require: No collide with snake's position)
    def random_apple(self):
        apple_position = np.random.randint(0, 15, 2)
        while (True):
            for body in self.snake.body:
                flag = False
                if body[0] == apple_position[0] and body[1] == apple_position[1]:
                    flag = True
                if flag == False:
                    return apple_position
            apple_position = np.random.randint(0, 15, 2)

    # check if the snake is out of bound
    def out_of_bounds(self, new_position):
        return new_position[0] < 0 or new_position[0] > 14 or new_position[1] < 0 or new_position[1] > 14
