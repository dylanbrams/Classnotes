
class Point(object):
    def __init__(self, xy_in):
        x_coord = xy_in[0]
        y_coord = xy_in[1]
        my_point = Point(x_coord, y_coord)
    def __init__(self, x_coord_in, y_coord_in):
        self.x_coord = x_coord_in
        self.y_coord = y_coord_in

class Circle(object):
    def __init__(self, radius, xy_center):
        self.radius = radius
        #self.center = Point(xy_center)
        self.center = Point(xy_center[0], xy_center[1])
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

def main():
    circle = Circle(4, (1, 1))
    return

if __name__ == '__main__':
    main()

