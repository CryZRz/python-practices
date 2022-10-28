#data types

#String #text
"hello world"
print(type("hello world"))

print("bye" + "world") #concat Strings

#Number 
200
print(type(100))

print(200 + 200)#sum numbers

#Float
30.5
print(type(30.5))

#Boleans
True
False
print(type(True))
print(type(False))

#Arrays or List
[10, 20, 30, 50]
["fernanda", "jimena", "chris", "alan"]
["fernanda", "jimena", 200, True, 36.5]
print(type([10, 20, 30, 50]))


#Tuples for dates not change
(10, 30, 30, 55) #immutable
print(type((10, 30, 30, 55)))


#Dictorionies
{
    "name": "Christian",
    "lastname": "Ramos",
    "username" : "Cryz"
}
print(
    type(
        {
            "name": "Christian",
            "lastname": "Ramos",
            "username" : "Cryz"
        }
    )
)

#Nontype
print(type(None))