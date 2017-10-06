class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        print "Making a new car"
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if self.price> 10000:
            self.tax=0.15
        else:
            self.tax=0.12
    def display_all(self):
        print "I am the luxurious car costing", str(self.price), "crusing at a speed of", self.speed , self.fuel, "tank of gas with", self.mileage 
        return self
# new_car=Car(2000,"35mph","full", "15mpg")
# new_car.display_all()
# first_car=Car(2000, "5mph","Not Full", "105mpg")
# first_car.display_all()
# average_car=Car(2000, "15mph", "Kind of Full", "95mpg")
# average_car.display_all()
# mediocre_car=Car(2000, "25mph", "Full", "25mpg")
# mediocre_car.display_all()
poor_car=Car(200, "45mph", "Empty","25mpg")
poor_car.display_all()
# drean_car=Car(20000000, "35mph","Empty", "15mpg", str(self.tax))



