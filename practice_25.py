# 1.      Write a program to demonstrate basic data type in python. (Numbers, Strings, Lists, Tuples, Dictionary, Set, Frozenset, Bool, Mutable and Immutable.)

# pblm 1
# a = 5
# print("Type of a: ", type(a))
# b = 5.0
# print("\nType of b: ", type(b))
# c = 2 + 4j
# print("\nType of c: ", type(c))

# print(5==5)
# print(5>6)

# pblm 2

# num=int(input("Enter your number : "))
# while(num>=0):
#     print(num)
#     num=num-1

# pblm 3
# user =  input("Enter your name : ")
# num = int(input("Enter the number of your name should be prined : "))
# while num > 0:
#     print(user)
#     num= num-1

# pblm 4
# dic = {
#     "book" : "literature",
#     "book1": "comic",
#     "book2": "funny"
# }
# print(dic)

# pblm 5
# list = ['Khushal','Varad','Ramesh',7,'Parth']
# list.pop()
# print(list)
# list.remove('Varad')
# print(list)
# list.append(5)
# print(list)
# list.extend('K')
# print(list)

# pblm 6
# import math
# c = float(input("Enter the Angle : "))

# print(math.sin(c))
# print(math.cos(c))
# print(math.tan(c))

# pblm 7
# str = input("Enter the String : ")

# print(len(str))
# i = 1
# while i <= 10:
#     print(str)
#     i = i+1
# print(str[0])
# print(str[1])
# print(str[2])
# print(str[-1],str[-2],str[-3])

# print(str[::-1])
# if len(str) >= 7:
#     print(str[7])
# else:
#     print("Not Enough Lenght of String")
        
# pblm 8
# string = input("Enter any Strings: ")
# sentence = string.lower()
# vowels = 0
# consonants = 0 
# list = ["a","e","i","o","u"]  
# for letters in sentence:
#     if letters in list:
#         vowels +=1
#     else:
#         consonants +=1

# print("Number of vowels in strings:", vowels)
# print("NUmber of consonants in strins:", consonants)    

# pblm 9
# list = [1,2,3,4,5,6,9,5]
# print(len(list))
# print(list[6])
# print(list[::-1])
# if list.count(5) >= 0:  
#     print("Yes")
# else:
#     print("No")  

# print(list.count(5))  
# list.pop()   
# print(list)
# list.remove(1)
# print(list)
# list.sort()
# print(list)

#pblm 10
# F:\VIIT LEARNING & COLLEGE WORK\SECOND YEAR\SEMESTER 4\IT WORKSHOP(PYTHON)\Assignments\Assignment No. 1  --> These is the path for Text.txt
# fname = input("Enter the File Name : ")
# try:
#     fhand = open(fname)
# except :
#     print("File cannot be opened : ", fname)
#     exit()
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else: 
#             counts[word] += 1
# print(counts)


#practice Problems
# str = input("Enter the String : ")
# f = {}
# for i in str:
#     if i in f:
#         f[i] += 1
#     else:
#         f[i] = 1
# print(f)       

# greetings = "Hello World"
# new_greeting = 'J' + greetings[3:7]
# print(new_greeting)

# dict{
#     'one':'fy',
#     'two':'sy',
#     'three':'ty',
#     'four':'BTech'
# }
# print(dict)


