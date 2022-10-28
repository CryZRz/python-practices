operation = input("Select a operation: 1:Sum 2:Res 3:Multiplitcation 4:Division")

if int(operation) == 1:
    numbers_to_operation = input("how many numbers do you want to add")
    count = 0
    arr_numbers = []
    while count < int(numbers_to_operation):
        num = input("Insert number")
        arr_numbers.append(int(num))
        count = count+1
    result = 0    
    for num in arr_numbers:
        result = result + num
    print(f"Result: {result}")

elif int(operation) == 2:
    numbers_to_operation = input("how many numbers do you want to subtract")
    count = 0
    arr_numbers = []
    while count < int(numbers_to_operation):
        num = input("Insert number")
        arr_numbers.append(int(num))
        count = count+1
    result = arr_numbers[0]
    arr_numbers.pop(0)    
    for num in arr_numbers:
        result = result - num
    print(f"Result: {result}")

elif int(operation) == 3:
    numbers_to_operation = input("how many numbers do you want to multiply")
    count = 0
    arr_numbers = []
    while count < int(numbers_to_operation):
        num = input("Insert number")
        arr_numbers.append(int(num))
        count = count+1
    result = 1   
    for num in arr_numbers:
        result = num * result
    print(f"Result: {result}")

elif int(operation) == 4:
    numbers_to_operation = input("how many numbers do you want to subtract")
    count = 0
    arr_numbers = []
    while count < int(numbers_to_operation):
        num = input("Insert number")
        arr_numbers.append(int(num))
        count = count+1
    result = arr_numbers[0]
    arr_numbers.pop(0)    
    for num in arr_numbers:
        result = result / num
    print(f"Result: {result}")
else:
    print("this operation not exist")