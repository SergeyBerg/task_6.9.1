from rectangle import Rectangle, Square, Circle


rect1 = Rectangle(3,4)
rect2 = Rectangle(15,5)

# print(rect1.get_area())
# print(rect2.get_area())

square1 = Square(5)
square2 = Square(10)

# print(square1.get_area_square(), square2.get_area_square())

circle1 = Circle(15)
circle2 = Circle(11)

figures = [rect1, rect2, square1, square2, circle1, circle2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())