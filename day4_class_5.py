# start
# load the old expenses from the from django.utils.translation import ugettext_lazy as _show menu
# 1. Add expense'
# 2. view expense
# 3. total expensr
# 4. exit
# user selects one option
# function runs
# save data
# repeat


expenses = []

try:
    file = open("expense.txt","r")
    for line in file:
        expenses.append(float(line))
    file.close()
except:
    pass

while True:
    print("\n ---Menu----")
    print("1. Add expense")
    print("2. View expense")
    print("3. Total expense")
    print("4. Exit")
    
    choice = input("choose options: ")
    
    if choice == "1":
        amount = float(input("Enter expense: "))
        expenses.append(amount)
        
        file = open("expense.txt","w")
        for e in expenses:
            file.write(str(e) + "\n")
        file.close()
        
        print("Expense added")
        
    elif choice == "2":
        print("Expenses:")
        for e in expenses:
            print(e)
    elif choice == "3":
        total = 0
        for e in expenses:
            total += e
        print("Total Expense:", total)
    elif choice == "4":
        print("exit")
        break
    
    else:
        print("Invalid choice")