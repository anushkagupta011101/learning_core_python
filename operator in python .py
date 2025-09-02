#----------------------------------------------------------------------------------------------------------------------------------
#author: ANUSHKA GUPTA

#---------------------------------------------------------------------------------------------------------------------------------

#*********************************************** OPERATORS ******************************************************************




# Arithematic operation {+,_,*,/,%,//,**}

# (+): it shows the addition of two or more than two numbers
# x=56
# y=78
# z=x+y
# print(z)


# (-): it shows the subtraction of two numbers
# x=100
# y=67
# z=x-y
# print(z)

# (*): it shows the multiplication of two numbers
# x=34
# y=6
# z=x*y
# print(z)

#(/): it shows the division 
# x=56
# y=7
# z=x/y
# print(z)    #gives float 
# print(int(z))     # gives integer



# # % modules: it shows reminder

# # x=25
# # y=25
# # z=x%y
# # print(z)

# # // float division: it shows value before the decimal after division
# print(10//4)

# # **: it adss power or any number like square,cube and custom
# x=9
# print(x**2)

# # write a python code program to show the area of circle with radius 14c,

# # x=14
# # a=22/7*(x*x)
# # print(a)


# # python follows BODMAS rule
# # x=10
# # y=2
# # z=3
# # s=x+y*z/2

# # print(s)

#-----------------------------------------------------------------------------------------------------------------------

comparison operator
 		operator 				name
 		>						greater than
 		<						less than
 		==						equal to
 		!=						not equal to
 		>=						greater than or equal to
 		<=						less than or equal to'''

#greator than  (>)
'''x=12
y=10
if x<y:
	print("true")
elif x<y:
	print("this is right")
else:
	print("nothing is true")'''

#less than  (<)
'''x=45
y=15
if x<y:
	print("this is true")
elif x>y:
	print("prince is right")'''


# equal to (==)
'''x=67
z=67
y=67
if x==y==z:
	print("chhotu")'''
# not equal to  (!=)
'''x=23
y=23
z=34
if x==y==z:
	print("yes")
elif x==y!=z:
	print("true")
#greator than or equal to /less than or equal to
x=10
y=12
z=12
if y>x and y==z:
	print("this is true")'''
#[note:- we can use elif or else on condition]


'''Python assigment operators
 =	assign
+=	add and assign
-=	substract and assign
*=	multiplication and assign
/= 	divide and assign
%=	modules and assign
**= exponentation and assign
//= floor divison and assign'''

 # assign   (=)
'''x=13
x+=12
print(x)
#sbstraction and assign
x=25
x-=30
print(x)
#multiplication and assign
x=10
x*=15
print(x)
#divison and assign
x=15
x/=5
print(x)
#modulus and assign
x=30
x%=8
print(x)
#Floor divisiable and assign
x=45
x//=8
print(x)
#Exponentation and assign
x=6
x**=3
print(x)'''


#Logical Operators: 
# 1: and: if both conditions are true it will show true, and if any statment is wrong then it will show False
# 2: or: if any of the condition is true , it will show true.
# 3: not: not true= false, not false: True  ... it reverse conditions of And, or

#WAP to print a number is between 20 5o 50 then show yes else show no
# x= int(input("enter any number:"))
# if x>=20 and x<=50:
#     print("yes")
# else: 
#     print("no")


# WAP to show if textis "a" or "b" thenshow yes

# x=str(input("enter any text:"))
# if x=="a" or x=="b":
#   print("yes")
# else:
#   print("no")



# MEMBERSHIP OPERATOR:  in and not in
# in : it return True when value is in text
# not in : it return True when value is not in text


#WAP to show the status if text contain "a" show yes else no
# x=input("enter any text:")
# if "a" in x:
#     print("yes")
# else:
#     print("no")

#WAP to check if alphabet is vowel then print("vowel")else "consonant"


