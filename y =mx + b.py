from fractions import Fraction
from math import *
def find_intercept_Origin(x,y):
    match x,y:
        case 0,0:
            return "Origin"
        case 0,y:
            return "Y-Intercept"
        case x,0:
            return "X-Intercept"
        case _:
            return "Regualar"
def find_slope(x,y,x_2,y_2): #bugged returns frac_slope as slope
    '''Function to Find Slope'''
    slope = ((y_2 - y)/(x_2 - x))
    '''If slope is a decimal convert to fraction and retrun vaule'''
    if slope == float:
        frac_slope = str(Fraction(slope))
        return frac_slope
    else:
        return slope
def find_x_y_intercept(x_coefficient,y_coefficient,vaule):
    while True:
        try:
            find_x_y = int(input("What do want to find(x (1) /y (2))?: "))
            break
        except ValueError:
            print("Enter Int")
    if find_x_y < 1:
        find_x_y = 1
        print("Input less than one input is now One (Finding X).")
    elif find_x_y > 2:
        print("Input greated than two input is now One (Finding Y).")
    match find_x_y:
        case 1:
            x_intercept = vaule / x_coefficient
            if abs(x_intercept) < 1 or x_intercept == float:
                return str(Fraction(x_intercept))
            else:
                return x_intercept
        case 2:
            y_intercept = vaule / y_coefficient
            if abs(y_intercept) < 1 or y_intercept ==  float:
                return str(Fraction(y_intercept))
            else:
                return y_intercept
def solve_sys_eqau_simple(b_val,m_val,m_val2,b_val2):
    print(f"y = {m_val}x + {b_val}")
    print(f"y = {m_val2}x +{b_val2}")
    m_total = (m_val) - (m_val2)
    b_total = (b_val2) - (b_val)
    x = b_total / m_total
    print(x)
    y = m_val * x + b_val
    print(y)
    if y == float:
        y = Fraction(y)
    if x == float:
        x = Fraction(x)
    return f"({x},{y})"
'''
Fuctions to verify Shape
def verify_triangle_tpye(point1x,point1y,point2x,point2y,point3x,point3y):
    pass
    type_triangle = ["Traingle Type:"]
    # calculate Slopes
    slope_1_2 = (point2y-point1y) / (point2x-point1x)
    slope_1_3 = (point3y-point1y) / (point3x-point1y)
    slope_2_3 = (point3y-point2y) / (point3x-point2x)
    # calculate Lengths
    length_1_2 = sqrt(((point2x - point1x)**2) + ((point2y -point1y)**2))
    length_1_3 = sqrt(((point3x - point1x)**2)+ ((point3y - point1y) **2))
    length_2_3 = sqrt(((point3x -point2x) **2)+ ((point3y - point2y)**2))
    if length_1_2 == length_1_3 == length_2_3:
        type_triangle.append("Equilateral")
    elif not length_1_2 == length_1_3 == length_2_3:
        type.append("Scalene triangle")
def find_quad_tpye(point1x,point1y,point2x,point2y,point3x,point3y,point4x,point4y):
    length_1_2 = sqrt(((point2x - point1x)**2) + ((point2y -point1y)**2))
    length_1_3 = sqrt(((point3x - point1x)**2)+ ((point3y - point1y) **2))
    length_2_4 =sqrt(((point4x - point2x) **2) + ((point4y - point2y)**2))
    length_3_4 = sqrt(((point4x -point3x)**2)((point4y -point3y)**2))
    if length_1_2 == length_1_3 == length_2_4 == length_3_4:
        return "Sqaure"
    if ((length_1_2 == length_3_4) and (length_1_3 == length_2_4)) or ((length_1_2 == length_1_3)and (length_2_4 == length_3_4)):
        return "Rectangle"
'''
