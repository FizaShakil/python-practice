# compare three number from greatest number
def print_greatest_num(num1, num2,num3):
    if(num1>num2 and num1>num3):
        print("First number is greatest which is: ", num1)
    elif(num2>num1 and num2>num3):
        print("Second number is greatest which is: ", num2)
    else:
        print("Third number is greatest, which is: ", num3)

print_greatest_num(50, 30, 10)

#celsius to fahrenheight conversion
def conversion_function(celsius):
    fahrenheight= (celsius * 9/5) + 32
    print(f"The {celsius}C into fahrenheight is {fahrenheight}F")

conversion_function(20)

# recursive function to calculate sum of first n natural numbers
def sum_calculate(n):
    if n<=1:
        return n
    else:
        return n + sum_calculate(n-1)
    
print(sum_calculate(5)) # call

#function to calculate specific start pattern
# ***
# **
# *
def print_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

print_pattern(9)

# print multiplication of given table
def table(num):
    print(f"Table of {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {i*num}")

table_input = table(16)
