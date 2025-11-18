num = int(input("Enter a number: "))

reverse_num = 0

temp = num

while temp > 0:
    digit = temp % 10
    reverse_num = reverse_num * 10 + digit
    temp //= 10

print("Reversed number:",reverse_num)