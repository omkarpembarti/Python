a=0
b=1
x = int(input("Enter the no: "))
print("Fibonacci upto ",x," :",end='')
while a <= x:
    print(a,end=' ')
    c = a+b
    a = b
    b = c
print('\r')

a=0
b=1
counter = 1
print("First ",x,"Fibonacci no: ",end='')
while counter <= x:
    print(a,end=' ')
    c = a+b
    a = b
    b = c
    counter = counter + 1
print('\r')