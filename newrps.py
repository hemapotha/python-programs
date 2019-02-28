import random
l=["r","p","s"]

#take input from user
u=input("enter your choice")

#input from computer
c=random.choice(l)
print("computer got",c)

#compare user and computer choice
if c==u:
	print("tie")
if c=='r'and u=='s':
	print("comp wins")
if c=='s'and  u=='r':
	print("user wins")
if u=='p'and c=='s':
	print("computer wins")
if u=='s'and c=='p':
	print("you won")
if u=='p' and c=='r':
	print("uesr wins")
if u=='r'and c=='p':
	print("computer wins")

