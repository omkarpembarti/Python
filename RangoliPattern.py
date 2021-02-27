"""
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""

n = int(input())

for i in range(n,0,-1):
    for space in range(i-1,0,-1):
        print(end='--')
    for reverse in range(n,i-1,-1):
        if i == n:
            print(chr(97+reverse-1),end='')
        else:
            print(chr(97+reverse-1),end='-')
    for straight in range(i+1,n+1):
        if straight == n:
            print(chr(97+straight-1),end='')
        else:
            print(chr(97+straight-1),end='-')
    for space in range(i-1):
        print(end='--')
    print()
for i in range(2,n+1):
    for space in range(1,i):
        print(end='--')
    for reverse in range(n,i-1,-1):
        if i == n:
            print(chr(97+reverse-1),end='')
        else:    
            print(chr(97+reverse-1),end='-')
    for straight in range(i+1,n+1):
        if straight == n:
            print(chr(97+straight-1),end='')
        else:
            print(chr(97+straight-1),end='-')
    for space in range(i-1):
        print(end='--')
    print()
