#Conditionals
age = input("insert your age:")

if int(age) < 18 :
    print("you are underage")
else :
    print("you are of legal age")



name = "Jhon"
last_name = "Carter"

if  name == "Jhon":
    if last_name == "Carter":
        print(f"you are {name} {last_name}")
    else:
        print(f"you are not {name}")


x = 10
y= 20
if x == 10:
    print("your number is ten")
elif x < 10 :
    print("yout number is less than ten")
else:
    print("yout number is greather than ten")


if x > 2 and x <= 10:
    print("x is greather than two and less than ten or equal to ten")
if x > 2 or x <= 20:
    print("x is greather than two or less or equal to twenty")
if(not(x == y)):
    print("x is not equal y")