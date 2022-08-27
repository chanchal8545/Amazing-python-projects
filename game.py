import random
list = ["s","w","g"]

total_choice=10
chance=0
my_score=0
computer_score=0

print("\nSnack,Water,Gun Game\n")
print("s for Snack\nw for Water\ng for Gun\n")

while chance<total_choice:
   print("Enter your choice:")
   me=str(input())
   
   r=random.choice(list)
   print("the computer choice is:\n ",r)
   total_choice=total_choice-1
# using snack
   if me=="s" and r=="s":
       print("your score is ",my_score,"computer score is ",computer_score)
       print("you remaining chances is",chance,"/10\n")
   elif me=="s" and r=="w":
       my_score=my_score+1
       print("your score is ",my_score,"and computer score is ",computer_score)
       print("you remaining chances is",chance,"/10\n")
   elif me=="s" and r=="g":
       computer_score=computer_score+1
       print("your score is ",my_score,"computer score is ",computer_score)
       print("you remaining chances is",chance,"/10\n")

# using water
   if me=="w" and r=="s":
       computer_score=computer_score+1
       print("your score is ",my_score,"computer score is ",computer_score)
       print("you remaining chances is",total_choice,"/10\n")
   elif me=="w" and r=="w":
       print("tie both side ")
       print("your score is ",my_score,"computer score is ",computer_score) 
       print("you remaining chances is",total_choice,"/10\n")
   elif me=="w" and r=="g":
       my_score=my_score+1
       print("your score is ",my_score,"and computer score is ",computer_score) 
       print("you remaining chances is",total_choice,"/10\n")

# using gun
   if me=="g" and r=="s":
       my_score=my_score+1
       print("your score is ",my_score,"and computer score is ",computer_score)
       print("you remaining chances is",total_choice,"/10\n")
   elif me=="g" and r=="w":
       computer_score=computer_score+1
       print("your score is ",my_score,"computer score is ",computer_score)
       print("you remaining chances is",total_choice,"/10\n")
   elif me=="g" and r=="g":
       print("tie both side ")
       print("your score is ",my_score,"computer score is ",computer_score)  
       print("you remaining chances is",total_choice,"/10\n")            
print("Game over")
if my_score>computer_score:  
    print("you are the winner and coputer is loose")
elif computer_score>my_score:
    print("coputer is winner and you are loose")   