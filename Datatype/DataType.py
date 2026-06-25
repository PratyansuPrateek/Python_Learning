name = input("what is your name ").strip().title()
first, second = name.split(" ")
print("hello", first)
print("hello", second)
print("Hello,",name) 
print("Hello, " + name)
print(f"Hello, {name}")

print("Hello, \"prateek\"") # '\' is basically a escape character whcih is use to Don't treat the next character normally; do something special with it


"""
* This 'f' is stand for formating, in moden python we basically use to add  value directly in side the
string by using {} we can perform any data type inside this.  

* This ',' is separater which is used to add the 
string with other variable including one space in front. we can perform any datatype.

* this '+' is a concatination operator which is
  used to add two string to getter. Here we can only strings

* '.strip()' is a predefine method which is used to remove the white space 
   from first and last.

* '.title()' is a predefine method whcih is used to make the every word first
   letter Capital in a string.

* '.capitalize() is a predefine method whcih make the first letter of the string 
   capital.

* '.split()' is a predefine method which is used to split the string in to sub string
   


"""


