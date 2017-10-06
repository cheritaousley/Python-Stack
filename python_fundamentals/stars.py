
# x = [4, 6, 1, 3, 5, 7, 25]
# def draw_stars(list_x):
#     # print "Got into the function!"
#     for num in range(len(list_x)):
#         # print num
#         # print list_x[num]
#         if type(list_x[num])== int:
#             # print "got pass if check!"
#             print list_x[num]* ' *'
# draw_stars([4,6,1,3,5,7,25])

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(list_x):
        # print "Got into the function!"
    for num in range(len(list_x)):
        # print num
        # print list_x[num]
        if type(list_x[num])== int:
            # print "got pass if check!"
            print list_x[num]* ' *'
        elif type(list_x[num])== str:
            print list_x[num][0]
draw_stars(x)