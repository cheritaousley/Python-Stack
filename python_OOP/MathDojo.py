# import arithmetic 
# class MathDojo(object):
#     def __init__(self, results):
#         self.results=0
#     def add(self):
#     def subtract(self):

def add_numbers(*num):
    sum=0
    for thing in num:
        sum += thing
    return sum
print add_numbers(5)
print add_numbers(5,6,7)
print add_numbers(5,6,7,8,9,10)
