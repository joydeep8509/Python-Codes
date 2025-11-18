X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\n")
for row in range(3):
	for column in range(3):
		print(X[row][column], end=" ")
	print()
	
print("\n")   
row = column = 1

X[row][column] = 11

print(X)
print("\n")

for row in range(3):
	for column in range(3):
		print(X[row][column], end=" ")
	print()