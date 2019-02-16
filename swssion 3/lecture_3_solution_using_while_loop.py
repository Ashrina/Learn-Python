#1. Print all the even number from 1 to 50.

i=1
while i<=50:
    if i%2==0:
        print (i)
    i=i+1



#2. Take an integer input from the user, and use that integer to make a table as output.






#3. Make multiplication tables for 1 to 20.

n=1
while n<=20:
    i=1
    print("\n namta",n,"\n")
    while i<=10:
        print(i,"X",n,"=",i*n)
        i=i+1
     
    n=n+1


#4. Write a program to find factorial of an input.

i = int(input("Enter a number: "))
def factorial (i):
    j = 1
    while i >= 1:
        j = j*i
        i=i-1
    return j
print ("The factorial of",i,"is",factorial(i))



#5. Take an integer as input and show if it’s prime or not.

i=2
num=int(input("enter number:"))
while i<=num:
    if (num%i)==0:
        print (num, "is not a prime number.")
        i = i + 1
    else:
        print (num, "is a prime number.")
        break



