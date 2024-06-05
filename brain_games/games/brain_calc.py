import operator
import random


DESCRIPTION = 'What is the result of the expression?.'


def apply_operator(operator_str, num1, num2):
    if operator_str == '+':
        return operator.add(num1, num2)
    elif operator_str == '-':
        return operator.sub(num1, num2)
    elif operator_str == '*':
        return operator.mul(num1, num2)


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator_str = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator_str} {num2}"
    correct_answer = str(apply_operator(operator_str, num1, num2))
    return expression, correct_answer
