import random

from Topic import Topic


class MathTopic(Topic):

    def make_addition_question(self):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        point = 0
        user_answer = input(str(num1) + " + " + str(num2) + " = ")
        if int(user_answer) == (num1 + num2):
            point = 1
        return point

    def make_subtraction_question(self):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        while num2 > num1:
            num2 = random.randint(0, 100)
        point = 0
        user_answer = input(str(num1) + " - " + str(num2) + " = ")
        if int(user_answer) == (num1 - num2):
            point = 1
        return point

    def make_multiplication_question(self):
        num1 = random.randint(0, 12)
        num2 = random.randint(0, 12)
        point = 0
        user_answer = input(str(num1) + " x " + str(num2) + " = ")
        if int(user_answer) == (num1 * num2):
            point = 1
        return point

    def make_division_question(self):
        num1 = random.randint(0, 100)
        num2 = random.randint(1, 100)
        while (num1 < num2) or ((num1 % num2) != 0):
            num2 = random.randint(1, 100)
        point = 0
        user_answer = input(str(num1) + " / " + str(num2) + " = ")
        if int(user_answer) == (num1 / num2):
            point = 1
        return point
