"""
    This module provides functionality for finding the Euclidean distance
    between 2 Point objects.

    Original Author: Pranesh Kumar

    Created On: 12 Apr 2023
"""


class Point:
    def __init__(self, a: float = 0, b: float = 0):
        """Constructor of Point class

        Args:
            a (float, optional): x coordinate of Point. Defaults to 0.
            b (float, optional): y coordinate of Point. Defaults to 0.
        """
        self.__x = a
        self.__y = b
        self.__x_diff = 0
        self.__y_diff = 0
        self.__distance = 0

    def distance(self, anotherobject) -> float:
        """Find the Euclidean distance between 2 points

        The Euclidean distance between 2 points using the formula

        d = (((x1-x2)**2 + (y1-y2)**2)**0.5)

        Args:
            anotherobject (Point): another Point object to find the distance

        Returns:
            float: distance between 2 objects
        """
        self.__x_diff = (self.__x - anotherobject.__x) ** 2
        self.__y_diff = (self.__y - anotherobject.__y) ** 2
        self.__distance = (self.__x_diff + self.__y_diff) ** 0.5
        return self.__distance

    def __str__(self) -> str:
        """Returns human-readable string representation of an object

        Returns:
            str: String representation of object
        """
        return f"({self.__x} , {self.__y})"


# driver code
if __name__ == "__main__":
    x1 = float(input("Enter x coordinate of first point:"))
    y1 = float(input("Enter y coordinate of first point:"))
    x2 = float(input("Enter x coordinate of second point:"))
    y2 = float(input("Enter y coordinate of second point:"))

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    print("Point p1 is:", p1)
    print("Point p2 is:", p2)

    print("Distance between p1 and p2 is: ", p1.distance(p2))
    print("Distance between p2 and p1 is: ", p2.distance(p1))
