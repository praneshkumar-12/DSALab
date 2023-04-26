
def solve_quadratic(a, b, c, x):
    coefficients = [a, b, c]
    value = 0.0
    for idx in range(0, len(coefficients)):
        temp = coefficients[idx]
        for i in range(len(coefficients) - (idx + 1)):
            temp *= x
        value = value + temp
    return value      



if __name__ == "__main__":
    print("Enter the co-efficients of a quadratic equation: ")
    a = float(input("Enter coefficient of x^2: "))
    b = float(input("Enter the coefficient of x: "))
    c = float(input("Enter the constant value: "))
    x = float(input("Enter the value of the variable: "))
    print("Solved value is:", solve_quadratic(a,b,c,x))
    
