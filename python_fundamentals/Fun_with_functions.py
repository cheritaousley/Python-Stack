#number 1
# def odd_even(range):
#     for i in range(1, 2001):
#         if i%2 == 1:
#             print str(i) + ' ' + "this is an odd number"
#         elif i%2 == 0:
#             print str(i) + ' ' + "this is an even number"
# odd_even(range)

#number 2
# my_list=[0,1,2,3]
# def multiply(arr):
#     for num in arr:
#         print (num*5)
# multiply(my_list)

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a, 5)
print b

#number 3
# new_array = []
# def layered_multiples(arr):
    # a=[2,4,5]
    # b=multiply(a,5)
    # print arr
    # for x in arr:
    #     val_arr=[]
    # for i in 
    #     val_array.append(1)
    #     new_array.append(new_array)
    # return arr
# my_list=[0,1,2,3]
# a=[2,4,5]
# x=layered_multiples(my_list(a,3))
# print x
# layered_multiples


def layered_multiples(arr):
    # print arr
    new_array=[]  
    for x in arr: 
        val_arr=[]
        for i in range(0,x):
            val_arr.append(1)
            # new_array.append(val_arr)
            new_array.append(val_arr)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
layered_multiples
# output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]



