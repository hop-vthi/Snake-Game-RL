from matplotlib import pyplot as plt
import numpy as np
import os
import pickle
from collections import defaultdict

def get_moving_avgs(arr, window, convolution_mode):
    """Compute moving average to smooth noisy data."""
    if len(arr) < window:
        # Phòng trường hợp số episode đã chạy nhỏ hơn cửa sổ trượt (window)
        return np.array(arr)
    return (
        np.convolve(np.array(arr).flatten(), np.ones(window), mode=convolution_mode)
        / window
    )


# TODO : sửa lại đoạn env.return_queue 
def plot_training_results(env, agent, rolling_length: int = 500):
    fig, axs = plt.subplots(ncols=3, figsize=(15, 5))

    # 1. Đồ thị Episode rewards (Tổng phần thưởng nhận được)
    # env.return_queue thường là một danh sách lưu reward của các tập gần nhất
    axs[0].set_title("Episode rewards")
    reward_moving_average = get_moving_avgs(
        env.return_queue, rolling_length, "valid"
    )
    axs[0].plot(range(len(reward_moving_average)), reward_moving_average)
    axs[0].set_ylabel("Average Reward")
    axs[0].set_xlabel("Episode")

    # 2. Đồ thị Episode lengths (Số bước đi/thời gian sống của rắn mỗi trận)
    # env.length_queue lưu độ dài mỗi episode
    axs[1].set_title("Episode lengths")
    length_moving_average = get_moving_avgs(
        env.length_queue, rolling_length, "valid"
    )
    axs[1].plot(range(len(length_moving_average)), length_moving_average)
    axs[1].set_ylabel("Average Episode Length")
    axs[1].set_xlabel("Episode")

    # 3. Đồ thị Training error (Sai số TD-Error của thuật toán Q-learning)
    # Rút trực tiếp từ mảng training_error bạn đã định nghĩa trong SnakeAgent
    axs[2].set_title("Training Error")
    training_error_moving_average = get_moving_avgs(
        agent.training_error, rolling_length, "same"
    )
    axs[2].plot(
        range(len(training_error_moving_average)), training_error_moving_average
    )
    axs[2].set_ylabel("Temporal Difference Error")
    axs[2].set_xlabel("Step")

    plt.tight_layout()
    plt.show()


def save_agent_q_table(agent, filepath: str = "weights/snake_q_table.pkl"):
    """Trích xuất Q-table từ Agent và lưu xuống ổ đĩa dưới dạng file nhị phân (.pkl)"""
    # Tự động tạo thư mục weights nếu chưa có
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Chuyển defaultdict sang dict thông thường để vượt qua giới hạn không lưu được lambda của thư viện pickle
    raw_q_dict = dict(agent.q_values)

    with open(filepath, "wb") as f:
        pickle.dump(raw_q_dict, f)
    print(f"\n[IO SUCCESS] Da luu Q-table thanh cong tai: {filepath}")


def load_agent_q_table(agent, filepath: str = "weights/snake_q_table.pkl") -> bool:
    """Đọc file .pkl từ ổ đĩa và nạp ngược lại vào bộ não q_values của Agent"""
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            raw_q_dict = pickle.load(f)

        # Chuyển đổi ngược từ dict thường sang defaultdict(lambda: np.zeros) để Agent tiếp tục chạy mượt mà
        agent.q_values = defaultdict(
            lambda: np.zeros(agent.env.action_space.n), raw_q_dict
        )
        print(f"[IO LOADED] Da tai thanh cong Q-table tu: {filepath}. San sang demo!")
        return True
    else:
        print(f"[IO WARNING] Khong tim thay file {filepath}! Agent se choi ngau nhien.")
        return False