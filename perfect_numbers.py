# Creating a function, which check wether number is Perfect number or not?
''' The number, which is equal to divisor's sum equal to the given number: eg: 6 is perfect number:

6 => 1 + 2 + 3 = 6
28 => 1 + 2 + 4 + 7  + 14 = 28'''
def isPerfect():
    n = int(input("Enter any number: "))
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")

print(isPerfect())
