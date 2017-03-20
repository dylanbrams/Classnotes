
#Class Definitions

class Point(object):
    def __init__(self, xy_in):
        x_coord = xy_in[0]
        y_coord = xy_in[1]
        self._xy_tuple = Point(x_coord, y_coord)
    def __init__(self, x_coord_in, y_coord_in):
        self.x_coord = x_coord_in
        self.y_coord = y_coord_in
    def __repr__(self):
        return ("X: " + str(self.x_coord) + ", Y:" + str(self.y_coord))

class Circle(object):
    def __init__(self, radius, xy_center):
        self._radius = radius
        #self.center = Point(xy_center)
        self._center = Point(xy_center[0], xy_center[1])
    def is_in_circle(self, x_in, y_in):
        """

        >>> Circle(3, 4, 4).is_in_circle(5, 5)
        True

        >>> Circle(3, 4, 4).is_in_circle(10, 5)
        False

        :param x_in:
        :param y_in:
        :return:

        """

        return False;

    def print_xy_center(self):
        print (repr(self._center))

    def move_circle(self, new_xy_center):
        # self.center = Point(new_xy_center[0], new_xy_center[1])
        myCenter = Point(new_xy_center[0], new_xy_center[1])
        return Circle(self._radius, new_xy_center)

def move_circle(circle, new_xy_center):
    # self.center = Point(new_xy_center[0], new_xy_center[1])
    myCenter = Point(new_xy_center[0], new_xy_center[1])
    return Circle(circle.radius, new_xy_center)

def find_circle_largest_radius(circles):
    highest_radius = 0
#    for circle in circles:


#Main Definition
def main():
    circle_instance = Circle(4, (1, 1))
    circle_instance.print_xy_center()
    Circle._center = (3, 12634)
    print(repr(circle_instance.center))
    NewCircle = circle_instance.move_circle((2,2))
    NewCircle.print_xy_center()
    NewCircle2 = move_circle(NewCircle, (4,5))
    print(repr(circle_instance.center))
    return
# Circle: (class)
#     Methods:
#             print_xy_center
#             is_in_circle
#             move_circle
#     Properties:
#             center
#             radius

#Main Call
if __name__ == '__main__':
    main()

