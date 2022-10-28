#List
demo_list = [10, 20, 15, 30, "hola"]
colors = ["red", "green", "yellow"]

new_list = list((1, 2, 3, 4, 5))#Create a list used the constructor
print(new_list)

r = list(range(1, 10))#Create a list with range
print(r)

#Methods of the lists
print(len(colors))
print(colors[0])
print("green" in colors)
colors.append("violet")
colors.extend(["orange", "blue"])
colors.extend(("pink", "black"))
colors.insert(1, "white")
colors.insert(len(colors), "cian")
print(colors)
colors.pop()
colors.remove("red")
colors.pop(3)
print(colors)
colors.sort()
print(colors)
colors.sort(reverse = True)
print(colors)
index = colors.index("white")
print(index)
print(colors.count("yellow"))
colors.clear()
print(colors)