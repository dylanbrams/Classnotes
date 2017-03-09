
class Circle(object):
    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

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