class Figures:
    def __init__(self, color, side_a, side_b=0, side_c=0):
        self.side_a = abs(float(side_a))
        self.side_b = abs(float(side_b))
        self.side_c = abs(float(side_c))
        self.color = color

    def painting(self, color):
        if self.color == color:
            return f"Фигура уже цвета {self.color}"
        else:
            self.color = color
            return f"Теперь фигрура цвета {self.color}"


class Triangle(Figures):
    def __init__(self, color, side_a, side_b, side_c):
        super().__init__(color, side_a, side_b, side_c)

    def info_triangle(self):
        return f"Это треугольник со сторонами равными: {self.side_a}, {self.side_b}, {self.side_c} и цветом {self.color}"

    def perimeter(self):
        pt = self.side_a + self.side_b + self.side_c
        return f"Периметр этого треугольника равна {pt}"

    def square(self):
        st = (self.side_a + self.side_b + self.side_c) / 2
        return f"Площадь этого треугольника равна {st}"


class Rectangle(Figures):
    def __init__(self, color, side_a, side_b):
        super().__init__(color, side_a, side_b)

    def info_rectangle(self):
        return f"Это прямоугольник со сторонами: {self.side_a}, {self.side_b}, {self.side_a}, {self.side_b} и цветом {self.color}"

    def perimeter(self):
        pr = 2 * (self.side_a + self.side_b)
        return f"Периметр этого прямоугольника равен {pr}"

    def square(self):
        sr = self.side_a * self.side_b
        return f"Площадь этого прямоугольника равна {sr}"


if __name__ == "__main__":
    fig_t = Triangle("red", 2.1, 2, 4.3)
    print(fig_t.perimeter())
    print(fig_t.square())
    print(fig_t.painting("red"))
    print(fig_t.painting("blue"))
    print(fig_t.info_triangle())

    fig_r = Rectangle("yellow", 2.2, 4)
    print(fig_r.perimeter())
    print(fig_r.square())
    print(fig_r.painting("yellow"))
    print(fig_r.painting("green"))
    print(fig_r.painting("yellow"))
    print(fig_r.info_rectangle())
