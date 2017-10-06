students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# def students_name(student_list):
#     for student in student_list:
#         print student
#         for info in student:
#             print info
#             for val in info:
#                 print val
# students_name(students)

#correct way
# def students_name(student_list):
#     for student in student_list:
#         print student['first_name'], student["last_name"]
# students_name(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def students_instructors(students_instructors_names):
    for users in students_instructors_names:
        print users
        users_list= students_instructors_names[users]
        # print users_list
        count=0
        for person in users_list:
            # print person
            # message= ""
            char_count=len(person['first_name'])+ len(person['last_name'])
            count += 1
            message= str(count) + " "
            for key in person:
                # print key
                 message= message +"-" + " " + person[key] 
            print message +" "+ "-" + str(char_count)
        # if users == 'Students':
        #     print students[0]
        # elif users == 'Instructors':
        #     print instructors[0]
students_instructors(users)