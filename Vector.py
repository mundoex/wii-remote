import numpy

class Vector3():
    def __init__(self,x=0,y=0,z=0):
      self.arr=numpy.array([x,y,z])

    def __add__(self, o):
        return self.arr+o.arr

    def stereograhpic_projection(self):
        return numpy.arr([self.x()/self.z(), self.y()/self.z()])

    def x(self):
        return self.arr[0]

    def y(self):
        return self.arr[1]

    def z(self):
        return self.arr[2]