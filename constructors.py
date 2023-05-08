class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11    # can add or remove this line to change a value
print(point.x)


## exercise ##
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")


john = Person("John Wick")
print(john.name)
john.talk()
