#!/usr/bin/env python
# coding: utf-8

# In[1]:


#11. Write a python program to find the factorial of a number.
def factorial(n): 
      
    if (n==1 or n==0):
          
        return 1
      
    else:
          
        return (n * factorial(n - 1)) 
  
# Driver Code 
num = 5; 
print("number : ",num)
print("Factorial : ",factorial(num))


# In[2]:


#12.Write a python program to find whether a number is prime or composite.
number = int(input("Enter The Number"))

if number > 1:
    for i in range(2,int(number/2)+1):
        if (number % i == 0):
            print(number, "is not a Prime Number")
            break
    else:
        print(number,"is a Prime number")
# If the number is less than 1 it can't be Prime    
else:
    print(number,"is not a Prime number")


# In[3]:


#13.Write a python program to check whether a given string is palindrome or not.
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
    


# In[5]:


#14.Write a Python program to get the third side of right-angled triangle from two given sides.
def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
       
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# In[6]:


#15.Write a python program to print the frequency of each of the characters present in a given string.
string=input("Enter the string ")
freq=[None]*len(string)
for i in range(0,len(string)):
  freq[i]=1
  for j in range(i+1,len(string)):
    if(string[i]==string[j]):
        freq[i]=freq[i]+1
        string=string[:j]+'0'+string[j+1:];
print("Character and their frequency");
for i in range(0,len(freq)):
    if(string[i]!=' ' and string[i]!='0'):
        print(string[i]+"="+str(freq[i]))


# In[ ]:




