

while True:
    i = input("Enter operation: - , + , / , * , **: ")
    if i =='0':
        print("Goodbye")
        break

    if i in ('+', '-', '*', '/', '**'):
         num1 = float(input("Enter first digit: "))
         num2 = float(input("Enter second digit: "))
         if i == '+':
             print("%.2f" % (num1 + num2))
         elif i == '-':
            print("%.2f" % (num1 - num2))
         elif i == '*':
            print("%.2f" % (num1 * num2))
         elif i == '**':
                 print("%.2f" % (num1 ** num2))
         elif i == '/':
            if num2 !=0:
                 print("%.2f" % (num1 / num2))
            else:
                 print("Can't work with 0")

