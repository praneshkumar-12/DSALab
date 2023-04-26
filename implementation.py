count = 0
def solve_quadratic(coeffs, x):
    count = 0
    coefficients = coeffs
    count += 1
    value = 0
    count += 1
    for idx in range(0, len(coefficients)):
        temp = coefficients[idx]
        count += 1
        for i in range(len(coefficients) - (idx + 1)):
            temp *= x
            count += 1
        value += temp
        count += 1
    return value, count

def pow(x,y):
    global count
    count += 1
    if y == 0:
        return 1
    else:
        if y % 2 == 0:
            temp = pow(x, y//2)
            return temp * temp
        else:
            if y > 0:
                temp = pow(x, y//2)
                return x * temp * temp
            else:
                temp = pow(x, y//2)
                return (temp * temp)/x

def efficient_solve_quadratic(coeffs, x):
    global count
    count = 0
    coefficients = coeffs
    count += 1
    value = 0.0
    count += 1
    for idx in range(0, len(coefficients)):
        count += 1
        temp = coefficients[idx] * pow(x, len(coefficients) - (idx + 1))
        count += 1
        value += temp
        count += 1

    return value, count

def horners_method(coeffs, x):
    global count 
    count = 0
    sum = coeffs[0]
    count += 1
    for idx in range(1, len(coeffs)):
        sum = sum * x + coeffs[idx]
        count += 1
    return sum ,count

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
