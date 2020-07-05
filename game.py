import os, time
from random import randint
import tkinter as tk

HEIGHT = 200
WIDTH = 300
POINT = 5
LIFE = 5

BALLAMOUNT = 20
BALLLENGTH = 10
BALLCOLOR = 'blue'

PADDLECOLOR = 'yellow'
PADDLELENGTH = 30
PADDLESTEP = 5
PADDLEHEIGHT = 20

BACKGROUND = 'skyblue'
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
    def __init__(self, player):
        self.life = LIFE
        self.point = 0
        self.ball = BALLAMOUNT
        self.name = player
    def is_end(self):
        if self.life <= 0 or (self.point + (LIFE - self.life) * POINT) == 100:
            return True
        else:
            return False
    def show_score(self):
        if self.point >= 90:
            print(self.name + " ， 您好棒！")
        elif self.point >= 75:
            print(self.name + " ， 不錯唷！")
        elif self.point >= 60:
            print(self.name + " ， 還可以！")
        else:
            print(self.name + " ， 在努力練習！")
    def add_point(self):
        self.point = self.point + POINT
    def deduct_life(self):
        self.life = self.life - 1
    def drop_ball(self):
        if self.ball:
            self.ball = self.ball - 1 
            return randint(0, WIDTH - 1)
        else:
            return -1
    def get_life(self):
        return self.life
    def get_point(self):
        return self.point
    def get_ball(self):
        return self.ball

class Paddle:
    def __init__(self, pos, canvas):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(pos, HEIGHT - PADDLEHEIGHT, pos + PADDLELENGTH, HEIGHT, fill = PADDLECOLOR)
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)
    def move_left(self, event):
        pos = self.canvas.coords(self.id)
        if pos[0] > PADDLESTEP:
            self.canvas.move(self.id, -1 * PADDLESTEP, 0)
    def move_right(self, event):
        pos = self.canvas.coords(self.id)
        if pos [2] < (WIDTH - PADDLESTEP):
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
            if ball_pos[3] == HEIGHT - PADDLEHEIGHT:
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
    canvas = tk.Canvas(window, width = WIDTH, height = HEIGHT, bg = BACKGROUND, bd = 0, highlightthickness = 0)
    window.resizable(0,0)
    canvas.pack()

    score = Score("Steven")
    paddle = Paddle(0, canvas)
    board = Board(score, paddle, canvas)
    clock = 0

    while not score.is_end():
        if clock % 100 == 0:
            board.add_ball()
        board.render()
        window.update_idletasks()
        window.update()
        time.sleep(DELAYTIME)
        clock = clock + 1