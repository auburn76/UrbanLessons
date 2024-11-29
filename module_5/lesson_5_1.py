class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1:
            print('Такого этажа не существует')
        elif new_floor > self.number_of_floors:
            print(f'В нашем ЖК "{self.name}" только {self.number_of_floors} этажей')
        else:
            print('Едем по этажам: ')
            for i in range(1, new_floor + 1):
                print(i, 'этаж')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)