# This is the solution to the Any or All problem on HackerRank
# hackerrank.com/challenges/any-or-all/problem
#
# Get the number of integers to check from user
num_integers = int(input('Enter the number of integers (1-99): '))
while num_integers < 1 or num_integers > 99:
    print('Invalid number of integers.  Number must be an integer between 1 and 99.')
    num_integers = int(input('Enter the number of integers (1-99): '))
#
# Get the input string of integers
input_integers = input('Enter the integers separated by blanks:')
integer_string = input_integers.split()

# Test the string of integers and print the result
positive_test = []
palindrome_test = []
index = int(0)
while index < num_integers:
    user_int = int(integer_string[index])
    if user_int < 0:
        user_test = False
    else:
        user_test = True
    positive_test.insert(index,user_test)
    if integer_string[index] == str(integer_string[index])[::-1]:
        user_test = True
    else:
        user_test = False
    palindrome_test.insert(index,user_test)
    index += 1
if all(positive_test) and any(palindrome_test):
    print('True.  All integers are positive and at least one is a palindrome.')
else:
    print('False.  Either one integer is negative or there are no palindromes.')