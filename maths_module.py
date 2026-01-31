import math
nums = 16
print(math.sqrt(nums))
print(math.pow(2,12))
num = 7.8
print(math.floor(num))
print(math.ceil(num))
print(math.fabs(5))

import random 
dice = random.randint(1,6)
print(dice)

student = ["Rahul","Karan","Vishal","NEha"]
selected = random.choice(student)
print("congratulation",selected)

#date time
import datetime
current = datetime.datetime.now()
print(current)
today = datetime.date.today()
print(today)
print(current.day)
print(current.month)
print(current.year)