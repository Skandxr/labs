number_1 = float(input("Input a number"))
number_2 = float(input("Input another number"))

print("1. Add +\n 2. Subtract -\n 3. Multiply *\n 4. Divide / \n 5. Square s")

choice = str(input("Inout what operation you would like to peform e.g. *, / etc"))

if choice == "+":
    print(f"{number_1} + {number_2} = {number_1 + number_2}")
if choice == "-":
    print(f"{number_1} - {number_2} = {number_1 - number_2}")
if choice == "*":
    print(f"{number_1} * {number_2} = {number_1 * number_2}")
if choice == "/":
    print(f"{number_1} / {number_2} = {number_1 / number_2}")
if choice == "s":
    print(f"{number_1}^{number_1} = {number_1 * number_1}")