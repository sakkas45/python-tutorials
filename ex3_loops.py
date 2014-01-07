__author__ = 'sakkas'




#while loop
#fibonacci sequence with while loop
# a=eval(input("Which fibonacci term do you want to know?:"))
# fib1=1
# fib2=1
# fib=0
# i=0
# while i<a-2:
#     fib=fib1+fib2
#     fib2=fib1
#     fib1=fib
#     i=i+1
# print(fib)

#for loop
#fibonacci sequence with for loop
a=eval(input("Which fibonacci term do you want to know?:"))
fib1=1
fib2=1
fib=1
for i in range (1,a-1):
    fib=fib1+fib2
    fib2=fib1
    fib1=fib
print(fib)