"""
    This module provides functionality for finding the k-nearest neighbours
    of a given point with some k random points

    Original Author: Pranesh Kumar

    Created on : 12 Apr 2023
"""

# importing the necessary modules
from question1 import Point
import random


def findKNN(k: int, newPoint: Point, startvalue: int = 0, endvalue: int = 100) -> list:
    """This function finds the k-nearest neighbours of a given point with k
    random points generated.

    It returns the points which are closest to the newPoint in ascending order

    Args:
        k (int): number of points to be generated
        newPoint (Point): new object of Point class whose KNN is to be determined
        startvalue (int, optional): Starting range for generating random values. Defaults to 0.
        endvalue (int, optional): Starting range for generating random values. Defaults to 100.

    Returns:
        list: list of points in ascending order of distance from newPoint
    """
    distances = {}
    for _ in range(k):
        myPoint = Point(
            random.randint(startvalue, endvalue), random.randint(startvalue, endvalue)
        )
        distances[str(myPoint)] = newPoint.distance(myPoint)

    distancesList = list(distances)
    knearestneighbours = sorted(distancesList, key=lambda x: x[1])

    return knearestneighbours


# driver code
if __name__ == "__main__":
    n = int(input("Enter the number of test cases: "))
    x1 = 12
    y2 = 21
    p = Point(x1, y2)
    print(findKNN(n, p))
