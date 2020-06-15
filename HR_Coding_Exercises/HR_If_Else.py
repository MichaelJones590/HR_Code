# This is the "Python If-Else" Exercise on HackerRank
# hackerrank.com/challenges/py-if-else/problem
input_num = input('Enter an integer: ')
while input_num.isdigit() == False:
    input_num = input('Enter an integer: ')
input_int = int(input_num)
if input_int % 2 != 0:
    print('It\'s odd')
else:
    print('It\'s even')
    if input_int >= 2 and input_int <= 5:
        print('Not weird')
    elif input_int >= 6 and input_int <= 20:
        print('Weird')
    elif input_int > 20:
        print('Not weird')
    else:

        pass