#find greatest of four numbers
num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))
num3 = int(input("Enter 3rd num: "))
num4 = int(input("Enter 4th num: "))

greatest_num = max(num1, num2, num3, num4)
print("Greatest number is: ", greatest_num)

# check wheteher student is pass or fail in each subject and overall
#  by taking input of 3 number

marks1 = int(input("Enter 1st subject marks "))
marks2 = int(input("Enter 2ndsubject marks "))
marks3 = int(input("Enter 3rd subject marks "))

total_each =50
grand_total = 150

passing_ratio_marks1 = (marks1/total_each)*100
passing_ratio_marks2 = (marks2/total_each)*100
passing_ratio_marks3 = (marks3/total_each)*100

if (((marks1 + marks2 + marks3)/grand_total)*100 >=40):
        print("You are passed")
        if passing_ratio_marks1>=33:
              print("You are passed in subject 1")
        else:
               print("You are failed in subject 1")

        if passing_ratio_marks2>=33:
               print("You are passed in subject 2")
        else:
               print("You are failed in subject 1")

        if passing_ratio_marks3>=33:
               print("You are passed in subject 3")
        else:
               print("You are failed in subject 3")

else:
       print("You are Failed. your grandtotal is less than 40%")

# program to detect spam comments
input_string = input("Enter your comment message: ")

s = input_string.lower()
print(s)

spam_keywords = [
    "make a lot of money",
    "buy now",
    "subscribe this",
    "click this"
]

# Check if ANY of the spam keywords are present in the input string
if (spam_keywords[0]== s or
    spam_keywords[1]== s or
    spam_keywords[2]== s or
    spam_keywords[3]== s):
    print("Its a spam comment. Be aware of scam")
else:
    print("It is not a spam comment")

#program to count whether character is less han 10 or not

str_input = input("Enter the string: ")
str_length = len(str_input)

if(str_length>=10):
    print("Your string has greater than 10 characters")
else:
    print("Your string has less than 10 characters")

#program to find out whether the name is present in list or not
    
list1 = ["Ana", "Elsa", "Sana", "Sarah", "Fiza", "Humaima"]

input_name = input("Enter name to search in list: ")
input_name_lower = input_name.lower()
list_lower = [name.lower() for name in list1]

if(input_name_lower in list_lower):
    print("Your name is in list: Congratulations! ")
else:
    print("Your name is not in list. Sorry")

