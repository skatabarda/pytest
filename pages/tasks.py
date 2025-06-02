# list_a = [1, 5, 7, 10, 15]
import random


# def moreThanFive():
#     for i in list_a:
#         if i >= 5:
#             print(i)
#
# moreThanFive()
#
#
# list_b = [1,3,15]
#
# def commonNums():
#     for i in list_a:
#         if i in list_b:
#             print(i)
# commonNums()
#
#
#
# num1 = int(input("Введите число: "))
#
# def evenNum():
#     if num1 % 2 == 0:
#         print("Число четное")
#     elif num1 % 2 == 1:
#         print("Число нечетное")
#     else:
#         print("Вы ввели дробное чилос")
#
# evenNum()
#
# #
# # def palindrome():
# #     user_num = input("Введите число и мы проверим является ли это число палиндромом")
# #     if user_num[-1] == user_num[0]:
# #         print("Число палиндром")
# #     else:
# #         print("Число не палиндром")
# # palindrome()
#
#
#
# def is_palindrome(num):
#     num_str = str(num)
#     return num_str == num_str[::-1]
#
# def main():
#     user_input = input("Введите число и мы проверим, является ли оно палиндромом: ")
#     try:
#         number = int(user_input)
#         if is_palindrome(number):
#             print(f"{number} — палиндром.")
#         else:
#             print(f"{number} — не палиндром.")
#     except ValueError:
#         print("Ошибка! Вы ввели некорректное число.")
#
# if __name__ == "__main__":
#     main()

# def say_hi():
#         name = input("Как вас зовут?: ")
#         print(f"Привет,{name}!")
#
# say_hi()


def guess_random_num():
    random_num = random.randint(1,5)
    user_guest = int(input("Угадайте число от 1 до 5: "))
    if user_guest == random_num:
        print("Вы угадали!")
    else:
        summ_of_two = random_num  + user_guest
        print(f"Вы не угадали. Сумма вашего числа и загаданного = {summ_of_two} и поэтому число было?: ")
        second_guess = int(input(": "))
        if second_guess == random_num:
            print("Вы угадали")
        else:
            print("Нет же!")


guess_random_num()