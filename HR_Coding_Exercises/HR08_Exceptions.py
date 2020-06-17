# This is the solution to the Exceptions problem on HackerRank
# hackerrank.com/challenges/exceptions/problem
#
# Get the number of test cases from user
test_cases = int(input('Enter the number of test cases: '))
while test_cases < 0 or test_cases > 9:
    print('Invalid number of test cases.  Number must be an integer between 1 and 9.')
    test_cases = int(input('Enter the number of test cases: '))
#
# Get the test-case pairs from the user
test_cases_list = []
index = int(1)
while index <= test_cases:
    test_case = input('Enter test case values separated by a space (example: \"x y\")')
    test_cases_list.insert(index, test_case)
    index += 1
#
# Process the test-case pairs trapping errors and printing results
index = 0
while index < test_cases:
    split_string = test_cases_list[index].split()
    try: 
        print('Result of ', split_string[0], '/', split_string[1], 'is:', int(split_string[0]) / int(split_string[1]))
    except ZeroDivisionError as z:
        print('Error Code:', z)
    except ValueError as v:
        print('Error Code:', v)
    index += 1