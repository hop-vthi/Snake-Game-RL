Phase 2: Implement Snake Agent
---
**1. Recap Environment**  
Custom environment. Environment (file `Env.py`) được kế thừa từ [gymnasium.env](https://gymnasium.farama.org/api/env/#gymnasium.Env)
Để ngắn gọn thì có các phương thức căn bản:
+ `gym.make()`: Khởi tạo môi trường.
+ `env.reset()`: Reset môi trường (sau mỗi `episode`, kết thúc...)
+ `env.step(action)`: Sau khi thực hiện method này (state + action) thì
  **return** `next_obs`, `reward`, `terminated`, `truncated`, `(info)`
  Ngoài ra còn có `env.render()`, `env.close()`... Thêm nữa, ta có:
1. `observation_space`(Không gian quan sát ví dụ với snake có thể là)

```python
obs_space = [head_x,head_y,target_x,target_y]
obs_space = [[snake_coor],[target_coor]]
# Với snake_coor[0] đang nghĩ để coor là snake's head. Sau đó custom với length thì length++
# Hoặc không thì để obs_space là cả một mảng 2D, đánh số target(1) và snake(0). Tuy nhiên thì vẫn phải lưu trữ lại coor của cả hai. Phần này đang nghĩ
```

2. `action_space` (Không gian di chuyển)
```python
#action_space thì đơn giản chỉ có lên, xuống, trái, phải
action_space = [0,1,2,3]
# Sau đó trong class GridWorldEv cần định nghĩa Ví dụ
self._action_to_direction = {
            0: np.array([0, 1]),   # Move right (column + 1)
            1: np.array([-1, 0]),  # Move up (row - 1)
            2: np.array([0, -1]),  # Move left (column - 1)
            3: np.array([1, 0]),   # Move down (row + 1)
        }
# Reference: https://gymnasium.farama.org/introduction/create_custom_env/
```

For more information and resources:
+ [gymnasium.env](https://gymnasium.farama.org/api/env/#gymnasium.Env)  (mentioned)
+ [Snake-Agent-DQN(Github1)](https://github.com/zanocrate/snake-rl)
+ [Snake-Environment(Github2)](https://github.com/grantsrb/Gym-Snake)

**2. Custom Environment Components**
+ `Env __init__`: Đã nói ở trên, xem chi tiết tại [Custom_Env](https://gymnasium.farama.org/introduction/create_custom_env/#)
+ `Construct Obs`: Get observation
+ `Reset function`
+ `Step function`: Là phương thức env.step(action), đã nói ở trên. Logic chính của trò chơi.

**3. Tóm lại về phần Environment**
Do ở trong Environment cũng có khá nhiều phần nhỏ khác, nên em định chia mỗi người một phần nhỏ đấy, xong sau đó mình đi giải quyết các chức năng tiếp theo. Hoặc không thì mình sẽ chia theo các chức năng luôn:
+ `Environment`
+ `Train model (DQN)` (Phần này cần đọc hiểu phần Unit 3/ Get batch, Save experience, Có thể sử dụng TensorFlow, Torch, Target NNetwork, State NNetwork...)
+ `Object Snake`. Các movements của nó -> action. Phần này cần bàn luận 1 chút @.@
+ `Main & Render`. Main thì không có gì quá nhiều. Render() để visualize, animation...

Last but not least báo cáo và slides @@
  Thực ra, thầy cũng bảo trọng số phần project thầy đang cho không quá cao. Nếu không thể sắp xếp được thời gian, thì mình có thể cân nhắc không dùng DQN nữa mà dùng Q-Learning thôi. Thì phần training sẽ đơn giản hơn và lúc ấy thì chỉ cần Custom Env.
  Tài liệu đọc cho Q-Learning & DQN:
+ [Blackjack Q-Learning](https://gymnasium.farama.org/introduction/train_agent/)
+ [Cart-pole DQN](https://youtu.be/97gDXdA7kVc?si=9WqLrx_ACTLQdTom)