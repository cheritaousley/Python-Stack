# def about_me():
#     "name" = "Cherita"
#     "age" = "26"
#     "country_of_birth" = "USA"
#     "favorite_language"= "Python"
# print about_me()

# dict= {'name': 'Cherita', 'age':'26', 'country_of_birth': 'USA', 'favorite_language': 'Python'}
# print "My name is", dict['name']
# print "My age is", dict['age']
# print "My country of birth is", dict['country_of_birth']
# print "My favorite language is", dict["favorite_language"]

# def about_me():
#     for x in dict:
#         print dict['name']
#         print dict['age']
#         print dict['country_of_birth']
#         print dict["favorite_language"]
# about_me()
my_dict= {'name': 'Cherita', 'age':'26', 'country_of_birth': 'USA', 'favorite_language': 'Python'}
def about_me(data):
    for key in data:
        print data[key] , "is" , "the", key
about_me(my_dict)