#print inputted 7 fruits
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1} ")
    fruits.append(fruit)

print(fruits)

# print inputted 7 marks in sorted manner
marks = []
for i in range(7):
    mark = int(input(f"Enter mark of student {i+1}: "))
    marks.append(mark)

sorted_marks = sorted(marks)
print("After sorting: " , sorted_marks)

#tuple
fisrt_tuple = (1,"Hello", True, 2.13)
print(fisrt_tuple)

#sum of list
list1 = []
for i in range(4):
    num = int(input(f"Enter numbers in list {i+1}: "))
    list1.append(num)
print(list1)
sum_of_list = sum(list1)
print("After sum: " , sum_of_list)

#count 0 in list
list2= [1,9,55,7,0,45,0,4,0]
print("0s in list are: ", list2.count(0))
print("Index of first zero: ", list2.index(0))