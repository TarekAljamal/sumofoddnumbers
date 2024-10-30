
# A python code that requests the user to enter a number x to calculate the sum of odd numbers from 1 to x

x = input("Enter the number x to calculate the sum from to x: ") # request the user to enter a number and stores in x
sum=0 # Hold the sum of odd numbers from 1 to x, initialized with value zero

for x in range(1,int(x)+1,1): # Checks all numbers from 1 to x and adds the odd ones in sum
    if(x%2!=0):
      sum += x

print(sum) # Prints the sum of odd numbers 
