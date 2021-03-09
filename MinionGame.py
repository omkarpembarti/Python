"""
from collections import Counter
s = input().upper()
v = ['A','E','I','O','U']
result = []
stuart = 0
kevin = 0

for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        result.append(s[i:j])
result = Counter(result).items()

for key,value in result:
    if key[0] in v:
        kevin = value + kevin
    else:
        stuart = value + stuart

print(kevin)
print(stuart)

if kevin> stuart:
        print('Kevin',kevin)
if stuart > kevin:
        print('Stuart',stuart)
if kevin==stuart:
        print('Draw')
"""

#BANANA
#012345

s = input().upper()
v = ['A','E','I','O','U']
result = []
stuart = 0
kevin = 0

for i in range(0,len(s)):
    if s[i] in v:
        kevin = (len(s)-i) + kevin
    else:
        stuart = (len(s)-i) + stuart

if kevin>stuart:
    print("Kevin",kevin)
elif stuart>kevin:
    print('Stuart',stuart)
else:
    print('Draw')