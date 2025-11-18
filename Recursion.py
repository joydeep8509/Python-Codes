# The term Recursion can be defined as the process of defining something in terms of itself. 
# In simple words, it is a process in which a function calls itself directly or indirectly. 
# Program to print the fibonacci series upto n_terms

# Recursive function
# Program to print factorial of a number
# recursively.

# Recursive function

def tri_recursion(k):                 #function  k=l
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

l=int(input ("Enter the Number : " ))
print("\n\nRecursion Example Results")
tri_recursion(l)