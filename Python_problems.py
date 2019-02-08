# problem 1 : asks the user to enter their name and their age. Print out the name and age.
name = input("Enter user name : ")
age = input("Enter user age : ")

print ("User name is :  ",name)
print ("User age is : ",age)




# problem 2 : accepts the radius of a circle from the user and compute the area.
r = float(input ("Enter the radius: "))
p = 3.1416
Area = p *(r**2)
print ("Area is :",Area)





# problem 3: to calculate the sum of three given numbers (accept from the user).
x = float(input("Enter the value of x : "))
y = float(input("Enter the value of y : "))
z = float(input("Enter the value of z : "))
sum = x+y+z

print ("Summation of the given numbers is :",sum)




# problem 4 : accept the base and height of a triangle and compute the area. 
b = float(input("Enter the value of base : "))
h = float(input("Enter the value of height : "))

area = (b*h)/2

print("Area of the triangle is : ",area)


# problem 5 : accepts the user's first and last name and print them in reverse order with a space between them.
first_name = input("Enter user's First name : ")
last_name = input("Enter user's Last Name : ")
print (last_name[::-1] + " " + first_name[::-1])

#or

fname = input("Input your Name : ")
print (fname[::-1])





# problem 6 :accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
numbers = input("Enter some comma-seprated numbers : ")
list = numbers.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)



# problem 7 : display the first and last colors from the following list...color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
print ("The first and last color of the list is : ",color_list[0], color_list[3])



