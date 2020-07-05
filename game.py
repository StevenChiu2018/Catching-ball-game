import os, time
from random import randint
import tkinter as tk

# 視窗大小
WINDOWHEIGHT = 400
WINDOWWIDTH = 300

# 遊戲的基本設置
GAMEHEIGHT = 200
GAMEWIDTH = 300
POINT = 5
LIFE = 5

# 球的基本設置
BALLAMOUNT = 20
BALLLENGTH = 10
BALLCOLOR = 'blue'

#接盤的基本設置
PADDLECOLOR = 'yellow'
PADDLELENGTH = 30
PADDLESTEP = 5
PADDLEHEIGHT = 20

#系統設置
BACKGROUND = 'skyblue' #背景顏色設置
DELAYTIME = 0.01

class Ball:
    def __init__(self, pos, canvas):
        self.canvas = canvas
        self.id = self.canvas.create_oval(pos, 0, pos + BALLLENGTH, BALLLENGTH, fill = BALLCOLOR)
    def render(self):
        self.canvas.move(self.id, 0, 1)
    def get_pos(self):
        return self.canvas.coords(self.id)
    def delete(self):
        self.canvas.delete(self.id)

class Score:
    def __init__(self, player, window):
        self.life = LIFE
        self.point = 0
        self.ball = BALLAMOUNT
        self.name = player
        self.window = window
    def is_end(self):
        if self.life <= 0 or (self.point + (LIFE - self.life) * POINT) == 100:
            return True
        else:
            return False
    def show_score(self):
        head_text = tk.StringVar()
        if self.point >= 90:
            head_text.set(self.name + " ， 您好棒！")
        elif self.point >= 75:
            head_text.set(self.name + " ， 不錯唷！")
        elif self.point >= 60:
            head_text.set(self.name + " ， 還可以！")
        else:
            head_text.set(self.name + " ， 在努力練習！")
        label = tk.Label(self.window, textvariable = head_text)
        label.place(x = (GAMEWIDTH / 4), y = (GAMEHEIGHT / 4))
        self.window.update()
    def add_point(self):
        self.point = self.point + POINT
    def deduct_life(self):
        self.life = self.life - 1
    def drop_ball(self):
        if self.ball:
            self.ball = self.ball - 1 
            return randint(0, GAMEWIDTH - 1)
        else:
            return -1
    def get_life(self):
        return self.life
    def get_point(self):
        return self.point
    def get_ball(self):
        return self.ball
    def show_state(self):
        head_text = tk.StringVar()
        head_text.set("Player: " + self.name + "    " + "Score: " + str(self.point) + "    " + "Life: " + str(self.life) + "/" + str(LIFE))
        label = tk.Label(self.window, textvariable = head_text)
        label.place(x = 0, y = GAMEHEIGHT + 1)

class Paddle:
    def __init__(self, pos, canvas):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(pos, GAMEHEIGHT - PADDLEHEIGHT, pos + PADDLELENGTH, GAMEHEIGHT, fill = PADDLECOLOR)
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)
    def move_left(self, event):
        pos = self.canvas.coords(self.id)
        if pos[0] > PADDLESTEP:
            self.canvas.move(self.id, -1 * PADDLESTEP, 0)
    def move_right(self, event):
        pos = self.canvas.coords(self.id)
        if pos [2] < (GAMEWIDTH - PADDLESTEP):
            self.canvas.move(self.id, PADDLESTEP, 0)
    def get_pos(self):
        return self.canvas.coords(self.id)

class Board:
    def __init__(self, new_score, paddle, canvas):
        self.score = new_score
        self.balls = []
        self.paddle = paddle
        self.canvas = canvas
    def render(self):
        for ball in self.balls:
            ball_pos = ball.get_pos()
            paddle_pos = self.paddle.get_pos()
            if ball_pos[3] == GAMEHEIGHT - PADDLEHEIGHT:
                if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
                    self.score.add_point()
                else:
                    self.score.deduct_life()
                ball.delete()
                del self.balls[0]
            else:
                ball.render()
    def add_ball(self):
        ball_pos = self.score.drop_ball()
        if ball_pos != -1:
            ball = Ball(ball_pos, self.canvas)
            self.balls.append(ball)

if __name__ == "__main__":
    window = tk.Tk()
    canvas = tk.Canvas(window, width = WINDOWWIDTH, height = WINDOWHEIGHT, bg = BACKGROUND, bd = 0, highlightthickness = 0)
    window.resizable(0,0)
    canvas.pack()

    player_name = input('Player name: ')
    score = Score(player_name, window)
    paddle = Paddle(0, canvas)
    board = Board(score, paddle, canvas)
    clock = 0

    while not score.is_end():
        if clock % 100 == 0:
            board.add_ball()
        board.render()
        score.show_state()
        window.update_idletasks()
        window.update()
        time.sleep(DELAYTIME)
        clock = clock + 1
    score.show_score()
    while True:
        input()