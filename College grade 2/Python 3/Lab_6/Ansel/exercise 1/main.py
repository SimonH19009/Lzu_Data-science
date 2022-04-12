import Shape
a=Shape.Point()
print(repr(a))
b=Shape.Point(3,4)
print(repr(b))
print(b.distance_from_origin())
a.x=2
a.y=3
print(a.distance_from_origin())
