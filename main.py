import math

def perimeter(a, b):
    c2 = a * a + b * b
    c = math.sqrt(c2)
    print(f"Периметр прямоугольного треугольника = {c + a + b}")

def square(a, b):
    print(f"Площадь прямоугольного треугольника = {a * b / 0.5}")

if __name__ == '__main__':
    a = int(input("Введите сторону a: "))
    b = int(input("Введите сторону b: "))
    perimeter(a, b)
    square(a, b)
