#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
out_put = number % 10 if number > 10 else number % -10
if out_put > 5:
    print(f"Last digit of {number} is {out_put} and is greater than 5")
elif out_put == 0:
    print(f"Last digit of {number} is {out_put} and is 0")
else:
    print(f"Last digit of {number} is {out_put} and is less than 6 and not 0")
