questions=["Capital of India? ","5+5 = ","Python is a (language / animal)?"]

answer = ["delhi","10","language"]



try:
    file = open("high_score.txt","r")
    high_score = int(file.read())
    file.close()
except:
    high_score = 0
    
score=0
name= input("enter the name")


for i in  range(len(questions)):
    ans = input(questions[i]).lower()
    if ans == answer[i]:
        score = score+ 1
print("\nYour scre:", score)
print("high score:", high_score)

if score> high_score:
    file = open("high_score.txt", "w")
    file.write(str(score))
    file.close()
    print("New High score")
else:
    print("try again")
