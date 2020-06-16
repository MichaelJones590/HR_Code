# This is the solution to the Lists problem on HackerRank
# hackerrank.com/challenges/python-lists/problem
def get_commands(command_num):
    command_list = []
    counter = command_num
    while counter > 0: 
        command = input('Enter valid command: ').lower()
        command_split = command.split()
        index = command_num - counter
        command_list.insert(index, command_split)
        counter -= 1
    return command_list
def run_command(out_list = list(), command_list = list()):
    if command_list[0] == 'insert':
        out_list.insert(int(command_list[1]), int(command_list[2]))
    elif command_list[0] == 'append':
        out_list.append(int(command_list[1]))
    elif command_list[0] == 'remove':
        out_list.remove(int(command_list[1]))
    elif command_list[0] == 'pop':
        out_list.pop()
    elif command_list[0] == 'sort':
        out_list.sort()
    elif command_list[0] == 'reverse':
        out_list.reverse()
    elif command_list[0] == 'print':
        print('\nOutput list is ', out_list)
    else:
        print('Invalid command')
    return out_list
command_array = []
num_commands = int(input('Enter the number of commands: '))
command_array = get_commands(num_commands)
print('Number of commands is: ', str(num_commands))
print('Command array is: ', command_array)
print('Executing commands:')
output_list = []
counter2 = num_commands
while counter2 > 0:
    index2 = num_commands - counter2
    output_list = run_command(output_list, command_array[index2])
    counter2 -= 1