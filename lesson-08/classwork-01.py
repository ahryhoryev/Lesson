# Дан список словарей. Каждый словарь описывает машину (серийный номер, цвет и год выпуска).
# Создать функцию, которая возвращает новый список со всеми машинами, год выпуска которых больше Х.

# Написать декоратор, который будет выводить на печать время выполнения функции из предыдущей задачи (end_time - start_time).
import datetime


def my_decorator(func):
    def timer(year):
        start_time = datetime.datetime.now()
        result = func(year)
        end_time = datetime.datetime.now()
        print(end_time - start_time)
        return result

    return timer


@my_decorator
def filter_cars(year):
    car_list = [
        {"sn": 4435, "color": "red", "year": 1998},
        {"sn": 6935, "color": "green", "year": 2010},
        {"sn": 567, "color": "black", "year": 2000},
        {"sn": 1185, "color": "grey", "year": 2020}
    ]
    result = []
    for car in car_list:
        if car["year"] > year:
            result.append(car)
    return result


def main():
    year = 2000
    filtered_cars = filter_cars(year)
    print(filtered_cars)


if __name__ == "__main__":
    main()
