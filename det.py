R=int(input("enter a number"))
C=int(input("enter a number"))
matrix=[]
print("enter the entries row wise")
for i in range(R):
	a=[]
	for j in range(C):	
		a.append(int(input()))
	matrix.append(a)
#print the matrix
for i in range(R):
	for j in range(C):
		print(matrix[i][j], end=" ")
	print()
det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
print("det of a matrix",det)
