import random
random_num=random.randint(60,101)
# print random_num
def scores_grades(num):
    print "Scores and Grades"
    score= random_num
    if score<69 and score>60:
        print score
        print "Your grade is D"
    elif score<79 and score>70:
        print score
        print "Your grade is C"
    elif score<89 and score>80:
        print score
        print "Your grade is B"
    elif score<100 and score>90:
        print score
        print "Your grade is A"
    else: 
        print "You falied"
scores_grades(random_num)