
num = int(input("Enter a number: "))
def calc_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
calc_factors(num)
