# This is the solution to the Shape-Reshape problem on HackerRank
# hackerrank.com/challenges/np-shape-reshape/problem
#
# Get the nine integers from user
import numpy
input_integers = ""
integer_list_str = []
valid_integers = False
while valid_integers == False:
    input_integers = input('Enter the integers for the array separated by blanks:')
    integer_list_str = input_integers.split()
    integer_list_int = []
    index = int(0)
    while index < 9:
        if integer_list_str[index].isdigit() == False:
            print('Invalid entry.  Integers must be entered')
            valid_integers = False
            index = 9
        else:
            user_integer = int(integer_list_str[index])
            integer_list_int.insert(index, user_integer)
            valid_integers= True
            index += 1
#
# Shape the array into a 3x3 array and print it
# print(numpy.shape(integer_list_int))
reshaped_list = numpy.reshape(integer_list_int, (3, 3))
print('Here\'s the 3x3 array:\n')
print(reshaped_list)