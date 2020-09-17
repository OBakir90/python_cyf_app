
class Person:

    def __init__(self, name):
        self.name=name

    def talk(self):
        print(f'Hi, I`m {self.name}')


person1=Person('Hakan Zahit')

person1.talk()