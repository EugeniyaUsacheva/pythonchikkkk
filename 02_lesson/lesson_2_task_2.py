#високосный год или нет?
def is_year_leap(year):
    return year % 4 == 0

#год для проверки
year = 2025

#результат
result = is_year_leap(year)

#получение результата
print(f"Год {year}: {result}")
