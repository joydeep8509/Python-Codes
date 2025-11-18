matrix = [[1, 2, 3, 4], 
	[5, 6, 7, 8],
	[9, 8, 5, 1]]

# print("Matrix =", matrix)
for row in range(3):
	for column in range(4):
		print(matrix[row][column], end=" ")
	print()