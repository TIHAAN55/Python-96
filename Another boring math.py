import random
import math
print(" FUN CALCULATOR ")

luck = random.randint(1, 10)
print("Your lucky number is: ", luck)

fun = ["play", "sleep", "read", "tv i guess"]
act = random.choices(fun)
print("Your activity: ", act)

print("\nGuess the old number from 1 to 5")
s = random.randint(1, 5)

while True:
    guess = int(input("Enter: "))
    
    if guess == s:
        print("Good boy!")
        break
    else:
        print("Not a good boy!")
        
dec = float(input("Enter a dec. num.: "))

print("Ceiling: ", math.ceil(dec))
print("Floor: ", math.floor(dec))

x = 10
y = -5
print("Copysign: ", math.copysign(x, y))

neg = int(input("Enter - num. : "))
print("Absolute cinema: ", math.fabs(neg))

n1 = int(input("Enter number: "))
n2 = int(input("Enter another: "))

print("GCD: ", math.gcd(n1, n2))

print("Summary: ")
print("Lucky num. : ", luck)
print("Lucky act. : ", act)
print("Secret: ", s)
print("         ")