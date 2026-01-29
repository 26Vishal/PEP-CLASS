# # dict1 ={"a":2,"b":3}
# # dict2=dict1.copy()
# # print(dict2)

# # mobile ={"brand":"Samsung","model":524,"price":75000,"stock":20}

# # print(mobile)
# # print(mobile.keys())
# # print(mobile.get("model"))
# # print(mobile.values())


# contact={}
# while True:
#     print("\n---contact book----")
#     print("1. Add contact")
#     print("2. view contact")
    
#     print("3. search contact")
#     print("4. delete contact")
#     print("5. exit ")
    
#     choice = input("enter your choice")
    
#     if choice=="1":
#         name = input("Enter name")
#         Phone = int(input("enter number"))
#         contact[name]=phone
#         print("contact added succesfully")
    
#     elif choice =="2":
#         name = input("Enter the name you wan tot see")
#         if contact:
#             print("\n usaved contact")
#             for name,phone in contact.items():
#                 print(f"name: {name},phone: {phone}")
          
#         else:
#             print("contact not found")
        
#     elif choice =="3":
#         name = input("Enter name in search abr: ")
#         if name in contact:
#             print("Phone naumber :", contact[name])
#         else:
#             print("contact not found")
            
#     elif choice =="4":
#         name = input("enter the nmae you want to delete")
#         if name in contact:
#             del contact[name]
#             print("contact deleted")
#         else:
#             print("contact not found")
        
#     elif choice=="5":
#         print("thank you for using contact book")
#         break 
#     else:
#         print ("invalid choice!! pls try again")
        
        
        
name = "vishal"
print(name[1:2])
print(name)
print(name[0:6:2])
print(name[::-1])

s = "programming"
count =0
for i in s:
    if i in aeiou:
        count+=1
    
print(count)

sa= "programming"
a=0
b=length(sa)
for 


file = open("MOVIE.TXT ","r")
data=file.read()
print(data.replace(" "," "))
file.close()