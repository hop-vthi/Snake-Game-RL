import pygame
from random import randint

# --- CÁC HẰNG SỐ ---
BLOCK_SIZE = 30
GRID_SIZE = 15
WIDTH = BLOCK_SIZE * GRID_SIZE
HEIGHT = BLOCK_SIZE * GRID_SIZE

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class snakeGame:
    def __init__(self):
        pygame.init()
        self.directions = [0,1,2,3]     # 0: Up, 1:Down, 2: Left, 3: Right
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake AI Environment')
        self.clock = pygame.time.Clock()
        self.font_small = pygame.font.SysFont('sans', 20)
        self.reset()

    def reset(self):
        # snake[0] là ĐẦU RẮN 
        self.body = [[5, 10], [4, 10], [3, 10]]  #index 0 is head
        self.direction = self.directions[3] #Reset Right Direction
        self.score = 0
        self.frame_iteration = 0 # Dùng cho sau nay khi train -> giới hạn tg 1 lần chs game
       # self.place_apple()
        
        # TODO: Trả về state ban đầu cho Agent (ví dụ: mảng tọa độ, hướng nhìn...)
        # return self.get_state() 

#    def place_apple(self):
        # Sinh táo ko đc trùng thân rắn
        # Gridsize-1 để nó khớp 1 map
#        self.apple = [randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)]
#        while self.apple in self.snake:
#            self.apple = [randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)]

#    def step(self, action):
#        #action space: up,down,right,left

#        self.frame_iteration += 1
        #start game
#       for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()
    def movement(self, action):
        if action == 0: #Forward
            self.handle_forward(self.direction)
        elif action == 1: #Left
            self.handle_left(self.direction)
        else: #Right
            self.handle_right(self.direction)
        return self.body[0], self.direction


    #new_head = [head_x, head_y]

        # checkCollapse
        #reward = 0
        #done = False
        # Dùng cho sau nay khi train -> giới hạn tg 1 lần chs game
        #if self.is_collision(new_head) or self.frame_iteration > 100 * len(self.body):
        #    done = True
        #    reward = -1 # sử dụng sau
        #    return reward, done, self.score

        # update head ăn điểm / ko ăn
        #self.body.insert(0, new_head)
        #if new_head[0] == self.apple[0] and new_head[1] == self.apple[1]:
        #    self.score += 1
        #    reward = 1 #
        #    self.place_apple()
        #else:
        #    self.body.pop() # Không ăn táo thì xóa đuôi để độ dài không đổi

        # Trả về kết quả cho Agent
        # Trong thực tế sẽ trả về (state, reward, done, score)
        #@TODO 
        return reward, done, self.score

    def handle_forward(self, direction):
        head_x, head_y = self.body[0]
        if (direction==0):
            self.body[0] = head_x - 1, head_y
        elif (direction == 1):
            self.body[0] = head_x + 1, head_y
        elif (direction == 2):
            self.body[0] = head_x, head_y - 1
        else:
            self.body[0] = head_x, head_y + 1
        self.body.pop()

    def handle_left(self, direction):
        head_x, head_y = self.body[0]
        if (direction==0):
            self.body[0] = head_x, head_y -1
            self.direction = 2 # Change direction to Left
        elif (direction == 1):
            self.body[0] = head_x , head_y + 1
            self.direction = 3 # Change direction to left
        elif (direction == 2):
            self.body[0] = head_x + 1, head_y
            self.direction = 1 # Change direction to down
        else:
            self.body[0] = head_x -1 , head_y
            self.direction = 0 # Change direction to up

    def handle_right(self, direction):
        head_x, head_y = self.body[0]
        if (direction==0):
            self.body[0] = head_x, head_y +1
            self.direction = 3 # Change direction to right
        elif (direction == 1):
            self.body[0] = head_x , head_y -1
            self.direction = 2 # Change direction to left
        elif (direction == 2):
            self.body[0] = head_x - 1, head_y
            self.direction = 0 # Change direction to up
        else:
            self.body[0] = head_x + 1 , head_y
            self.direction = 1 # Change direction to up

    def is_collision(self, head_x, head_y):
        # Đâm tường
        if head_x < 0 or head_x > GRID_SIZE - 1 or head_y < 0 or head_y > GRID_SIZE - 1:
            return True
        # Đâm thân (so sánh từ phần thân thứ 1 trở đi, không xét đầu)
        new_head = head_x, head_y
        if new_head in self.body[1:]:
            return True
        return False

    def check_apple(self, check):
        if (check == 0):
            self.body.pop()

    def check_danger_flag(self):
        new_head = self.body[0]
        x,y,z=0
        if (self.direction == 0):
            if (self.is_collision(new_head[0]-1,new_head[1])):
                x = 1
            if (self.is_collision(new_head[0],new_head[1])-1):
                y=1
            if(self.is_collision(new_head[0]-1,new_head[1])+1):
                z=1
        elif (self.direction == 1):
            if (self.is_collision(new_head[0]+1,new_head[1])):
                x = 1
            if (self.is_collision(new_head[0],new_head[1])-1):
                y= 1
            if(self.is_collision(new_head[0]-1,new_head[1])+1):
                z=1
        elif (self.direction == 2):
            if (self.is_collision(new_head[0],new_head[1])-1):
                x = 1
            if (self.is_collision(new_head[0]+1,new_head[1])):
                y=1
            if(self.is_collision(new_head[0]-1,new_head[1])+1):
                z=1
        elif (self.direction == 3):
            if (self.is_collision(new_head[0],new_head[1])+1):
                x = 1
            if (self.is_collision(new_head[0]-1,new_head[1])):
                y=1
            if(self.is_collision(new_head[0]+1,new_head[1])+1):
                z=1
        return  x,y,z

    # này sau đưa sang cho gym nó render() trong env.py
    def render(self, speed=15):
        # Vẽ game lên màn hình với tốc độ fps
        self.screen.fill(BLACK)

        # Vẽ rắn
        for pt in self.snake:
            pygame.draw.rect(self.screen, GREEN, (pt[0]*BLOCK_SIZE, pt[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # Vẽ táo
        pygame.draw.rect(self.screen, RED, (self.apple[0]*BLOCK_SIZE, self.apple[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        # Vẽ điểm
        score_txt = self.font_small.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_txt, (5, 5))

        pygame.display.flip()
        self.clock.tick(speed)

if __name__ == '__main__':
    env = snakeGame()
    
    # Vòng lặp này mô phỏng quá trình AI đang chơi
    ActionSpace = ["up","down","right","left"] # 0 , 1, 2 # Forward, Left, Right
    while True:
        # WF : rnd action -> getState -> render currentEnv
        action = ActionSpace[randint(0, 3)]
        reward, done, score = env.step(action)
        env.render()
        if done:
            env.reset()
            # print(f"Game Over! Final Score: {score}")

