di={'r':"rock",'p':"paper",'s':"scissor"}
import random
l=["r","p","s"]

cscore=0
uscore=0


while True:
	

	u=input("enter your choice")
	print("you got",di[u])

	c=random.choice(l)
	print("computer got",di[c])

	if c==u:
		print("tie")
	if c=='r'and u=='s':
		print("comp wins")
		cscore=cscore+1
		uscore=uscore
	if c=='s'and  u=='r':
		print("user wins")
		uscore=uscore+1
	if u=='p'and c=='s':
		print("computer wins")
		cscore=cscore+1
	if u=='s'and c=='p':
		print("user wins")
		uscore=uscore+1
	if u=='p' and c=='r':
		print("computer wins")
		cscore=cscore+1
	if u=='r'and c=='p':
		print("computer wins")
		cscore=cscore+1

	print("score")
	print("computer",cscore,"user",uscore)

	if cscore==3:
		print("computer is the champion")
		exit()
	elif uscore==3:
		print("user is the champion")
		exit()



