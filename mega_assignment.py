
#Q26. What is a string? How can we declare string in Python?
#ANS: String is a collection of alphabets, words or other characters. 
#     It is one of the primitive data structures and are the building blocks for data manipulation.
#     Python has a built-in string class named str . Python strings are "immutable" which means they cannot be changed after they are created.Z
#    example - 
# Single quotes: 'Big Data'
# Double quotes: "Big Data"
# Triple quotes: ''' Big 
#                    Data'''


#Q27. How can we access the string using its index?
#ANS:  We can access string or its part by providing the index no. or range of index nos.
#      name = 'ashish kumar'
#      print(name[0:]) 
 

#Q28. Write a code to get the desired output of the following
#       string = "Big Data iNeuron"
#       desired_output = "iNeuron"
#ANS:   print(string[9:])


#Q29. Write a code to get the desired output of the following
#string = "Big Data iNeuron"
#desired_output = "norueNi"
#ANS: c = "Big Data iNeuron"
#    b=c[9:]
#    a=b[::-1]
#    print(a)
#       OR
# string = "Big Data iNeuron"
# desired_output = "norueNi"
# print(string[-1:-8:-1])

#Q30. Resverse the string given in the above question.
# rev= string[::-1]

#Q31. How can you delete entire string at once?
#ANS: By using del before the name of string varaiable.
#     ex- name="ashish kumar
#         del name

#Q32. What is escape sequence?
#ANS: An escape sequence is a sequence of characters that, when used inside a character or string,
#     does not represent itself but is converted into another character or series of characters

#Q33. How can you print the below string? h
#   'iNeuron's Big Data Course'
#ANS: a="iNeuron's Big Data Course" OR a= 'iNeuron\'s Big Data Course'
#     print(a)

#Q34. What is a list in Python?
#ANS:
# List in python is a sequential datatype. 
# It is used to store different types of data in a sequential manner.

#Q35. How can you create a list in Python?
#ANS: We can create a list by placing elements inside square brackets []. sepearted by commas.
#     sample_list = [1, 'Hi', True, 4.5]

#Q36. How can we access the elements in a list?
#ANS: by reffering their indexes.
#     sample_list = [1, 'Hi', True, 4.5]
#     smaple_list[0] -> 1

#Q37. Write a code to access the word "iNeuron" from the given list.
#     lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
#ANS: print(lst[4][2])

#Q38. Take a list as an input from the user and find the length of the list.
#ANS:
# lst = []
# x= int(input('pls no. of elements:' ))
# for i in range(0,x):
#     a=(input())
#     lst.append(a)
# print(len(lst))
# input_list = list(input('Enter , separated list items:').split(','))
# print(len(input_list))


#Q39. Add the word "Big" in the 3rd index of the given list.
#ANS:
# lst = ["Welcome", "to", "Data", "course"]
# lst[2]='Big'
# print(lst)

#Q40. What is a tuple? How is it different from list?
#ANS: Tuple is another type of sequential datatype. We can store different types of data inside it.
#     The difference between Tuple & List is, List is mutable & Tuple is immutable.

#Q41. How can you create a tuple in Python?
#ANS: # Using () brackets
#      tup1 = (1, 2, 'Big', 'Data', 2.0)

#Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
#ANS:  We cannot add data after creating the Tuple as tuples are immutable.
#     The only way to update the tuple is to overwrite the entire tuple with required changes.

#Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
#ANS: We can combine two tuples using + operator.
#     tup1 = (1,2,3,4)
#     tup2 = (5,6,7,8)
#     combined_tuple = tup1 + tup2

# Q44. Take a tuple as an input and print the count of elements in it.
#ANS:
# tup1 = eval(input('Enter the tuple elements:'))
# print('Length of the tuple is:', len(tup1))

# Q45. What are sets in Python?
#ANS: Set is a data type in pyton which is collection of unique elements. It is not indexed.

# Q46. How can you create a set?
#ANS:
# Method 1
# s1 = {1, 2, 3}
# # OR 
# Method 2
# # s2 = set([1,2,3])

# Q47. Create a set and add "iNeuron" in your set.
#ANS:
# s1 = {'Big', 'Data', 'Engineer'}
# s1.add('iNeuron')

# Q48. Try to add multiple values using add() function.
#ANS: We cannot add multiple values using add() function.

# Q49. How is update() different from add()?
#ANS: update() function can add multiple elements in a set if iterable items like list, tuple, string or another set is providied to it as an argument.

# Q50. What is clear() in sets?
#ANS: clear() function is used to delete all elements in set & make it empty.

# Q51. What is frozen set?
#ANS: Frozen set is datatype in Pyton. It is similar to set except it is immutable.

# Q52. How is frozen set different from set?
#ANS: Set is mutable while frozen set is immutable.

