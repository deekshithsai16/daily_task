#Declare variables of the following data types

num=100		#int datatype
print(num)
print(type(num))

fract=181.2	#float datatype
print(fract)
print(type(fract))

char='VJ'	#str datatype
print(char)
print(type(char))

mass_1=50	#bool datatype
mass_2=60
res=mass_1>mass_2 and mass_2>mass_1
print(res)
print(type(res))

#Arithmetic Operators
num_1=10
num_2=10
print("num_1 : ",num_1)
print("num_2 : ",num_2)
sum=num_1+num_2
print("sum of num_1+num_2 is : ",sum)	#additiom
sub=num_1-num_2
print("sub of num_1-num_2 is : ",sub)	#subtraction
mul=num_1*num_2
print("mul of num_1*num_2 is : ",mul)	#multiplication
div=num_1/num_2
print("div of num_1/num_2 is : ",div)	#division
mod=num_1%num_2
print("mod of num_1%num_2 is : ",mod)	#modulus

#Comparison Operators
person_1=65		#greater than ('>')
person_2=55
com=person_1>person_2
print(com)

person_3=5.9		#less than ('<')
person_4=5.9
comp=person_3<person_4
print(comp)

re=person_1==person_2	#equal to ('==')
print(re)

re=person_1!=person_2	#equal to ('!=')
print(re)

#Logical Operators

#and logic operator
sd=[5.8,60]		#sd<siddharth>
ba=[6.0,75]		#ba<baladitya>
stmt_1=sd[0]<ba[0]
stmt_2=sd[1]<ba[1]
print(stmt_1)
print(stmt_2)
re=stmt_1 and stmt_2
print("your assemption is:",re)

#or logic operator
sd=[5.8,60]		#sd<siddharth>
ba=[6.0,75]		#ba<baladitya>
stmt_1=sd[0]<ba[0]
stmt_2=sd[1]<ba[1]
print(stmt_1)
print(stmt_2)
re=stmt_1 or stmt_2
print("your assemption is:",re)

#not logical operators
sd=[5.8,60]		#sd<siddharth>
ba=[6.0,75]		#ba<baladitya>
stmt_1=sd[0]<ba[0]
print(stmt_1)
re=not stmt_1
print("your assemption is:",re)

#Take two numbers as user input and

#Perform all arithmetic operations
num_1=10
num_2=2
print("num_1 : ",num_1)
print("num_2 : ",num_2)
sum=num_1+num_2
print("sum of num_1+num_2 is : ",sum)	#additiom
sub=num_1-num_2
print("sub of num_1-num_2 is : ",sub)	#subtraction
mul=num_1*num_2
print("mul of num_1*num_2 is : ",mul)	#multiplication
div=num_1/num_2
print("div of num_1/num_2 is : ",div)	#division
mod=num_1%num_2
print("mod of num_1%num_2 is : ",mod)	#modulus
flo=num_1//num_2
print("flo of num_1//num_2 is: ",flo)	#floating point

#Check which number is greater
num_1=20	#by comarision operators
num_2=30
resul=num_1 > num_2
print(resul)
print("if false num_2 is bigger than num_1")
print("if true num_1 is bigger than num_2")

#Display whether both numbers are positive using logical operators
no_1=20
no_2=1
st_1=no_1>0		#logic operation 
st_2=no_2>0
print(st_1)
print(st_2)
result=st_1 and st_2
print(result)
print("if true both are positive")
print("if false both are negative or any one number is negative")




