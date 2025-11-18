##  Create a matrix using list comprehension 
matrix = [[column for column in range(4)] for row in range(4)]
print(matrix)
print("--------------------------------\n")
for row in range(4):
	for column in range(4):
		print(matrix[row][column], end=" ")
	print()