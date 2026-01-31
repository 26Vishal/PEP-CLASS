import re
text="cat cot cut"
result = re.findall("c.t",text)
print(result)

text="hello World"
print(bool(re.search("^Hello",text)))
print(bool(re.search("^Hello",text)))

#3. ending od string($)

text="hello World"
print(bool(re.search("Hello$",text)))
print(bool(re.search("Hello$",text)))

#4. 0 or more (*)
text="helloooo"
result= re.findall("lo",text)
print(result)

#5 one or more(+)
text = "hellooo"
result = re.findall("lo+",text)
print(result)

#8. Digits([0-9])
text = "My age is 30"
result = re.findall("[0-9]",text)
print(result)
#9. capital 
 \
     
#20. gropinng(())
text = "abab ab"
result = re.findall("(a+b)",text)
print(result)

#Write a syntax to validate a mobile no

import re
mobile = input("Enter mobile number:")
if re.match(r'^[6-9]\d{9}$',mobile):
    print("Vaild no")
else:
    print("Invalid mobile number")