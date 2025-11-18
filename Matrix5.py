## Program to add two matrices using nested loop
X = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 7, 9], [8, 10, 12]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

## iterate through rows
for row in range(len(X)):  ##len(x)=will return the row size

	## iterate through columns
	for column in range(len(X[0])):      ##len(x[0])=will return the column size
		result[row][column] = X[row][column]+ Y[row][column]   ##sum
		# result[row][column] = Y[row][column]- X[row][column]     ##sub

# for r in result:
# 	print(r)
	
print("\n")
for row in range(3):
	for column in range(3):
		print(result[row][column], end="  ")
	print()