
#from collections import Collection
no_of_shoes = int(input())
shoe_size = list(map(int,input().split()))
no_of_customers = int(input())
cust_choice = []
profit = 0

for i in range(no_of_customers):
    size , price = input().split()
    cust_choice.append([int(size),int(price)])

print(shoe_size)
print(cust_choice)
for i in cust_choice:
    if i[0] in shoe_size:
        profit = profit + i[1]
        shoe_size.remove(i[0])
print(profit)

#shoe_size = Collection(shoe_size)



