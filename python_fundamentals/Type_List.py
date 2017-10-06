#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# def test_type(value):
#  if type(value) == list:
#     print "That's a list!"
# test_type(l)
# #For each item on the list, print its data type
#     if type(value) == int:
#         print "That's a number"

def test_type(l_list):
    string_flag= False
    int_flag=False
    word_string= "String:"
    sum=0
    for i in l_list:
        print i
        if type(i) == str:
            string_flag= True
        elif type(i) == int:
            int_flag = True
        if type(i)== str:
            word_string= word_string + " " + i
        if type(i)== int:
            sum =sum +i
    if string_flag== True and int_flag== True:
        print "The list  you entered is of mixed type"
    elif string_flag== True:
        print "The list only has string"
    elif int_flag== True:
        print "The list only has numbers"
    print word_string
    print sum
test_type(l)

    