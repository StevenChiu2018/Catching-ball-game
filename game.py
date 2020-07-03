LENGTH = 100
WIDTH = 50
POINT = 5
LIFE = 5
BALLAMOUNT = 20

class Ball:
    def __init__(self, start_point):
        self.x = start_point
        self.y = 0
    def down(self):
        if self.y < LENGTH:
            self.y = self.y + 1
    def is_terminate(self):
        if self.y == LENGTH:
            return True
        else:
            return False

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
    def get_life(self):
        return self.life
    def get_point(self):
        return self.point
    def get_ball(self):
        return self.ball