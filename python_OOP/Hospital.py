big_hospitals= []
class Hospital(object):
    def __init__(self, name, capacity):
        self.patients=big_hospitals
        self.name=name
        self=capacity
    def admit_patients(self, ID, name, allergies, bed_number):
        Patient(ID, name, allergies, bed_number)
        # print self.patients
        print "I am adding this in the array"
    def display_hospitals(self):
        for things in self.patients:
            print things.ID, things.name, things.allergies, things.bed_number
    def discharge_patients(self,name):
        for x in self.patients:
            print x
            if x.name == name:
                y=self.patients.index(x)
                del self.patients[y]
                print "I am being removed"
    #this discharge isnt working! noe did it work on my call center
class Patient(object):
    def __init__(self, ID, name, allergies, bed_number):
        self.ID=ID
        self.name=name
        self.allergies=allergies
        self.bed_number=bed_number
        self.patient=[]
        big_hospitals.append(self)
        # print big_hospitals

hospital_info=Hospital('Hospital abc', 10)
hospital_info.admit_patients("001", "Jane Doe", "Peanut Allergy","01")
# hospital_info.display_hospitals()
# hospital_info.admit_patients("002", "John Doe", "Cat Allergy", "02")
# hospital_info.display_hospitals()
hospital_info.admit_patients("003", "James Bond", "Bee Allergy", "03")
hospital_info.display_hospitals()
hospital_info.discharge_patients("James Bond")
hospital_info.display_hospitals()