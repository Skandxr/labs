

integer = int(input("enter a number: "))

factorial = 1
while integer > 1:
    factorial *= integer
    integer -= 1
print("factorial: ", factorial)
#while integer