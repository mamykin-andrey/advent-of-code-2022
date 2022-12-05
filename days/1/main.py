from utils.fileutils import *


def main():
    input_file_name = get_relative_file_path('days/1/input.txt')
    calories = read_all_lines(input_file_name).split("\n")
    joined_calories = __join_calories(calories)
    print(__find_max_calories(joined_calories))


def __find_max_calories(calories: list[int]) -> int:
    # PriorityQueue is a better option
    return sorted(calories, reverse=True)[:3]


def __join_calories(all_calories: list[str]) -> list[int]:
    calories_amount = 0
    joined_calories = []
    for calories in all_calories:
        if calories:
            calories_amount += int(calories)
        else:
            joined_calories.append(calories_amount)
            calories_amount = 0
    joined_calories.append(calories_amount)
    return joined_calories


if __name__ == '__main__':
    main()
