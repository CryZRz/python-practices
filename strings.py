myStr = "hello world"

name = "cryz"

#methods for strings
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("hello","bye").upper())
print(myStr.count("l"))
print(myStr.startswith("hello"))
print(myStr.endswith("o"))
print(myStr.split(" "))
print(myStr.find("o"))
print(len(myStr))
print(myStr.index("w"))
print(myStr.isnumeric())
print(myStr.isalpha())
print(myStr[0])

#ways to concatenate strings
print("my name is " + name)
print(f"My name is {name}") #available as of python 3.6
print("my name {0}".format(name))