r=int(input("ENTER THE NUMBER OF ROWS:"))
c=int(input("ENTER THE NUMBER OF COLUMNS:"))

matrix1=[]
for var in range(0,r):
    r1=[]
    matrix1.append(r1)
    for var in range(0,c):
        x=int(input("ENTER THE FIRST MATRIX ELEMENT:"))
        r1.append(x)

matrix2=[]
for var in range(0,r):
    r2=[]
    matrix2.append(r2)
    for var in range(0,c):
        y=int(input("ENTER THE SECOND MATRIX ELEMENT:"))
        r2.append(y)
    
print("THE GIVEN MATRIX 1 IS ",matrix1)
print("THE GIVEN MATRIX 2 IS",matrix2)
