import random

class Animal: #Класс животных

    live = True #:живой
    sound = None #звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0 #степень опасности существа

    def __init__(self, speed):
        self.speed = speed
        self._coords = [0, 0, 0]  # Координаты

    def move(self, dx, dy, dz):
        self._coords[0] += dx * self.speed
        self._coords[1] += dy * self.speed
        if self._coords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._coords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0" )

    def speak(self):
        if self.sound != None:
            print(self.sound)

class Bird(Animal): #Подкласс птиц

    beak = True #наличие клюва

    def lay_eggs(self):
        print(f"Here are(is) {random.choice(range(1,4))} eggs for you")

class AquaticAnimal(Animal):

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._coords[2] -= abs(dz) * self.speed / 2

class PoisonousAnimal(Animal):

    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):

    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()