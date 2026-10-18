num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
operation = input("Enter operation (+, -, *, /, %, **):")
if operation == "+" :
    result = num1 + num2
elif operation == "-" :
    result = num1 - num2
elif operation == "*" :
    result = num1 * num2
elif operation == "/" :
    if num2 !=0 :
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed!"
elif operation == "%" :
    result = num1 % num2
elif operation == "**" :
    result = num1**num2
else:
    result = "Invalid operation"
print("Result:", result)


binary = input("Enter a binary number:")

decimal = 0
power = 0
index = len(binary)-1

while index >=0  :
    if binary[index] == "1" :
         decimal = decimal + (2 ** power)

    power = power + 1
    index = index - 1

print("Decimal:", decimal)    


number  =  int(input("Entera  decimal number:"))
binary  = ""
temp = number
if temp == 0 :
    binary = "0"
else:
    while  temp > 0:
        remainder =   temp % 2
        binary = str(remainder) + binary
        temp = temp//2

print("Binary:", binary)