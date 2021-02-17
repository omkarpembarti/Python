import os

z = open("Pattern-1.py","a")
z.write("After writing")
z.close()

x = open("Pattern-1.py")
print(x.read())
x.close()

if os.path.exists("Omkar.txt"):
    os.remove("Omkar.txt")
else:
    print("File does not exists")