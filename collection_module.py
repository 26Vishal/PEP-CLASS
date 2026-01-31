from collections import Counter
fruits = ["banana","apple","mango","Apple","Mango","BAnana"]
count = Counter(fruits)
print(count)

text ="hello"
count2 = Counter(text)
print(count2)
sentence = "Python is eay  and python is powerrfull"
count1 = Counter(sentence)
print(count1)
number = [1,2,2,3,1,3,4,1,3]
count3 = Counter(reversed(number))
print(count3)



#--------------------------------------------OS-------------------------------------------------#
import os 
current_path = os.getcwd()
print(current_path)
item = os.listdir()
print(item)


import os
folder_name = "MyFolder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("folder created successfully")
    
else:
    print("Folder is already present there")

