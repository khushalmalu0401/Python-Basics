# 1.      Write a program to demonstrate basic data type in python. (Numbers, Strings, Lists, Tuples, Dictionary, Set, Frozenset, Bool, Mutable and Immutable.)

# 1)     Execute following instructions.

# a = 5
# print("Type of a: ", type(a))
# b = 5.0
# print("\nType of b: ", type(b))
# c = 2 + 4j
# print("\nType of c: ", type(c))

# print(5==5)
# print(5>6)

# 2)     Write a program using a while loop that asks the user for a number, and prints a countdown from that number to zero.

# 3)     Write a program that asks the user for their name and how many times to print it. The program should print out the user’s name the specified number of times.

# 4)     create a dictionary var for a book information and display.

# 5)     Perform various operations on a list. (eg- sort, pop, remove, append, extend, del etc.)

# 6)     Write a program that asks the user for a number and then prints out the sine, cosine, and

# tangent of that number.

# 7)     Write a program that asks the user to enter a string. The program should then print the following:

# (a) The total number of characters in the string

# (b) The string repeated 10 times

# (c) The first character of the string (remember that string indices start at 0)

# (d) The first three characters of the string

# (e) The last three characters of the string

# (f) The string backwards

# (g) The seventh character of the string if the string is long enough and a message otherwise

# (h) The string with its first and last characters removed

# (i) The string in all caps

# (j) The string with every a replaced with an e

# (k) The string with every letter replaced by a space

# 8) Write a program that asks the user to enter a word and prints out whether that word contains any vowels

# 9) Write a program that asks the user to enter a list of integers. Do the following:

# (a) Print the total number of items in the list.

# (b) Print the last item in the list.

# (c) Print the list in reverse order.

# (d) Print Yes if the list contains a 5 and No otherwise.

# (e) Print the number of fives in the list.

# (f) Remove the first and last items from the list, sort the remaining items, and print the

# result.

# (g) Print how many integers in the list are less than 5.

# 10 )  Create dictionary for words and counts in file.  

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


