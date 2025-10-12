def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

sel = int(input("Select operation (1-4): "))

n1 = get_number("Enter first number: ")
n2 = get_number("Enter second number: ")

if sel == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif sel == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif sel == 3:
    print(n1, "*", n2, "=", mul(n1, n2))
elif sel == 4:
    print(n1, "/", n2, "=", div(n1, n2))
else:
    print("Invalid input")
