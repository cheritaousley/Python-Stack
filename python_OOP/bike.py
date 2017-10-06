class Bike(object):
    def __init__(self, price, max_speed):
        print "Maiking a bike"
        self.price=price
        self.max_speed=max_speed
        self.miles=0
    def displayInfo(self):
        print "This bike is"+" "+ str(self.price) + " " + "in USD, with a maximum speed of" + " " + self.max_speed + " " + "and total miles of" + " " + str(self.miles), "miles"
        return self
    def ride(self):
        self.miles += 10 
        print "Riding" + " " +  str(self.miles), "miles"
        return self
    def reverse(self):
        self.miles -= 5
        print "Reversing" + " " + str(self.miles), "miles"
first_bike= Bike(200,"25mph")
print first_bike.price
# first_bike.displayInfo()
# first_bike.ride()
# first_bike.reverse()
first_bike.displayInfo().ride().reverse()