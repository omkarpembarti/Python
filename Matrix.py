Matrix = []

def MatrixTakeInput(r,c):
    for i in range(r):
        a =(input().split())
        Matrix.append(a)

def MatrixPrint(r,c):
    for i in range(r):
        for j in range(c):
            print(Matrix[i][j], end = ' ')
        print('\r')

def MatrixStart():
    row = int(input("Enter no. of rows: "))
    col = int(input("Enter no of cols: "))
    MatrixTakeInput(row,col)
    MatrixPrint(row,col)

MatrixStart()
