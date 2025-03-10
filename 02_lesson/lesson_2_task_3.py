import math

#вычисление площади кввдрата
def square(side):
    area = side ** 2
    return math.ceil(area)

#сторона для проверки
side = 6.5
result = square(side)

#получение результата
print(f"Площадь квадрата со стороной {side}: {result}")