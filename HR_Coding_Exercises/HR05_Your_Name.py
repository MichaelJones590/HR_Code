# This is the solution to the What's Your Name problem on HackerRank
# hackerrank.com/challenges/whats-your-name/problem
first_name = ""
last_name = ""
name_length = int(0)
while name_length == 0:
    first_name = input('Enter your first name: ')
    name_length = len(first_name)
    if name_length > 10:
        print('Name is too long. First and last name cannot be more than 10 characters.')
        name_length = 0
    else:
        last_name = input('Enter your last name: ')
        name_length = name_length + len(last_name)
        if name_length > 10:
            print('Name is too long. First and last name cannot be more than 10 characters.')
            name_length = 0
        else:
            pass
greeting = 'Hello ' + first_name + ' ' + last_name + '! You just delved into python.'
print(greeting)