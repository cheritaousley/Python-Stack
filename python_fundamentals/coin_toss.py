import random
def coin_toss():
    head_count = 0
    tail_count = 0
    toss_count = 0
    for num in range(1,5001):
         toss = random.randint(0,1)
         if toss==0:
             head_count += 1
             toss_count += 1
             print "Attempt #", toss_count, ": Throwing a coin...It's a head!...Got " , head_count, "head(s) so far and" , tail_count, "tail(s) so far"
         else: 
            tail_count += 1
            toss_count += 1
            print "Attempt #", toss_count, ": Throwing a coin...It's a tail!...Got " , head_count, "head(s) so far and" , tail_count, "tail(s) so far"

coin_toss()