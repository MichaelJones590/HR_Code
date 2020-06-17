# This is the solution to the Runner Up problem on HackerRank
# hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
#
# Get the number of integers (scores) to check from user
num_scores = int(input('Enter the number of scores (must be between 2 and 10): '))
while num_scores < 2 or num_scores > 10:
    print('Invalid number of scores.  Number must be an integer between 2 and 10:')
    num_scores = int(input('Enter the number of scores (2-10): '))
#
# Get the input string of scores
input_scores = ""
scores_list_str = []
valid_scores = False
while valid_scores == False:
    input_scores = input('Enter the scores separated by blanks (between -100 and 100):')
    scores_list_str = input_scores.split()
    scores_list_int = []
    index = int(0)
    while index < num_scores:
        score = int(scores_list_str[index])
        if score < -100 or score > 100:
            print('Invalid entry.  Scores must be between -100 and 100.')
            valid_scores = False
            index = num_scores
        else:
            scores_list_int.insert(index, score)
            valid_scores = True
            index += 1
#
# Sort scores and find the runner up
scores_list_int.sort(reverse=True)
index1 = int(0)
index2 = int(1)
runner_up_score = int(0)
while index1 < num_scores:
    if scores_list_int[index2] < scores_list_int[index1]:
        runner_up_score = scores_list_int[index2]
        break
    else:
        index1 += 1
        index2 += 1
print('Runner-up score is: ', runner_up_score)
