import math


class Figure:
    sides_count = 0

    def __init__(self, __sides, __color, filled=False):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        if len(self.__sides) != self.sides_count:
            self.sides = [1] * self.sides_count

    def __is_valid_color(self, r, g, b):
        if not all(isinstance(x, int) for x in (r, g, b)):
            return False
        if not all(0 <= x <= 255 for x in (r, g, b)):
            return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                if i < 0:
                    return False
            return True
        else:
            return False

    def set_sides(self, *args):
        if self.__is_valid_sides(*args) is True:
            self.__sides = list(args)

    def get_sides(self, index):
        if 0 <= index < self.sides_count:
            return self.__sides[index]
        else:
            return None



    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(sides, color)
        self.__radius = sides[0] / 2 * math.pi
        self.__square = 0

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides
        self.__height = 0
        self.__square = 0
        self.__perimeter = sum(sides) / 2
        self.__a = self.__sides[0]
        self.__b = self.__sides[1]
        self.__c = self.__sides[2]

    def get_square(self):
        # Возвращает площадь треугольника используя формулу Герона
        self.__square = (self.__perimeter * (self.__perimeter - self.__a)
                         * (self.__perimeter - self.__b)
                         * (self.__perimeter - self.__c)) ** 0.5
        return self.__square

    def calculate_height(self, side):
        if side == "a":
            side = 2 * self.get_square() / self.__a
        elif side == "b":
            side = 2 * self.get_square() / self.__b
        elif side == "c":
            side = 2 * self.get_square() / self.__c
        return side


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = [sides[0]] * 12

    def get_volume(self):
        return self.__sides[0] ** 3

    def get_sides(self, index):
        return self.__sides

circle1 = Circle((200, 200, 100), [10])  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), [6])
triangle1 = Triangle((122, 35, 234), [5, 4, 6])
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)# Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)# Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)# Не изменится
print(cube1.get_sides(0))
circle1.set_sides(15)# Изменится
print(circle1.get_sides(0))

# Проверка периметра (круга), это и есть длина:

print(len(circle1))
print(len(triangle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка объема и высоты треугольника
print("Объем треугольника = ", triangle1.get_square())
print("Высота a:", triangle1.calculate_height("a"))
print("Высота b:", triangle1.calculate_height("b"))
print("Высота c:", triangle1.calculate_height("c"))

# проверка площади круга
print("Площадь круга:", circle1.get_square())
