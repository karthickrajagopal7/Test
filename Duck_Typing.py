class PyCharm:
    def execute(self):
        print("Compiling")
        print("Runing")

class Myeditior:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Runing")

class Laptop:
    def code(self,ide):
        ide.execute()

ide=Myeditior()
lap1=Laptop()
lap1.code(ide)
