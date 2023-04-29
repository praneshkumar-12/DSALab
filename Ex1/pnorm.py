"""
    This module provides with a function called norm()
    which returns the p-norm form of a vector in 3d space.

    When the value of p is specifically 2, then the p-norm results
    in Euclidean norm.

    This function calculates both p-norm and Euclidean norm

    p-norm is programmatically expressed as:

    p_norm = ((v[0] ** p) + (v[1] ** p) + (v[2] ** p) + ...... + (v[n] ** p)) ** (1/p)

    where,
    v - vector in 3d space (v1, v2, v3, ...., vn)
    p - if p is 2, then results in Euclidean norm

    Original Author : Pranesh Kumar

    Created On Sat 08 Apr 2023
"""


def norm(vector: iter, p: int = 2) -> float:
    """This function calculates and returns the p-norm form of a vector.
    If the value of p is specifically 2, then it is called Euclidean form.

    When norm(vector) is called, then it calculates Euclidean form, 
    where p takes the value 2, by default.
    When norm(vector, p) is called, then it calculates p-norm form.

    Args:
        vector (iter): any indexed iterable, i.e, a vector in 3d space
        p (int, optional): value of p to calculate p-norm form. Defaults to 2, for Euclidean form.

    Returns:
        float: the value of p-norm form of the given vector (sequence)
    """
    total: int = 0
    for elt in vector:
        total = total + (elt ** p)
    p_norm: float = total ** (1 / p)
    return p_norm


# end of norm() func.


# test code
if __name__ == "__main__":
    """Following code will be executed only when this Python
    file is run directly.  Code will be ignored if this
    file is imported by another Python source
    """

    # testing by providing values after getting input from user
    seq: tuple = eval(input("Enter sequence in tuple form: "))
    ch: str = input("Do you want Eucledian form? (Y?N): ")
    if ch.upper() == "Y":
        print(norm(vector=seq))
    else:
        P: int = int(input("Enter p value: "))
        print(norm(vector=seq, p=P))
