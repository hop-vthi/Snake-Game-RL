import os

from tqdm import tqdm  # Progress bar
from gymnasium.wrappers.vector import RecordEpisodeStatistics

from env import SnakeBoardEnv
from snake import Snake
from SnakeAgent import SnakeAgent
from train import *
from render import Render

train_mode = True
MODEL_PATH = os.path.join("weights", "snake_q_table.pkl")
# Training hyperparameters
learning_rate = 0.01        # How fast to learn (higher = faster but less stable)
n_episodes = 500000        #  Number of hands to practice
start_epsilon = 1.0         # Start with 100% random actions
epsilon_decay = start_epsilon / (n_episodes / 2)  # Reduce exploration over time
final_epsilon = 0.1         # Always keep some exploration

# Create environment and agent
snake = Snake()
env = SnakeBoardEnv(snake, 15, 42) #snake, size, seed
agent = SnakeAgent(env, learning_rate, start_epsilon, epsilon_decay, final_epsilon)
# env = RecordEpisodeStatistics(env) # custom env not applicable -mace
display = Render()
episode_rewards = []
episode_lengths = []
episode_scores = []
max_score = 0



if train_mode:
    for episode in tqdm(range(n_episodes)):
        # Start a new hand
        obs, throwaway_empty_dict = env.reset() #add padding -mace
        done = False
        total_reward = 0
        step_count = 0
        score = 0
        check_goal = 0

        # shitass_counter = 0
        while not done:
            # Agent chooses action (initially random, gradually more intelligent)
            action = agent.get_action(obs)

            # Take action and observe result
            next_obs, reward, terminated, throwaway1, throwaway2, check_goal = env.step(action)

            # if check_goal =1 meaning that snake eats food
            score+= check_goal
            # Learn from this experience
            agent.update(obs, action, reward, terminated, next_obs)

            #display.render(env.snake.body, env.apple_location) if episode >= n_episodes - 100 else None

            # Move to next state
            done = terminated
            obs = next_obs

            # Calculate total_reward and step_count at each episode
            total_reward+=reward
            step_count+=1

        # Appending reward and step after each episode
        episode_rewards.append(total_reward)
        episode_lengths.append(step_count)
        episode_scores.append(score)
        max_score = max(score, max_score)
        # Reduce exploration rate (agent becomes less random over time)
        agent.decay_epsilon()
    #save_agent_q_table(agent, MODEL_PATH)
    plot_training_results(episode_rewards, episode_lengths, episode_scores, agent)
    print(f'Max score: {max_score}')

#else:
    # Gọi hàm từ file train để nạp bộ não cũ vào Agent
    # if load_agent_q_table(agent, MODEL_PATH):
    #     agent.epsilon = 0.0  # Khóa tính năng chạy ngẫu nhiên, ép ăn mồi tối ưu nhất
    #     # Chạy thử 3 trận
    #     for demo_ep in range(3):
    #         print(f"Chay tran demo so {demo_ep + 1}...")
    #         obs, _ = env.reset()
    #         done = False
    #
    #         while not done:
    #             display.render(env.snake.body, env.apple_location)
    #             action = agent.get_action(obs)
    #             next_obs, reward, terminated, _, _ = env.step(action)
    #             obs = next_obs
    #             done = terminated
    #plot_training_results(env,agent,10000)
     
# for key in dict(agent.q_values):
#     if key == 0:
#         print("END GAME/EPISODE TERMINATED\n")
#         continue
#     best_move_index = list(agent.q_values[key]).index(max(agent.q_values[key]))
#     if best_move_index == 0:
#         best_move = "MOVE FORWARD"
#     elif best_move_index ==1:
#         best_move = "TURN LEFT"
#     elif best_move_index ==2:
#         best_move = "TURN RIGHT"
#     else:
#         best_move = "IDK BOSS"
#     apple_forward_behind ="Apple is behind" if key[0] else "Apple is forward"
#     apple_left_right ="Apple is right" if key[1] else "Apple is left"
#     danger_forward_flag = "Danger forward" if key[2] else "No danger forward"
#     danger_left_flag = "Danger left" if key[3] else "No danger left"
#     danger_right_flag = "Danger right" if key[4] else "No danger right"
#     d_map = {0: "up", 1: "down", 2: "left", 3: "right"}
#     direction =d_map[key[5]]
#     key = (
#         f"{apple_forward_behind}", 
#         f"{apple_left_right}",
#         f"{danger_forward_flag}",
#         f"{danger_left_flag}",
#         f"{danger_right_flag}",
#         f"{direction}"
#     )
#     print(f"obs: {key}, policy: {best_move}")
