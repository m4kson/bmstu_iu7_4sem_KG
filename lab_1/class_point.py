EPS = 1e-6

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_equal(self, x, y):
        if abs(x - self.x) < EPS and abs(y - self.y) < EPS:
            return True
        else:
            return False
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
    
    