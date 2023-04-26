
def solve_quadratic(coeffs, x):
    coefficients = coeffs
    value = 0.0
    for idx in range(0, len(coefficients)):
        temp = coefficients[idx]
        for i in range(len(coefficients) - (idx + 1)):
            temp *= x
        value = value + temp
    return value      

def pow(x,y):
    if y == 0:
        return 1
    else:
        if y % 2 == 0:
            return pow(x, y//2) * pow(x, y//2)
        else:
            if y > 0:
                return x * pow(x, y//2) * pow(x, y//2)
            else:
                return (pow(x, y//2) * pow(x, y//2))/x

def efficient_solve_quadratic(coeffs, x):
    coefficients = coeffs
    value = 0.0
    for idx in range(0, len(coefficients)):
        temp = coefficients[idx] * pow(x, len(coefficients) - (idx + 1))
        value += temp
    return value

if __name__ == "__main__":
    degree = int(input("Enter the degree of the polynomial equation:"))
    coeffs = []
    print("Enter the co-efficients of the polynomial equation: ")
    for i in range(degree, -1, -1):
        c = float(input("Enter the coefficient of x^%d: " % i))
        coeffs.append(c)
    x = float(input("Enter the value of the variable: "))
    print("1. Solved value is:", solve_quadratic(coeffs, x = x))
    print("2. Efficiently Solved value is:", efficient_solve_quadratic(coeffs, x = x))
    
