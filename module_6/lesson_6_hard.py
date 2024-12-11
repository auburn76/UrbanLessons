class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides):
        if isinstance(__sides, tuple):
            self.__sides = __sides
        else:
            print('неверное число сторон')
        if isinstance(__color, tuple):
            self.__color = __color
        else:
            print('неверно указан цвет')
        self.filled = False # атрибут закрашивания

    def get_color(self):
        print(f'RGB код цвета {self.__color}')

    def get_sides(self):
        print(f'Стороны фигуры {self.__sides}')

    def __is_valid_color(self, *new_color):
        if not isinstance(new_color, tuple):
            return False
        if len(new_color) != 3:
            return False
        for i in new_color:
            if i not in range(0, 256) and not isinstance(i, int):
                return False
        return True

    def __is_valid_sides(self, *new_sides):
        if not isinstance(new_sides, tuple):
            return False
        if len(new_sides) != len(self.__sides):
            return False
        for i in new_sides:
            if i <= 0 and not isinstance(i, int):
                return False
        return True

    def set_color(self, *new_color):
        if self.__is_valid_color(*new_color):
            self.__color = new_color
        else:
            print('неверно указан цвет')

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) and len(new_sides) == self.sides_count:
            self.__sides = new_sides
        else:
            print('неверное число сторон')

    def __len__(self):
        return sum(self.__sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        if len(__sides) == self.sides_count:
            super().__init__(__color, *__sides)
            self.__radius = self.__sides[0] / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.__radius**2

class Triangle(Figure):
    sides_count = 3

    def __init__(self,  __color, *__sides):
        super().__init__(__color, *__sides)

    def get_square(self):
        return (self.__len__()/2 * (self.__len__()/2 - self.__sides[0]) *
                (self.__len__()/2 - self.__sides[1]) *(self.__len__()/2 - self.__sides[2]))**0.5


class Cube(Figure):
    ides_count = 12

    def __init__(self,  __color, *__sides):
        super().__init__(__color, *__sides)

    def get_volume(self):
        return self.__sides[1] * self.__sides[2] * self.__sides[3]


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())