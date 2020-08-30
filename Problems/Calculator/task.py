# put your python code here
num1 = float(input())
num2 = float(input())
oper = input()

if oper == "+":
    res = num1 + num2
elif oper == "-":
    res = num1 - num2
elif oper == "/":
    if num2 == 0:
        res = "Division by 0!"
    else:
        res = num1 / num2
elif oper == "*":
    res = num1 * num2
elif oper == "mod":
    if num2 == 0:
        res = "Division by 0!"
    else:
        res = num1 % num2
elif oper == "pow":
    res = num1 ** num2
elif oper == "div":
    if num2 == 0:
        res = "Division by 0!"
    else:
        res = num1 // num2

print(res)
