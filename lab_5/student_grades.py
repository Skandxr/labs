data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

import statistics

grades = data.split(',')

print(grades)

grades = list(map(int, grades))

print (f"This is the minimum grade - {min((grades))}")
print (f"This is the maximum grade - {max((grades))}")

print (f"The average grade to 2 d.p is {sum(grades)/len(grades):.2f}")# :.2f to 2 decimal places

print (f"The average of the grades is {statistics.mean(grades)}")
print (f"The median of the grades is {statistics.median(grades)}")

min_grade = min(grades)
max_grade = max(grades)
average_grade = statistics.mean(grades)
median_grade = statistics.median(grades)

print (f"Minimum Grade: {min_grade}\nMaximum Grade: {max_grade}\nAverage Grade: {(average_grade):.2f}\nMedian Grade: {(median_grade):.2f}")
