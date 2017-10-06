class Animal(object):
    def __init__(self, name):
        self.name=name
        self.health=10
    def walk(self):
        for i in range(1,4):
            self.health -=1
        print "I am walking and now my is has decreased to", self.health
        return self
    def run(self):
        for i in range(1,3):
            self.health -=5
        print "I am running and now my is has decreased to", self.health, "I am tired, whew"
        return self
    def fly(self):
        self.health -=10
        print "I am flying and now my is has decreased to", self.health
        return self
    def display_health(self):
        print "Hi, I am a" + " " + self.name + " " + "with a health of" + " " + str(self.health)
class Dog(Animal):
    def __init__(self, name):
        self.name=name
        self.health=150
class Dragon(Animal):
    def __init__(self,name):
        self.name=name
        self.health=170
# first_animal=Animal("giraffe" )
# first_animal.walk()
# first_animal.run()
# first_animal.display_health()
# dogs_only=Dog("Cobi")
# dogs_only.walk().run().display_health()
drangons_only=Dragon("Beattle")
drangons_only.fly().display_health()