# Program to print table of 3

table_input = int(input("Enter a number to print table: "))
print("Table of ", table_input)
for i in range(1,11):
    nums = i * table_input
    print(table_input, " x ", i ," = ", nums )

#program to greet all members in list
list1=["Sanam", "Hina", "Faiza", "Humera", "Lubna"]
for i in list1:
    print("Hello, ", i)

#program to find given number is prime or not
def is_prime(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to the square root
        if num % i == 0:
            return False  # If divisible by any number, it's not prime
    return True  # If no divisors found, it's prime

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#program to print sum of n natural num
n = int(input("Of how much numbers you want to calculate sum? "))
list2 = []
for i in range(n):
    input_nums = int(input(f"Now Enter {i+1} number: "))
    list2.append(input_nums)

sum_of_nums = sum(list2)
print("Sum of the inputted numbers are: ", sum_of_nums)

def print_pyramid_pattern(n):
    """
    Prints a star pyramid pattern for a given number of rows (n).
    """
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)

        print(spaces + stars)

n = 3
print_pyramid_pattern(n)

#print star pattern
input_num = int(input("Enter input: "))
for i in range(1 , input_num+1):
    print("*" * i)

