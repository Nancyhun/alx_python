#!/usr/bin/python3
import random

# num = [random.randint(-10,10) for i in range(10)]

# for x in num:
#     if x > 0:
#         print(x,"is positive")
#     elif x < 0:
#         print(x,'is negative')
#     else:
#         print(x,'is zero')


number = random.randint(-10, 10)
if number > 0:
    print(number,"is positive")

elif number == 0:   
    print(number,"is zero")

else: 
    print(number, "is negative")
  
