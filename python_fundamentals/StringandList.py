# words = "It's thanksgiving day. It's my birthday, too!"
# print words.find("day")
# print words.replace("day", "month")
  
    

# x= [2,54,-2,7,12,98]
# print max(x)

# x=["hello", 2,54,-2,7,12,98,"world"]
# print x[0] + x[7]

# x=[19,2,54,-2,7,12,98,32,10,-3,6]
# print x.sort()
# print x

x=[19,2,54,-2,7,12,98,32,10,-3,6]
print x.sort()
y=x[:len(x)/2]
z=x[len(x)/2:] 
print y
print z
y.append(z)
print y