# Q53. What is union() in sets? Explain via code.
#ANS: union() in set is used to combine the elements of two different sets.
# s1 = {'Big', 'Data', 'Engineer'}
# s2 = {1, 2, 3}
# print(s1.union(s2))
# # Output -> {1, 2, 3, 'Data', 'Engineer', 'Big'}

# Q54. What is intersection() in sets? Explain via code.
#ANS: intersection() in sets is used to get only those elements which are present in both the sets.
# s1 = {'Data', 'Engineer', 'Software', 'Developer'}
# s2 = {'Software', 'Engineer', 'Data', 'Science'}
# print(s1.intersection(s2))
# # Output -> {'Data', 'Software', 'Engineer'}

# Q55. What is dictionary in Python?
#ANS: dictionary data type in Python is used to store data in the form of key-value pairs.

# Q56. How is dictionary different from all other data structures.
#ANS: dictionary stores data in key-value pair. While most of the sequential data types use indexes to access data dictionary uses keys.

# Q57. How can we declare a dictionary in Python?
#ANS: Empty dictionary
# dict1 = dict()
# dict2 = {}

# Dictionary with elements
# dict3 = {'name':'Vivek', 'age':23, 'city':'Pune'}
# Q58. What will the output of the following?

# var = {}
# print(type(var))
# <class 'dict'>

# Q59. How can we add an element in a dictionary?
#ANS: dict1 = dict()

# # Method 1
# dict1.update({'name':'Vivek'})

# # Method 2
# dict1['age'] = 23

# print(dict1)
# # Output -> {'name': 'Vivek', 'age': 23}

# Q60. Create a dictionary and access all the values in that dictionary.
#ANS: dict1 = {'name':'Vivek', 'age':23, 'city':'Pune'}
# print(dict1.values())
# Output -> dict_values(['Vivek', 23, 'Pune'])

# Q61. Create a nested dictionary and access all the element in the inner dictionary.
#ANS: dict1 = {'name':'Vivek', 'age':23, 'city':'Pune', 'skills': {'language':'Python', 'database':'MySQL'}}
# print(dict1.get('skills'))
# # Output -> {'language':'Python', 'database':'MySQL'}

# Q62. What is the use of get() function?
#ANS: get() function is used to get value corresponding to the key given as an argument.

# Q63. What is the use of items() function?
#ANS: items() function is used to get a list of key-value tuples of a dictionary

# Q64. What is the use of pop() function?
#ANS: pop() function is used to get value corresponding to the key given as an argument. It also deletes that key-value pair from dictionary.

# Q65. What is the use of popitems() function?
#ANS: It removes the last item inserted from a dictionary.

# Q66. What is the use of keys() function?
#ANS: keys() function is used to get all the keys from a dictionary.

# Q67. What is the use of values() function?
#ANS: values() function is used to get all the values from a dictionary.

# Q68. What are loops in Python?
#ANS: Loops in Python are used to execute a block of code repeatedly until the condition is True.

# Q69. How many type of loop are there in Python?
#ANS: In Python there are two types of loops

# for loop
# while loop

# Q70. What is the difference between for and while loops?
#ANS: Mostly we use 'for loop' for a particular range and we use 'while loop' until a particular condition is True.

# Q71. What is the use of continue statement?
#ANS: continue statement is used to skip the current execution of the loop & move to the next iteration.

# Q72. What is the use of break statement?
#ANS: break statement is used to exit from the loop.

# Q73. What is the use of pass statement?
#ANS: pass statement is used to temporarily execute the program without the block of code which we have planned to develop in future.

# Q74. What is the use of range() function?
#ANS: range() function generates range of numbers which have been passed to it as an argument.

# Q75. How can you loop over a dictionary?
#ANS: We can use items() function to loop through a dictionary.
# dict1 = {'name':'Vivek', 'age':23, 'city':'Pune', 'skills': {'language':'Python', 'database':'MySQL'}}
# for k,v in dict1.items():
#     print('Key:', k, 'Value:', v)


#Coding problems
#Q76. Write a Python program to find the factorial of a given number.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for num in range(1, n+1):
#         result = result * num
#     return result
# x = 5
# ans = factorial(x)
# print("Factorial of number ",x, " = ", ans)

#Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100
#ANS:
#   def sicalculator():
#     p=int(input('enter the pricipal amount :'  ))
#     t=int(input('enter the time in years :'  ))
#     r=int(input('enter the rate of interset :'  ))
#     si=(p*t*r)/100
#     print("Your simple interset would be",si)
# Simple_interset= sicalculator()

#Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.
#ANS:
# def cicalculator():
#     principal=int(input('enter the pricipal amount :'  ))
#     time=int(input('enter the time in years :'  ))
#     rate=int(input('enter the rate of interset :'  ))
#     a=principal*(1+rate/100)**time
#     ci=round(a-principal)
#     print("Your compounded interset would be",ci)
# compound_interset= cicalculator()

