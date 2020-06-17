# This is the solution to the Nested Lists problem on HackerRank
# hackerrank.com/challenges/nested-list/problem
from operator import itemgetter
num_students = int(input('Enter the number of students (2 to 5): '))
while num_students < 2 or num_students > 5:
    num_students = int(input('Enter the number of students (2 to 5): '))
counter = num_students
all_students_list = []
student_score_list = []
while counter > 0:
    student_name = input('Enter the name of the student: ')
    student_score = float(input('Enter grade for student: '))
    student_score_list.insert(0,student_name)
    student_score_list.insert(1,student_score)
    index = num_students - counter
    all_students_list.insert(index, student_score_list)
    student_score_list = []
    counter -= 1
sorted_students = sorted(all_students_list, key=itemgetter(1,0))
index1 = int(0)
index2 = int(1)
second_lowest_score = int(0)
second_lowest_students = ""
while index2 < num_students:
    if second_lowest_score == 0:
        if sorted_students[index1][1] < sorted_students[index2][1]:
            second_lowest_score = sorted_students[index2][1]
            second_lowest_students = '\n' + str(sorted_students[index2][0])
        else:
            pass
    else:
        if sorted_students[index1][1] == sorted_students[index2][1]:
            second_lowest_students = second_lowest_students + '\n' + str(sorted_students[index2][0]) 
        else:
            pass
    index1 += 1
    index2 += 1
print('\nSecond lowest student(s):', second_lowest_students)