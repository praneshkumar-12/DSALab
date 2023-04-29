from implementation import solve_quadratic, efficient_solve_quadratic, horners_method
import random

if __name__ == "__main__":
    normalmethod = {}
    efficientmethod = {}
    hornersmethod = {}
    n = int(input("Enter degree: "))
    if n == 0:
        print("Degree cannot be zero!")
        exit()
    for degree in range(n, n+1):
        coeffs = []
        normal = []
        efficient = []
        horners = []
        for _ in range(1):
            coeffs = [random.uniform(-100.0, 100.0) for _ in range(degree)]
            xvalue = random.uniform(-100.0, 100.0)
            normal.append(solve_quadratic(coeffs=coeffs, x=xvalue)[1])
            efficient.append(efficient_solve_quadratic(coeffs=coeffs, x=xvalue)[1])
            horners.append(horners_method(coeffs=coeffs, x=xvalue)[1])
        normalmethod[degree] = sum(normal)/len(normal)
        efficientmethod[degree] = sum(efficient)/len(efficient)
        hornersmethod[degree] = sum(horners)/len(horners)

    print("Normal Method:", normalmethod)

    print("======================================")
    
    print("Efficient Method:", efficientmethod)

    print("======================================")

    print("Horner's Method:", hornersmethod)
    