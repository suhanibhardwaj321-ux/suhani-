print("welcone to this quiz")
play=input("do you want to play this game...")
text="tim is great!"
print(text.lower())
if play.lower()!="yes":
    quit()
print("okey! let's play:")
score=0

ans=input("what does cpu stands for?")
if ans.lower()=="central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

ans=input("what does ROM stands for?")
if ans.lower()=="read only memory":
    print("correct")
    score +=1
else:
    print("incorrect")

ans=input("what does RAM stands for?")
if ans.lower()=="random access memory":
    print("correct")
    score +=1
else:
    print("incorrect")

ans=input("what does GUI stands for?")
if ans.lower()=="graphical user interface":
    print("correct")
    score +=1
else:
    print("incorrect")

ans=input("what does GPU stands for?")
if ans.lower()=="graphics processing unit":
    print("correct!")
    score +=1
else:
    print("incorrect!")

ans=input("what does PSU stands for?")
if ans.lower()=="POWER SUPPLY":
    print("correct!")
    score +=1
else:
    print("incorrect!")

ans=input("BRAIN  of computer")
if ans.lower()=="cpu":
    print("correct!")
    score +=1
else:
    print("incorrect!")
print("you got"+str(score)+"question correct")  
    
    

