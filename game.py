from random import randint

HEIGHT = 100
WIDTH = 50
POINT = 5
LIFE = 5
BALLAMOUNT = 20
BALLCHAR = ''
BACKGROUND = ''

class Ball:
    def __init__(self, start_point):
        self.x = start_point
        self.y = 0
    def down(self):
        if self.y < HEIGHT:
            self.y = self.y + 1
    def is_terminate(self):
        if self.y == HEIGHT:
            return self.x
        else:
            return -1

class Score:
    def __init__(self, player):
        self.life = LIFE
        self.point = 0
        self.ball = BALLAMOUNT
        self.name = player
    def is_end(self):
        if self.life <= 0 or self.ball <= 0:
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
        self.ball = self.ball - 1
        return randint(0, WIDTH)
    def get_life(self):
        return self.life
    def get_point(self):
        return self.point
    def get_ball(self):
        return self.ball
# Use link list to chain all the ball in different level of the height

class Board:
    def __init__(self, new_score):
        self.score = new_score
        self.balls = []
        self.catcher_pos = WIDTH / 2
    def render(self):
        level_of_ball = 0
        for _ in range(0, HEIGHT):
            for j in range(0, WIDTH):
                if level_of_ball < len(self.balls) and j == self.balls[level_of_ball]:
                    print(BALLCHAR)
                    self.balls[level_of_ball].down
                    level_of_ball = level_of_ball + 1
                else:
                    print(BACKGROUND)
    def move_left(self):
        if self.catcher_pos > 0:
            self.catcher_pos = self.catcher_pos - 1
    def move_right(self):
        if self.catcher_pos < WIDTH:
            self.catcher_pos = self.catcher_pos + 1
    def add_ball(self, pos):
        ball = Ball(pos)
        self.balls.insert(0, ball)
    def is_score(self):
        if not self.balls or self.balls[-1].is_terminate() == -1:
            return
        elif self.balls[-1].is_terminate() == self.catcher_pos:
            self.score.add_point()
        else:
            self.score.deduct_life()
        self.balls.pop()

