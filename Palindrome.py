#Palindrome number
num = int(input("Enter the number :"))
temp = num       
reverse = 0
while temp > 0:
    remainder = temp % 10                 
    reverse = (reverse * 10) + remainder  ## 121
    temp = temp // 10                      
print("Reverse of the number:",reverse)

if num == reverse:    
  print('Palindrome')
else:
  print("Not Palindrome")