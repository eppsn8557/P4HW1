# CTI-110
# P4HW1 - Score List
# Nadia Epps
# 12 November 2023
#
num_scores = int(input("How many scores do you want to enter? "))
score_list = []

for i in range(num_scores):
    while True:
        score = int(input(f"Enter score #{i+1}: "))
        if score >= 0 and score <= 100:
            score_list.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")

lowest_score = min(score_list)
score_list.remove(lowest_score)
average_score = sum(score_list)/len(score_list)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return"B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

grade = calculate_grade(average_score)
print()
print()
print("--------------Results-----------")
print(f"Lowest score  :  {lowest_score:.1f}")
print("Modified List :  [{}]".format(' , ' .join(map(str, score_list))))
print("Scores Average:  {:.2f}".format(average_score))
print("Grade         : ", grade)
print("----------------------------------")


