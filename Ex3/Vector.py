"""
    This module provides functionality for representing a vector as ADT.

    It creates a list of n elements and the elements can be modified by using special functions.

    These special functions support the operations performed on the vector.

    Created on: 19 Apr 2023

    Original Author: Pranesh Kumar
"""

class Vector:
    def __init__(self, size: int):
        """Constructor of Vector Class

        Args:
            size (int): size of the vector

        Sets the default value of the vector as 0

        """
        self.dim = size
        self.coord = [0 for _ in range(size)]
    
    def __len__(self) -> int:
        """Returns the length (dimension) of the vector

        Returns:
            int: size of the vector
        """
        return self.dim
    
    def __getitem__(self, index) -> int:
        """Returns the element at a particular index

        Args:
            index (int): index of the element which is required

        Raises:
            IndexError: If the index is greater than the size of the vector

        Returns:
            int: Element at the particular index
        """
        if index > self.dim:
            raise IndexError("Vector index out of range")
        else:
            return self.coord[index]
    
    def __setitem__(self, index: int, value) -> None:
        """Sets the element at the specified index with the new value

        Args:
            index (int): index at which the element is to be replaced
            value (int): new value of the element to be replaced

        Raises:
            IndexError: If the index is greater than the size of the vector

        Returns:
            None
        """
        if index > self.dim:
            raise IndexError("Vector index out of range")
        else:
            self.coord[index] = value
    
    def __eq__(self, other) -> bool:
        """Checks for equality of 2 vector objects

        Args:
            other (Vector): another vector object where the equality is to be checked

        Returns:
            bool: True if the dimensions and values are the same, else False
        """
        if self.dim == other.dim and self.coord == other.coord:
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return str(self.coord)  
    
    def __add__(self, other):
        """Returns the sum of 2 vectors

        Args:
            other (Vector): second vector object to be added

        Raises:
            IndexError: if indices are not the same

        Returns:
            Vector: Vector object of same dimensions but values as the sum
        """
        if self.dim == other.dim:
            newvector = Vector(self.dim)
            for idx in range(len(newvector)):
                newvector.coord[idx] = self.coord[idx] + other.coord[idx]
            return newvector
        else: 
            raise IndexError("Index is not the same")
    
    def __sub__(self, other):
        """Returns the difference of 2 vectors

        Args:
            other (Vector): second vector object to be subtracted

        Raises:
            IndexError: if indices are not the same

        Returns:
            Vector: Vector object of same dimensions but values as the difference
        """
        if self.dim == other.dim:
            newvector = Vector(self.dim)
            for idx in range(len(newvector)):
                newvector.coord[idx] = self.coord[idx] - other.coord[idx]
            return newvector
        else: 
            raise IndexError("Index is not the same")
    
    def multiply_by_scalar(self, scalar: int):
        """Returns a vector multiplied by a scalar

        Args:
            scalar (int): scalar value to be multiplied
        
        Retunrs:
            Vector: new vector after multiplying with scalar
        """
        newvector = Vector(self.dim)
        for idx in range(len(newvector)):
            newvector.coord[idx] *= scalar
        return newvector
            

# driver code
if __name__ == "__main__":
    n1 = int(input("Enter the size of vector 1: "))
    v1 = Vector(n1)
    print(len(v1))
    
    for idx in range(len(v1)):
        v1[idx] = int(input("Enter value: "))
    
    print("====================")

    for idx in range(len(v1)):
        print(v1[idx])
    
    print(v1)

    print("====================")

    n2 = int(input("Enter the size of vector 2: "))
    v2 = Vector(n2)
    print(len(v2))
    
    for idx in range(len(v2)):
        v2[idx] = int(input("Enter value: "))
    
    print("====================")

    for idx in range(len(v2)):
        print(v2[idx])
        
    print(v2)

    print(v1 == v2)
    print(v2 == v1)
    
    print(v1 + v2)
    print(v1 - v2)
    