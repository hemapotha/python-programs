import random

d=0
p=0
while True:
  r=input("press r to roll,q to quit : ")
  if r =='r':
    d = random.randint(1,6)
    
    if d == 6:
      print("Congratulations,you can play now.")
      print("you got d:",6)
      break
    else:
      print("roll again till you get 6.")
while True:
  r = input("press r to roll,q to quit :")
  if r == 'r':
    d = random.randint(1,6)
    print("you got :",d)
    p = p+d
    if p > 100:
      p = p-d
      print("wait till you get",100-p,"or less")
      print("your new position is : ",p)

    if p == 100:
      print("you won!")
    if p == 8:
      p = 37
      print("you got a ladder.go to ",p)
    if p == 11:
      p = 2
      print("you got a snake,go to ",p)
  elif r == 'q':
    print("bye!")
    exit()