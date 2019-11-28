'''
HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.

gradingStudents has the following parameter(s):

grades: an array of integers representing grades before rounding
'''

import os
import sys

def gradingStudents(grades):
    result = []
    for i in grades:
        remainder = i % 5
        if i >= 38 and remainder >= 3:
            i = i - remainder + 5
        result.append(i)
    return result

if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)
    result = gradingStudents(grades)
    for i in result:
        print(i)