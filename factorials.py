num = int(input("Enter a number: "))
result = 1
for i in range(num, 0 , -1):
    result = result * i
print(f"The factorial of {num} is {result}")