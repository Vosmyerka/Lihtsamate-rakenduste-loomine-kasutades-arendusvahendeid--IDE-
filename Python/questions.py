score = 0
print ("Welcome to Math Quiz")
question1 = str(input("Are you ready to play? (Yes/No) "))
if question1 == "Yes":
    print("Then we'll start")
else:
    print("Ok, bye!")
    exit

question2 = str(input("2+2= " ))
if question2 == "4":
    print("Right!")
else:
    ("Wrong answer")