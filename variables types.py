class car:
    wheels = 5

    def __init__(self):
        self.milage = 8
        self.company ='Skoda'

c1 = car()
c2 = car()

car.wheels = 8
print(c1.milage, c1.company, c1.wheels)
print(c2.milage, c2.company, c2.wheels)
