# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total = 0

# loops through all in student_heights and adds it to total
for height in student_heights:
    total += height

# loops through all in student_heights and adds to number_of_students giving the number needed for average
number_of_students = 0
for student in student_heights:
    number_of_students += 1

# simple average calc but using round() to get it to the nearest number
average = round(total / number_of_students)
print(average)