# x=input("enter any text:")
# if "aeiou" in x :
#     print("yes",x)
# else:
#     print("no")


# membership operators:  in and not in
# in : it return True when value is in text
# not in : it return True when value is not in text


#WAP to show the status if text contain "a" show yes else no
# x=input("enter any text:")
# if "a" in x:
#     print("yes")
# else:
#     print("no")

#WAP to check if alphabet is vowel then print("vowel")else "consonant"


# x=input("enter any text:")
# if "aeiou" in x :
#     print("yes",x)
# else:
#     print("no")


# Logical Operators: 
# 1: and: if both conditions are true it will show true, and if any statment is wrong then it will show False
# 2: or: if any of the condition is true , it will show true.
# 3: not: not true= false, not false: True  ... it reverse conditions of And, or

#WAP to print a number is between 20 5o 50 then show yes else show no
# x= int(input("enter any number:"))
# if x>=20 and x<=50:
#     print("yes")
# else: 
#     print("no")


# WAP to show if textis "a" or "b" thenshow yes

# x=str(input("enter any text:"))
# if x=="a" or x=="b":
#   print("yes")
# else:
#   print("no")

# conditional statement: it is an important funtion in python which is used print the statment by condition
# #                       there are three block in python
# #1: if  2: elif   3:else



# # write a python program to print the if number is greater than 50 then show less Yes else show no
  

# x=25
# if x>50:
#     print("number is greater than 50")
# else: 
#     print("number is less than 50")


# #---------------------------------------------------------------------------

 # user input: used to accept the values from user. result of the input() is alaa

 # x= int(input("enter any number:"))
 # if x>100:
 #     print(x,"yes")
 # else: 
 #     print(x,"n0")



 # write a python program to check the number is less than 100 then print" below 100" else "above 100"

 # x=int(input("enter any number:"))
 # if x<100:
 #     print(x,"below 100")
 # else:
 #     print(x,"above100")


 # write a python program with the help of user input to check the number is even or odd
 # x=int(input("enter any value:"))
 # if x%2==0:
 #     print(x,"even")
 # else:
 #     print(x,"odd")


 # write a python program with help of user input to show the status if number is greater than 3 digit then show yes else no

 # x= int(input("enter any number:"))
 # if x>=100:
 #     print(x,"yes")
 # else:
 #     print(x,no)

 #-----------------------------------------------------------------------------------------------
 # income tax calculator
 # write a python program to show the interest by anual incomee
 # income= float(input("enter any number:"))
 # if income<300000:
 #     print("no tax")
 # elif income<700000:
 #     print("5%",income*0.05)
 # elif income<1000000:
 #     print("10%",income*0.1)
 # elif income<1200000:
 #     print("15%",income*0.15)
 # elif income<1500000:
 #     print("20%",income*0.2)
 # else:
 #     print("30%",income*0.3)

 # color= input("enter any color:")
 # if (color =="red"):
 #     print("stop")
 # elif (color== "green"):
 #     print("go")
 # elif (color== "yellow"):
 #     print("ready to go")
 # else:
 #     print("nothing")








# WaP to check if number between 1 to 20 then show "low", if number between 20 to 30 then show "mid",else high

# # x= int(input("enter any number:"))
# # if 1<=x<20:
# #     print(x,"low")
# # elif 20<=x<=30:
# #     print(x,"mid")
# # else:
# #     print(x,"high")



# # 
# # wap with the help of user input to the grade of student by % 
# # if % is greater than 50 then show "grade A"
# #     if % is greater than 80 then show "grade A+
# #         if % is greater than 70 then show "grade B
# #             if % is greater than 60 then show "grade 
# #                 else D


# # x= int(input("enter any number:"))
# # if x>90:
# #     print("Grade A+")
# # elif x>80:
# #     print("Grade A")
# # elif x>70:
# #     print("Grade B")
# # elif x>60:
# #     print("Grade C")
# # else:
# #     print("Grade D")




