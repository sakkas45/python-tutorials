__author__ = 'sakkas'




#sample 1: password
# password="pass"
# answer=input("Please enter the password:")
# if answer==password:
#     print("Welcome friend, you shall pass")
# else:
#     print("You shall not pass!")
#



#sample 2: simple calculator
#Please note that it crashes when you enter string
num1 = eval(input("Number 1:"))
num2 = eval(input("Number 2:"))

#input takes string. eval() converts to int.
#if input not convertible to int then it'll crash.

print("(1) Addition")
print("(2) Substraction")
print("(3) Multiplication")
print("(4) Division")
operator = eval(input("enter your choice(1-4):"))
if operator == 1:
    print(num1, "+", num2, "=", num1 + num2)
elif operator == 2:
    print(num1, "-", num2, "=", num1 - num2)
elif operator == 3:
    print(num1, "-", num2, "=", num1 * num2)
elif operator == 4:
    print(num1, "-", num2, "=", num1 / num2)
else:
    print("error")