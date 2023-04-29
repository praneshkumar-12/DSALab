"""
    This module provides functionality for implementing matrix as ADT.

    It provides functions for matrix addition, subtraction and multiplication.

    It also provides with special functions that support various operations.

    Created on: 19 Apr 2023

    Original Author: Pranesh Kumar
"""


class Matrix:
    def __init__(self, r: int = 0, c: int = 0):
        """Constructor of Matrix class

        Args:
            r (int, optional): Number of rows of matrix. Defaults to 0.
            c (int, optional): Number of cols of matrix. Defaults to 0.
        """
        self.rows = r
        self.cols = c
        self.values = [[0 for _ in range(c)] for _ in range(r)]

    def __len__(self):
        """Returns the length of the matrix (number of rows)

        Returns:
            int: Number of rows of the matrix
        """
        return self.rows

    def __getitem__(self, idx):
        """Returns the element at a particular index

        Args:
            idx (int): index of the element which is required

        Raises:
            IndexError: If the index is greater than the size of the vector

        Returns:
            int: Element at the particular index
        """
        if idx > self.__len__():
            raise IndexError("Index out of range")
        else:
            return self.values[idx]

    def __setitem__(self, idx, value):
        """Sets the element at the specified index with the new value

        Args:
            idx (int): index at which the element is to be replaced
            value (int): new value of the element to be replaced

        Raises:
            IndexError: If the index is greater than the size of the vector
        """
        if idx > self.__len__():
            raise IndexError("Index out of range")
        else:
            self.values[idx] = value

    def __str__(self):
        matrixasstring = ""
        for rows in range(len(self)):
            for cols in range(len(self[0])):
                matrixasstring += str(self[rows][cols]) + "\t"
            matrixasstring += "\n"
        return matrixasstring

    def __eq__(self, other):
        """Checks for equality of 2 matrix objects

        Args:
            other (Vector): another vector object where the equality is to be checked

        Returns:
            bool: True if the dimensions and values are the same, else False
        """
        if self.__len__() == len(other) and self[0].__len__() == len(other[0]) and self.values == other.values:
            return True
        else:
            return False

    def __add__(self, other):
        """Returns the sum of 2 matrices

        Args:
            other (Matrix): second matrix object to be added

        Raises:
            IndexError: if indices are not the same

        Returns:
            Matrix: Matrix object of same dimensions but values as the sum
        """
        if self.__len__() == len(other) and self[0].__len__() == len(other[0]):
            newmatrix = Matrix(self.__len__(), self[0].__len__())
            for rows in range(len(newmatrix)):
                for cols in range(len(newmatrix[0])):
                    newmatrix[rows][cols] = self[rows][cols] + other[rows][cols]
            return newmatrix
        else:
            raise IndexError("Index is not the same")

    def __sub__(self, other):
        """Returns the sum of 2 matrices

        Args:
            other (Matrix): second matrix object to be subtracted

        Raises:
            IndexError: if indices are not the same

        Returns:
            Matrix: Matrix object of same dimensions but values as the difference
        """
        if self.__len__() == len(other) and self[0].__len__() == len(other[0]):
            newmatrix = Matrix(self.__len__(), self[0].__len__())
            for rows in range(len(newmatrix)):
                for cols in range(len(newmatrix[0])):
                    newmatrix[rows][cols] = self[rows][cols] - other[rows][cols]
            return newmatrix
        else:
            raise IndexError("Index is not the same")

    def __mul__(self, other):
        """Returns the product of 2 matrices

        Args:
            other (Matrix): second matrix object to be multiplied

        Raises:
            IndexError: if indices are not the same

        Returns:
            Matrix: Matrix object of same dimensions but values as the product
        """
        if self[0].__len__() != len(other):
            raise IndexError("Index is not the same for multiplication")
        else:
            newmatrix = Matrix(self.__len__(), len(other[0]))
            for i in range(self.__len__()):
                for j in range(len(other[0])):
                    for k in range(len(other)):
                        newmatrix[i][j] += self[i][k] * other[k][j]
            return newmatrix

    def multiply_by_scalar(self, scalar: int):
        """Returns a matrix multiplied by a scalar

        Args:
            scalar (int): scalar value to be multiplied

        Retunrs:
            Matrix: new matrix after multiplying with scalar
        """
        newmatrix = Matrix(self.__len__(), self[0].__len__())
        for rows in range(len(newmatrix)):
            for cols in range(len(newmatrix[0])):
                newmatrix[rows][cols] = self[rows][cols] * scalar
        return newmatrix


# driver code
if __name__ == "__main__":
    m1 = Matrix(3, 3)
    m2 = Matrix(3, 3)
    print(len(m1))
    print(m1[0])
    print(m1[0][0])
    print("Enter matrix elements row-wise:")
    for rows in range(len(m1)):
        for cols in range(len(m1[0])):
            m1[rows][cols] = int(input())
    print(m1)
    print("Enter matrix elements row-wise:")
    for rows in range(len(m2)):
        for cols in range(len(m2[0])):
            m2[rows][cols] = int(input())
    print(m2)
    print(m1 == m2)
    print(m1 + m2)
    print(m1 - m2)
    print(m1.multiply_by_scalar(2))
    print(m1 * m2)
