# Steven Daniels
# 7/11/2024
# P4HW1_DanielsSteven
# program is to display a letter grade for the calculated average

# Ask for number of scores user want to enter

score_num = int(input("How many scores do you want to enter? "))

print()
#create empty list

scores = []
# enter scores into the list
# for num in range(0, score_num):

for num in range(1, score_num + 1):
    # collect scores
    score = float(input("Enter score #" + str(num) + ": "))
    # validate entry
    while score < 0 or score > 100:
        print("\nINVALID Score entered!")
        print("Score must be between 0 and 100!")
        score = float(input("Enter score #" + str(num) + ": "))
    scores.append(score)
    



#find lowest score

lowest = min(scores)

scores_modified = scores
#drop lowest score from new list

scores_modified.remove(lowest)


# calculate average

avg = sum(scores_modified)/ len(scores_modified)

# determine letter grade for average



if avg >= 90:

    grade = "A"
elif avg >= 80:

    grade = "B"

elif avg >= 70:

    grade = "C"
elif avg >= 60:

    grade = "D"
else:

    grade = "F"

# display results

print("\n--------------Results-----------")
print("Lowest Score  : {}".format(lowest))
print("Modified List : {}".format(scores_modified))
print("Scores Average: {:.2f}".format(avg))
print("Grade         : {}".format(grade))
print("----------------------------------")







