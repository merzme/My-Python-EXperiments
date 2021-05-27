
def add(firstValue,secondValue):
    result = firstValue+secondValue
    print(result)

def sub(firstValue, secondValue):
    result = firstValue-secondValue
    print(result)

def mul(firstValue, secondValue):
    result = firstValue*secondValue
    print(result)

def div(firstValue,secondValue):
    result = firstValue/secondValue
    print(result)


operator = input("enter the operator:")
firstValue = int(input("enter the first values: "))
secondValue = int(input("enter the second value:"))

if operator=="+":
    add(firstValue, secondValue)
elif operator == "-":
    sub(firstValue, secondValue)
elif operator == "*":
    mul(firstValue, secondValue)
elif operator == "/":
    div(firstValue, secondValue)
else:
    print("invalid operation")


