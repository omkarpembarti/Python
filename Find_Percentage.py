"""
Sample Input
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 
56.00
"""
import math
collection = {}
x =int(input())
for i in range(x):
    name, *mark = input().split()
    marks = list(map(float,mark))
    collection[name] = marks
name = input()
scoreArray = collection[name]

average = sum(scoreArray)/len(scoreArray)
print("%.2f" % average)