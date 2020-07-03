LENGTH = 100
WIDTH = 50
POINT = 5

class Ball:
    def __init__(self, start_point):
        self.x = start_point
        self.y = 0
    def down(self):
        if self.y < LENGTH:
            self.y = self.y + 1
    def terminate(self):
        if self.y == LENGTH:
            return True
        else:
            return False