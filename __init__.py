class computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print(self.cpu, self.ram)

    def config(self):
        print(self.cpu, self.ram)

com1 = computer('i5', 16)
com2 = computer('i10', '128gb')

com1.config()
com2.config()