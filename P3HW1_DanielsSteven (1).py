# StevenDaniels
# 7/7/2024
# P3HW1
# DEBUG
 
mod_1 = float (input('Enter grade for Module 1: '))
mod_2 = float (input('Enter grade for Module 2: '))
mod_3 = float (input('Enter grade for Module 3: '))
mod_4 = float (input('Enter grade for Module 4: '))
mod_5 = float (input('Enter grade for Module 5: '))
mod_6 = float (input('Enter grade for Module 6: '))
print(' ')

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sumof = sum(grades)
avg = sum(grades)/len(grades)

print('--------Results------- ')
print('Lowest Grade: ', ("{:.2f}".format(low)))
print('Highest Grade: ', ("{:.2f}".format(high)))
print('Sum of Grades: ', ("{:.2f}".format(sumof)))
print('Average: ', ("{:.2f}".format(avg)))
print('------------------------ ')

# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg < 60:
    print('Your grade is: F')




