# create list of 100 random numbers from 0 to 1000
#import library random for randint function
import random

# create empty list
my_list = []

# create loop 100 times
for i in range(100):
    # add new items to the list of random numbers adding every loop
    my_list.append(random.randint(0,1000))
# print it
print(my_list)

# sort list from min to max
# create loop for the each element of the list
for i in range(len(my_list)):
    # loop for current element to compare with the rest of the elements
    for j in range(i+1, len(my_list)):
        # compare two elements
        if my_list[i] > my_list[j]:
            # swap the current element if it is greater
            my_list[i],my_list[j] = my_list[j],my_list[i]
print(my_list)

# calculate average for even and odd numbers and print both average result in console
sum_even = 0
sum_odd = 0
count_even = 0
count_odd = 0
# create loop for the each element of the list
for i in range(len(my_list)):
    # define if number is even
    if my_list[i]%2 == 0:
        # add value to sum of even numbers
        sum_even = sum_even + my_list[i]
        # increase count of even numbers by one
        count_even = count_even + 1
    # define if number is odd
    elif my_list[i]%2 != 0:
        # add value to sum of odd numbers
        sum_odd = sum_odd + my_list[i]
        # increase count of odd numbers by one
        count_odd = count_odd + 1

# print both average result in console (avoiding division by zero)
try:
    print("avg odd = ",sum_odd/count_odd)
except:
    print("my_list doesn't include any odd elements")

try:
    print("avg even = ",sum_even/count_even)
except:
    print("my_list doesn't include any even elements")

