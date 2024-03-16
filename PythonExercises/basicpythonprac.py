#This is a python comment

#variables with the same indentifier gets
#overwritten by later declarations
a = 2
a = "Hello"
print("\n", a)

#Comparison of two numeric values return booleans

x = 3
y = 4
print("\n", x < y)
print("\n", x > y)
print("\n", x == y)

#For strings spanning multiple lines one can use ''' string here '''
multilinestring = '''this is
a multiline string'''

#Concatenation of strings
str1 = "Data "
str2 = "Science"
print("\n",str1 + str2)
#repetition of strings (ScienceScience .....)
print("\n",str2 * 10)
#in operator (does "ence" occur in str2?)
print("\nSubstring 'ence' occurs in str2?:", "ence" in str2)

#Conversion of other types/variables to strings using the function/object "str"

number_of_apples = 6
print("\nI have " + str(number_of_apples) + " apples")

firstname = "Emil"
lastname = " Bentin-Ørum"
age = 25
print("Name: " + firstname + lastname + "\nAge: " + str(age))

#You can index into strings like an array of chars (python is 0 indexed):
print(firstname[0])

#One can also index into the back of a string using -:
print(firstname[-1])
#lots of different methods for string objects
print(str.upper(firstname))

print("Jeg hedder Emil".split()) #returnerer en liste¨

#many formatting options. Can also use %A for placeholders
s = "name: {0}, Height: {1}".format("Barack Obama", 1.85)
print(s)

str3 = "Name: {0}\nAge: {1}".format(firstname + lastname, age)
print(str3)

print(("%s\n"*5) % tuple(range(5)))

#lists can contain different types:
list1 = [1, 2.0, "three", 4]
print(list1)
#you can change list after they are created:
list1[2] = "four"
print(list1) 
#lots of different methods for lists
list1.append(10)
print(list1)
list1.reverse()
print(list1)
list1.pop(4)
print(list1)
#accessing ranges of elements using slicing:
print(list1[1:3])
print(list1[:3])

list2 = ["One", "Two", "Three", "Four", "Five"]
print(list2[:3])
#two ways of printing last element of list2
print(list2[4:])
print(list2[-1:])
#printing last element but not in list anymore
print(list2[-1])

#Dictionaries/hashmaps
       #Key     #Value
days = {'Mon' : 'Monday', 'Tue' : 'Tuesday', 'Wed' : 'Wednesday'}

#Access elements by key:
print(days["Tue"])  #will print out Tuesday
#Add element to dics:
days['Thu'] = 'Thursday'
print(days)
#delete elements
del days['Mon']
print(days)
names = {'firstname' : 'Emil', 'lastname' : 'Bentin-Ørum', 'age' : 25}
names['address'] = 'Langesund'
print(names.keys())
names['name'] = names['firstname'] + ' ' + names['lastname']
del names["firstname"], names['lastname']
print(names)
print(names.keys())

#Files (remember to always save to a variable)
#input = open(filename, mode)
#readlines, writelines, close

list3 = [6, 9, 4, 8, 7, 1, 2]

def while_list_elements(lst):
    i = 0
    while (i < len(lst)):
        print(lst[i])
        i += 1

print(while_list_elements(list3))

def for_list_elements(lst):
    for i in range(len(lst)):
        print(lst[i])

print(for_list_elements(list3))

def isrightgreater(lst):
    for i in range(1, len(lst)):  # Start from the second element
        if lst[i] > lst[i - 1]:
            print(lst[i])

def isrightgreater1(lst):
    for i, entry in enumerate(lst):
        if i > 0 and entry > lst[i-1]:
            print(entry)

print(isrightgreater(list3))
print(isrightgreater1(list3))







