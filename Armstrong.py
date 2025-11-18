###Armstrong number
num = int(input("Enter a number: ")) 

# #initialize sum
sum = 0

## to find the power                          
times=0
temp=num           
while temp > 0:    
   times=times+1   
   temp//=10       

## find the sum of the cube of each digit
temp = num                        
while temp > 0:
   digit = temp % 10              
   sum += digit ** times ##153        
   temp //= 10                      

# #display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

print(sum)


###153= 1^3+5^3+3^3=1+125+27=153  Armstrong number