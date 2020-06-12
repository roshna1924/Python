num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
operation = int(input("Enter 1 for addition\n" "Enter 2 for Subtraction\n" "Enter 3 for multiplication\n" "Enter 4 for division\n"))
def arithmeticOperations(op):
    switcher = {
         1: "Result of addition : " + str(num1 + num2),
         2: "Result of Subtraction : " + str(abs(num1 - num2)),
         3: "Result of multiplication : " + str(num1 * num2),
         4: "Result of division : " + str(num1 / num2)
    }
    print(switcher.get(op, "invalid operation\n"))
arithmeticOperations(operation)