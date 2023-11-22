import random
import time

powerOfEquation = int(input("Please enter the power of the equation: "))
x_axis = int(input("Enter the value of point x: "))
print("Transactions are being processed...")
time.sleep(1)
print()

# equationOfPointTangentToFunction


def createEquationWDerivative(x):
    eq_str = ""
    der_eq_str = ""
    eq = float()
    der_eq = float()
    coefficientList = list()
    for i in range(powerOfEquation + 1):
        coefficient = int(random.random() * 10)
        coefficientList.append(coefficient)
        eq += coefficient * (x ** i)
        if coefficient == 0:
            continue
        else:
            if eq_str == "":
                eq_str = f"{coefficient}x^{i}"
            else:
                eq_str = f"{coefficient}x^{i}" + " + " + eq_str
        if i != 0:
            der_eq += i * coefficient * (x ** (i - 1))
            if coefficient * i == 0:
                continue
            else:
                if der_eq_str == "":
                    der_eq_str = f"{coefficient * i}x^{i - 1}"
                else:
                    der_eq_str = f"{coefficient * i}x^{i - 1}" + " + " + der_eq_str
    coefficientList.reverse()
    return eq, der_eq, eq_str, der_eq_str, coefficientList


def tangentEquation(x):
    results = list()
    eq, der_eq, eq_str, der_eq_str, coefficientList = createEquationWDerivative(x)
    C = eq - (der_eq * x)
    results.append(f"All coefficients : {coefficientList}")
    results.append(f"The equation : {eq_str}")
    results.append(f"The derivative of equation : {der_eq_str}")
    results.append(f"The point : {(x, int(eq))}")
    if C < 0:
        results.append(f"The equation of point Tangent : f(x) = {int(der_eq)}x {int(C)}")
    else:
        results.append(f"The equation of point Tangent : f(x) = {int(der_eq)}x + {int(C)}")
    return results


for i in tangentEquation(x_axis):
    print(i)
    print("-----------------------------------------------------------------")
