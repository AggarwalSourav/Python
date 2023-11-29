AIM: write a python program that accepts the length of three sides of a triangle as inputs. The Program should indicate whether or not the triangle is a right angled triangle.(Use Pythagoras Theroem).Also find out its area using Herons formula

def is_right_angle_triangle(a, b, c):
    # Checking if it's a right-angled triangle using Pythagoras theorem
    sides = [a, b, c]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

def calculate_area(a, b, c):
    # Calculating the area of the triangle using Heron's formula
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Taking user inputs for the lengths of the sides of the triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Checking if it's a right-angled triangle
if is_right_angle_triangle(side1, side2, side3):
    print("It is a right-angled triangle.")
else:
    print("It is not a right-angled triangle.")

# Calculating and displaying the area of the triangle
area = calculate_area(side1, side2, side3)
print("The area of the triangle is:", area)
