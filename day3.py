
# print(True+True+False)

nums=[0,1,0,3,12]
s = len(nums)
i=0
while i<s:
    if(nums[i]==0):
        nums[i], nums[s-1] = nums[s-1], nums[i]
        s-=1
    elif(nums[i]!=0):
        i+=1
        
print(nums)


text = "121"
left =0
right=len(text)-1
is_palindrome= True 
while left<right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left+=1
    right-=1

print(is_palindrome)

sentence = "Python make problem solve fun"
words= sentence.split()
longest =""
for i in words:
    if len(i)>len(longest):
        longest =i 
print(longest)