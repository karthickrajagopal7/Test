
class student:
    def __init__(self, name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand='HP'
            self.config='i7'
            self.ram=8
        def show(self):
            print(self.brand, self.config, self.ram)
s1 = student('Jaya', 3)
s2 = student('Karthi', 7)
s1.show()

print(s1.lap.brand)
print(s2.lap.config)