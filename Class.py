class computer:
    def config(self):
        print('I5, 16GB, 1TB')

com1=computer()
com2=computer()

computer.config(com1)
computer.config(com2)

com1.config()
com2.config()


class computer:
    def config(self):
        print('I3, 8GB, 500GB')
 
com1=computer()
computer.config(com1)

a = 2
a.bit_length()