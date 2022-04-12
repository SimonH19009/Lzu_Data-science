import math
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def distance_from_origin(self):
        return math.hypot(self.x,self.y)
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __repr__(self):
        return "Point({0.x!r},{0.y!r})".format(self)
    def __str__(self):
        return "({0.x!r},{0.y!r})".format(self)

class Point3D(Point):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z
    def distance_from_origin(self):
        return math.hypot((self.x),(self.y) , (self.z))
    def __eq__(self, other):
        return super().__eq__(other) and self.z == other.z
    def __repr__(self):
        return "Point3D({0.x!r}, {0.y!r}, {0.z!r})".format(self)
    def __str__(self):
        return "({0.x!r}, {0.y!r}, {0.z!r})".format(self)
