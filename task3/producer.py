import random
import time

def create_expression():
    num1 = random.randint(1, 9)
    operator = random.choice(['+', '-', '*', '/'])
    num2 = random.randint(1, 9)
    return f"{num1} {operator} {num2}"

def main():
    num_expressions = random.randint(120, 180)

    for _ in range(num_expressions):
        expression = create_expression()
        print(expression)
        time.sleep(1)
    main()
