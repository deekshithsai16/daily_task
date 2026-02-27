#Arithmetic Operations
#Calculate:
#Total
num_1=100
num_2=2
num_3=2
print("num_1 : ",num_1)
print("num_2 : ",num_2)
print("num_3 : ",num_3)
total=num_1+num_2		#total
print("total is : ",total)
total=num_1+num_2+num_3		#average
avg=total/3
print(avg)
rem=num_1%num_3			#remainder
print("rem is : ",rem)
squ=num_2**num_3		#square of a number
print("mod is : ",squ)


#Assignment Operators
numb_1=20
print("value of numb_1 is : ",numb_1)	
numb_1 +=10
print("value of numb_1 is : ",numb_1)	#+=
numb_1 -=10
print("value of numb_1 is : ",numb_1)	#-=
numb_1 *=10
print("value of numb_1 is : ",numb_1)	#*=
numb_1 //=10
print("value of numb_1 is : ",numb_1)	#//=


#Comparison Operators
person_1=65
person_2=55
person_3=5.9
person_4=5.9
com=person_1>person_2
print(com)		#Greater than
comp=person_3<person_1
print(comp)		#Less than
re=person_3==person_4
print(re)		#Equal to
res=person_1!=person_2
print(res)		#Not equal to
resu=person_3>=person_4
print(resu)		#Greater than or equal to
result=person_3<=person_1
print(result)		#Less than or equal to


#Logical Operators
sd=[5.8,60]		#sd<siddharth>
ba=[6.0,75]		#ba<baladitya>
stmt_1=sd[0]>ba[0]
stmt_2=sd[1]>ba[1]
print(stmt_1)
print(stmt_2)
assump_1=stmt_1 and stmt_2
print("your assemption is:",assump_1)	#and 
assump_2=stmt_1 or stmt_2
print("your assemption is:",assump_2)	#or
assump_3=not stmt_1
print("your assemption is:",assump_3)	#not


#Bitwise Operators
bin=5
bin_1=3
print(bin & bin_1)	#&
print(bin | bin_1)	#|
print(bin ^ bin_1)	#^
print(bin << bin_1)	#<<
print(bin >> bin_1)	#>>

#Membership Operators
list_1=[10,20,30,40,50]
print(list_1)		
ele=20 in list_1
print(ele)		#in
ele_1=1 not in list_1
print(ele_1)		#not in


#Identity Operators
number=10
number_1=10
print(number is number_1)
print(number is not number_1)






