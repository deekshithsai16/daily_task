#Extract the first half of the string.
py_prog_lang="PythonProgrammingLanguage"
print(py_prog_lang[0:12:1])	#Extract the first half of the string.
print(py_prog_lang[-1:-14:-1])	#Extract the second half using negative slicing only.
print(py_prog_lang[10:15:1])	#Extract the middle 5 characters dynamically.
py=py_prog_lang[0:6:1]
prog=py_prog_lang[-9:-20:-1]
lang=py_prog_lang[17:26:1]
print(py+prog+lang)		#Reverse only the middle portion of the string.


#Create a new string that contains:Characters at prime index positions only.
s="PythonProgrammingLanguage"	#2,3,5,7,9,11,13,15,17,19
print(s[1:3:1]+s[4::2])		#prime positions only
neg_even_ind=print(s[-2::-2])	#Characters at negative even index positions only.

vowel_count=(s[::1].count('a')+s[::1].count('e')+s[::1].count('i')+s[::1].count('o')+s[::1].count('u'))
print(vowel_count)		#vowels count

#part2
#Create a list of numbers from 1 to 20 dynamically.
numb=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#Extract elements divisible by 3 using step slicing logic.
print(numb[2::3])

#Reverse every block of 5 elements.
print(numb[0:5][::-1]+numb[5:10][::-1]+numb[10:15][::-1]+numb[15:20][::-1])
print(numb[10:]+numb[:10])		#Swap first half and second half of the list.
list_mi=[1,2,3]				
mirror_list=list_mi+list_mi[::-1]	
print(mirror_list)			#Create a mirrored list:
print(numb[1:-1])			#Remove the first and last element using slicing


#part4
#Create a tuple:
#Extract alternate elements from the end using negative step slicing.
t=(10,20,30,40,50,60,70,80)	
print(t[::-2])

#Rotate the tuple 3 positions to the right using slicing only.
print(t[-5:]+t[:-5])

#Rotate 2 positions to the left.
print(t[-2:]+t[:-2])

#Check if tuple remains same after double reverse operation (prove using slicing).
doub_rev=(t[::-1][::-1])
print(doub_rev)
same_tuple=(t==doub_rev)
print(same_tuple)

#task4
data="Datascience"
print(data[-1::-1])	#Generate output: