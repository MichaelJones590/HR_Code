# This is the solution to the Loops problem on HackerRank
# hackerrank.com/challenges/python-loops/problem
int_n = int(0)
while int_n < 1 or int_n > 20:
    int_n = int(input('Enter an integer between 1 and 20: '))
counter = int_n
while counter > 0:
    int_sq = int_n - counter
    print(str(int_sq * int_sq))
    counter -= 1