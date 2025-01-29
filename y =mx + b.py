from fractions import Fraction
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
def find_intercept(x_coefficient,y_coefficient,vaule):
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