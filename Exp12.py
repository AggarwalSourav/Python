AIM: Create a function max_of_three that takes three numbers as arguments and returns the largest of them and also create a parameter function that checks whether a given number is Armstrong or not.

def max_of_three(a, b, c):
    # Finding the largest number among three
    return max(a, b, c)
def is_armstrong(num):
    # Function to check if a number is Armstrong or not
    order = len(str(num))  # Calculating the number of digits in the number
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        return True
    else:
        return False
# Example usage of max_of_three function
a = 10
b = 25
c = 7

largest_number = max_of_three(a, b, c)
print(f"The largest number among {a}, {b}, and {c} is: {largest_number}")

# Example usage of is_armstrong function
number_to_check = 153  # Change this number to check for Armstrong property
if is_armstrong(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")
