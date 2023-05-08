class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass   #pass means nothing, skip the line.

dog1 = Dog()
dog1.bark()
