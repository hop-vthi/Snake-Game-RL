import numpy as np
import random
import math as m

BLOCK_SIZE = 30
GRID_SIZE = 15
# action, 0 = Forward, 1 = Left, 2 = Right
class Snake(object):
    def __init__(self):
        self.directions = [0, 1, 2, 3]     # 0: Up, 1:Down, 2: Left, 3: Right
        self.reset()


    def reset(self):
        # snake[0] là ĐẦU RẮN
        self.body = [[5, 10], [4, 10], [3, 10], [2, 10], [1, 10]]  #index 0 is head
        self.direction = self.directions[3] #Reset Right Direction
        self.score = 0
        self.frame_iteration = 0 # Dùng cho sau nay khi train -> giới hạn tg 1 lần chs game
    # self.place_apple()

    def movement(self, action):
        if action == 0: #Forward
            self.handle_forward(self.direction)
        elif action == 1: #Left
            self.handle_left(self.direction)
        else: #Right
            self.handle_right(self.direction)
        return self.body[0], self.direction

    # add to front of snake: body = [new_head] + body
    def handle_forward(self, direction):
        head_x, head_y = self.body[0]
        if (direction == 0):
            self.body = [[head_x - 1, head_y]] + self.body
        elif (direction == 1):
            self.body = [[head_x + 1, head_y]] + self.body
        elif (direction == 2):
            self.body = [[head_x, head_y - 1]] + self.body
        else:
            self.body = [[head_x, head_y + 1]] + self.body

    def handle_left(self, direction):
        head_x, head_y = self.body[0]
        if (direction==0):
            self.body = [[head_x, head_y - 1]] + self.body
            self.direction = 2 # Change direction to Left
        elif (direction == 1):
            self.body = [[head_x, head_y + 1]] + self.body
            self.direction = 3 # Change direction to left
        elif (direction == 2):
            self.body = [[head_x + 1, head_y]] + self.body
            self.direction = 1 # Change direction to down
        else:
            self.body = [[head_x - 1, head_y]] + self.body
            self.direction = 0 # Change direction to up

    def handle_right(self, direction):
        head_x, head_y = self.body[0]
        if (direction==0):
            self.body = [[head_x, head_y + 1]] + self.body
            self.direction = 3 # Change direction to right
        elif (direction == 1):
            self.body = [[head_x , head_y - 1]] + self.body
            self.direction = 2 # Change direction to left
        elif (direction == 2):
            self.body = [[head_x - 1, head_y]] + self.body
            self.direction = 0 # Change direction to up
        else:
            self.body = [[head_x + 1 , head_y]] + self.body
            self.direction = 1 # Change direction to up

    def is_collision(self, head_x, head_y):
        # Đâm tường
        if head_x < 0 or head_x > GRID_SIZE - 1 or head_y < 0 or head_y > GRID_SIZE - 1:
            return True
        # Đâm thân (so sánh từ phần thân thứ 1 trở đi, không xét đầu)
        new_head = [head_x, head_y]
        if new_head in self.body[1:]:
            return True
        return False

    def check_apple(self, check):
        if (check == 0):
            self.body.pop()

    # Ai code bẩn mắt thế !!!
    def check_danger_flag(self):
        new_head = self.body[0]
        x, y, z = 0, 0, 0
        if (self.direction == 0):
            if self.is_collision(new_head[0]-1,new_head[1]):
                x = 1
            if self.is_collision(new_head[0],new_head[1] - 1):
                y=1
            if self.is_collision(new_head[0],new_head[1] + 1):
                z=1
        elif (self.direction == 1):
            if self.is_collision(new_head[0]+1,new_head[1]):
                x = 1
            if self.is_collision(new_head[0],new_head[1] + 1):
                y= 1
            if self.is_collision(new_head[0],new_head[1] - 1):
                z=1
        elif (self.direction == 2):
            if self.is_collision(new_head[0] , new_head[1] - 1):
                x = 1
            if self.is_collision(new_head[0] + 1,new_head[1]):
                y=1
            if self.is_collision(new_head[0] - 1 ,new_head[1]):
                z=1
        elif (self.direction == 3):
            if self.is_collision(new_head[0], new_head[1] + 1):
                x = 1
            if self.is_collision(new_head[0] - 1, new_head[1]):
                y=1
            if self.is_collision(new_head[0] + 1, new_head[1]):
                z=1
        return  x,y,z
