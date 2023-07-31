print("My Calcy welcomes you!")

First = float(input("Enter the first value: "))

# Operator = "+", "-", "*", "/"
operator = input("Enter the operator: ")
if operator not in ("+", "-", "*", "/"):
    print("Error: Operator must be one of the following: +, -, *, /")
else:
    Second = float(input("Enter the second value: "))

    if operator == '+':
        print("The final output is:", First + Second)
    elif operator == '-':
        print("The final output is:", First - Second)
    elif operator == '*':
        print("The final output is:", First * Second)
    else:
        if Second == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("The final output is:", First / Second)
