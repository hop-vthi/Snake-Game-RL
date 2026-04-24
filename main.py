from tqdm import tqdm  # Progress bar
from env import SnakeBoardEnv
from snake import Snake
from SnakeAgent import SnakeAgent
from gymnasium.wrappers.vector import RecordEpisodeStatistics
# Training hyperparameters
learning_rate = 0.01        # How fast to learn (higher = faster but less stable)
# n_episodes = 500000        # Number of hands to practice
n_episodes = 500# Number of hands to practice
start_epsilon = 1.0         # Start with 100% random actions
epsilon_decay = start_epsilon / (n_episodes / 2)  # Reduce exploration over time
final_epsilon = 0.1         # Always keep some exploration

# Create environment and agent
snake = Snake()
env = SnakeBoardEnv(snake, 15, 42) #snake, size, seed
agent = SnakeAgent(env, learning_rate, start_epsilon, epsilon_decay, final_epsilon)

# env = RecordEpisodeStatistics(env) # custom env not applicable -mace

for episode in tqdm(range(n_episodes)):
    # Start a new hand
    obs, throwaway_empty_dict = env.reset() #add padding -mace
    done = False

    # shitass_counter = 0
    while not done:
        # Agent chooses action (initially random, gradually more intelligent)
        action = agent.get_action(obs)

        # Take action and observe result
        next_obs, reward, terminated, throwaway1, throwaway2 = env.step(action)

        # Learn from this experience
        agent.update(obs, action, reward, terminated, next_obs)

        # Move to next state
        done = terminated
        obs = next_obs

    # Reduce exploration rate (agent becomes less random over time)
    agent.decay_epsilon()

for key in dict(agent.q_values):
    best_move_index = list(agent.q_values[key]).index(max(agent.q_values[key]))
    if best_move_index == 0:
        best_move = "MOVE FORWARD"
    elif best_move_index ==1:
        best_move = "TURN LEFT"
    elif best_move_index ==2:
        best_move = "TURN RIGHT"
    else:
        best_move = "IDK BOSS"
    print(f"for observation {key} the policy is {best_move}\n")
