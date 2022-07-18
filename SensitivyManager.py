from vectormath import Vector2
from utils import sign, clamp

class SensitivityManager():
    def __init__(self, sensitivity):
        self.sensitivity=sensitivity
        self.v2=Vector2(0, 0)

    def set_sensivity(self,new_sence):
        self.sensitivity=clamp(new_sence, 0, 1)

    def move(self, input_v2):
        x_input_sign=sign(input_v2.x)
        x_sign = sign(self.v2.x)

        y_input_sign=sign(input_v2.y)
        y_sign = sign(self.v2.y)

        if y_sign != y_input_sign:
            self.v2.y=0
        self.v2.y+=self.sensitivity*y_input_sign

        if x_sign != x_input_sign:
            self.v2.x=0
        self.v2.x+=self.sensitivity*x_input_sign
    
    def direction_v2(self):
        x=int(round(self.v2.x, 2) % 1 == 0) * sign(self.v2.x)
        y=int(round(self.v2.y, 2) % 1 == 0) * sign(self.v2.y)
        return (x, y)

    
