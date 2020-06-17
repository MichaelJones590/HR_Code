# This is the solution to the Swap Case problem on HackerRank
# hackerrank.com/challenges/swap-case/problem
input_string = input('Enter a string to swap: ')
string_length = len(input_string)
while string_length < 0 or string_length > 1000:
    print('Invalid string length.  String must be greater than zero but not more than 1000 characters.')
    input_string = input('Enter a string to swap: ')
    string_length = len(input_string)
modified_string = input_string.swapcase()
print('The swapcase string is:\n', modified_string)