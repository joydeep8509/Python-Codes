## Program to multiply two matrices using nested loops


X = [[1,2],
    [3,4]]


Y = [[5,6],
    [7,8]]


result = [[0,0],
         [0,0]]



for i in range(len(X)):

   for j in range(len(Y[0])):

       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
print("\n\n")

for row in range(2):
	for column in range(2):
		print(result[row][column], end="     ")
	print("\n")