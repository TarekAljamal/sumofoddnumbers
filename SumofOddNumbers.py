
# A python code that requests the user to enter a number x to calculate the sum of odd numbers from 1 to x

x = input("Enter the number x to calculate the sum from to x: ")
sum=0 

for x in range(1,int(x)+1,1): # Checks all numbers from 1 to x and adds the odd ones in sum
    if(x%2!=0):
      sum += x

print(sum)
