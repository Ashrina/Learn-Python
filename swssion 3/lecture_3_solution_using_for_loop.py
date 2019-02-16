#1. Print all the even number from 1 to 50.

for i in range (2,51,2):
    print (i)



#2. Take an integer input from the user, and use that integer to make a table as output.





#3. Make multiplication tables for 1 to 20.
for i in range (1,21,1):
    print("\n namta",i,"\n")
    for n in range (1,11,1):
        print(i,"X",n,"=",i*n)
        


#4. Write a program to find factorial of an input.

i = int(input("Enter a number: "))
factorial = 1
for n in range(1,i + 1):
    factorial = factorial*n
print("The factorial of",i,"is",factorial)





#5. Take an integer as input and show if it’s prime or not.

num = int(input("Enter any number: "))
if num > 1:   
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(numb, "is not a prime number")

