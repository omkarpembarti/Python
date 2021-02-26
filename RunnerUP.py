x = int(input())
a = list(map(int,input().split()))
b= a
for i in range(1,x):
    for j in range(x-i):
        if a[j] < a[j+1]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp

for i in range(x):
    if a[i] == a[i+1]:
        continue
    else:
        break

print("WIthout Sort Method-->",a[i+1])
b.sort()
print("With Only Sort Method",b[len(b)-2])
c = list(set(b))
print("With Sort & Set Method",c[len(c)-2])

