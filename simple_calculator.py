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


def calculation():
    continue_calculation = True
    n1 = float(input("Enter a number: "))

    while continue_calculation:

        operator = input("Enter a operator a choice of +, -, *, /: ")
        n2 = float(input("Enter another number: "))
        answer = calculator[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {answer}")

        choice = input(
            f"Do you want to continue calculation with {answer}? 'y' or 'n': "
        ).lower()
        if choice == "y":
            n1 = answer
            print("\n" * 2)
        else:
            continue_calculation = False
            print("\n" * 4)
            calculation()


calculation()
