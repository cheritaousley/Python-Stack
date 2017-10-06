# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']

def my_list(l):
   for word in word_list:
    for letter in word:
        if letter == char:
            print word
my_list(new_list)