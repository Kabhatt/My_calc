def addition(x, y):
    return x + y
def substraction(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

while True:
    choice = input("Please Choose an operation to preform ( 1/2/3/4: )")
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "1":
            print("The Sum is:" + str(int(num1) + int(num2)))
        elif choice == "2":
            print("The difference is:" + str(int(num1) - int(num2)))
        elif choice == "3":
            print("The product is:" + str(int(num1) * int(num2)))
        elif choice == "4":
            if num2 == 0.0:
                print("Divide by 0 Error")
            else:
                print("The Quotient is:" + str(int(num1) / int(num2)))
