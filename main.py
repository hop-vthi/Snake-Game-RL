from tqdm import tqdm  # Progress bar
from env import SnakeBoardEnv
from snake import Snake
from SnakeAgent import SnakeAgent

<<<<<<< HEAD

# Khởi tạo các hyperparameters
=======
# Training hyperparameters
learning_rate = 0.01        # How fast to learn (higher = faster but less stable)
n_episodes = 500000        # Number of hands to practice
start_epsilon = 1.0         # Start with 100% random actions
epsilon_decay = start_epsilon / (n_episodes / 2)  # Reduce exploration over time
final_epsilon = 0.1         # Always keep some exploration
>>>>>>> main

# Create environment and agent
env = SnakeBoardEnv()
agent = SnakeAgent()


for episode in tqdm(range(n_episodes)):
    # Start a new hand
    obs = env.reset()
    done = False

    while not done:
        # Agent chooses action (initially random, gradually more intelligent)
        action = agent.get_action(obs)

        # Take action and observe result
        next_obs, reward, terminated = env.step(action)

        # Learn from this experience
        agent.update(obs, action, reward, terminated, next_obs)

        # Move to next state
        done = terminated
        obs = next_obs

    # Reduce exploration rate (agent becomes less random over time)
    agent.decay_epsilon()