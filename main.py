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
    if key == 0:
        print("END GAME/EPISODE TERMINATED\n")
        continue
    best_move_index = list(agent.q_values[key]).index(max(agent.q_values[key]))
    if best_move_index == 0:
        best_move = "MOVE FORWARD"
    elif best_move_index ==1:
        best_move = "TURN LEFT"
    elif best_move_index ==2:
        best_move = "TURN RIGHT"
    else:
        best_move = "IDK BOSS"
    apple_forward_behind ="Apple is behind" if key[0] else "Apple is forward"
    apple_left_right ="Apple is right" if key[1] else "Apple is left"
    danger_forward_flag = "Danger forward" if key[2] else "No danger forward"
    danger_left_flag = "Danger left" if key[3] else "No danger left"
    danger_right_flag = "Danger right" if key[4] else "No danger right"
    d_map = {0: "up", 1: "down", 2: "left", 3: "right"}
    direction =d_map[key[5]]
    key = (
        f"{apple_forward_behind}", 
        f"{apple_left_right}",
        f"{danger_forward_flag}",
        f"{danger_left_flag}",
        f"{danger_right_flag}",
        f"{direction}"
    )
    print(f"obs: {key}, policy: {best_move}")
