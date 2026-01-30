def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

n1 = int(input("Enter a number: "))
operator = input("Enter a operator a choice of +, -, *, /: ")
n2 = int(input("Enter another number: "))

if operator == "+":
    print(calculator[operator](n1, n2))

if operator == "-":
    print(calculator[operator](n1, n2))

if operator == "*":
    print(calculator[operator](n1, n2))

if operator == "/":
    print(calculator[operator](n1, n2))