#Q79. Write a Python program to check if a number is prime or not.
# def check():
#     n= int(input('enter a no : ' ))
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print('number is not a prime')
#                 break
#         else:
#                 print('number is prime')
#     else:
#          print("no. is not prime")      
# find=check()              

#Q80. Write a Python program to check Armstrong Number.\
# num = input('Enter a number: ')
# result = 0

# for n in num:
#  result += int(n) ** 3

# if int(num) == result:
#  print(num, 'is a Armstrong number')
# else:
#  print(num, 'is not a Armstrong number')

#Q81. Write a Python program to find the n-th Fibonacci Number.
# def fib():
#     n=int(input('enter any no'))
#     n1=0
#     n2=1
#     if n<=0:
#         print('wrong input')
#     elif n==1:    
#        return 1
#     else:
#       for i in range(1,n):
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         print(n2)
# fib()

#Q82. Write a Python program to interchange the first and last element in a list.
# lst=['ash','bsh','csh','dsh','she','shf','gsh']
# lst[0], lst[-1] = lst[-1], lst[0]
# print(lst)

#Q83. Write a Python program to swap two elements in a list.
# lst=['ash','bsh','csh','dsh','she','shf','gsh']
# lst[0], lst[-1] = lst[-1], lst[0]
# print(lst)

#Q84. Write a Python program to find N largest element from a list.
# lst=[12,34,53,64,13,100]
# print(max(lst))

#Q85. Write a Python program to find cumulative sum of a list.
# lst=[12,34,53,64,13,100]
# print(sum(lst))

#Q86. Write a Python program to check if a string is palindrome or not.
# def palincheck(x):
#     y=x[::-1]
#     if x==y:
#         print('Yes, the string is palindrome')
#     else:
#         print('No, string is not palindrome')

# check=input("pls enter any string : " )
# palincheck(check)

#Q87. Write a Python program to remove i'th element from a string.
# line=' i am ashish and i am from india'
# print(line.replace('a', '',1))

#Q88. Write a Python program to check if a substring is present in a given string.
#ANS:
# def checksub(a):
#     txt = "My name is khan and i am not a terrorist"
#     x = txt.rfind(a)
#     if x<0:
#        print('substring is not found')
#     else:
#        print('substring is found at index :',x)
    
# sub_str=input('enter the value of substring: ' )
# checksub(sub_str)

#Q89. Write a Python program to find words which are greater than given length k.
# s = input('Enter a string: ')
# k = int(input('Enter desired length: '))

# lst = s.split()
# for word in lst:
#     if len(word) > k:
#  print(word)

# #Q90. Write a Python program to extract unquie dictionary values.
# test_dict = {'my': [1, 8, 9, 6], 'big': [10, 11, 9, 1], 'data': [6, 12, 10, 6], 'dict': [5, 2, 1]}
# result = []
# for v in test_dict.values():
#     result += v
# print(list(set(result)))


#Q91. Write a Python program to merge two dictionary.
#ANS:
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# c=dict1.update(dict2) 
# print(dict1)

#Q92. Write a Python program to convert a list of tuples into dictionary.
#ANS:
#Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
#Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
# lst=[('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# abc=dict(lst)
# print(abc)

#Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
#Input: list = [9, 5, 6]
#Output: [(9, 729), (5, 125), (6, 216)]
#ANS:
# lst=[9,5,6]
# lst1 = [(val, pow(val, 3)) for val in lst] 
# print(lst1)

#Q94. Write a Python program to get all combinations of 2 tuples.
#Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
#Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
#ANS:
# import itertools
# test_tuple1 = (7, 2)
# test_tuple2 = (7, 8)
# c = list(itertools.product(test_tuple1, test_tuple2))
# d = list(itertools.product(test_tuple2, test_tuple1))
# e= c+d
# print(e)

#Q95. Write a Python program to sort a list of tuples by second item.
#Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
#Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
#ANS: don't know 

#Q96. Write a python program to print below pattern.
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
# n=5
# for i in range(0, n):
#         for j in range(0, i+1):
#             print("* ",end="")
#         print("\r")

#Q97. Write a python program to print below pattern.
#    *
#   **
#  ***
# ****
#*****
#ANS:
# print("Welcome to", end = ' ')
# print("GeeksforGeeks")
# n=5
# for i in range(n, 0):
#         for j in range(i+1,0):
#             print(" ",end="")
#         print("\r")

#Q98. Write a python program to print below pattern.
#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * * 
# n=5
# for i in range(1, n+1):
#     print(' ' * (n-i), '*' * i)


#Q99. Write a python program to print below pattern.
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5

# n = 5
# for i in range(1, n+1):
#  for j in range(1, i+1):
#   print(j, end=' ')
#  print()


#Q100. Write a python program to print below pattern.
#A 
#B B 
#C C C 
#D D D D 
#E E E E E 

# import string
# alpha = list(string.ascii_uppercase)
# n = 5
# for i in range(1, n+1):
#  print((alpha[i-1] + ' ') * i)
