class computer:
    def __init__(self):
        self.name = 'Karthi'
        self.age = 28

    def update(self):
        self.age = 30

c1 = computer()
c2 = computer()

c1.name='Jaya'
c1.age=27

c1.update()

print(c1.name,c1.age)
print(c2.name,c2.age)