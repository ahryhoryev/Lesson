"""Спортсмен поставил перед собой задачу пробежать в общей сложности Х километров.
В первый день спортсмен пробежал Y километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
Определите номер дня в который спортсмен достигнет своей цели.
Оформите решение в виде программы, которая на вход принимает числа X и Y и выводит номер найденного дня.```"""


def days_for_runner(runner_range: int, day_distance: int):
    """Function for counting days for runner"""
    days_count = 1  # first day
    distance = day_distance
    while runner_range > distance:
        day_distance = day_distance + day_distance * 0.1
        distance += day_distance
        days_count += 1
        print(distance)
    return days_count


def main():
    """Main program to get days for runner with input data"""
    runner_range = int(input("Enter distance (km): "))
    day_distance = int(input("Enter day distance for runner (km): "))
    days = days_for_runner(runner_range, day_distance)
    print(days)


if __name__ == "__main__":
    main()
