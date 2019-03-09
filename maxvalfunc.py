def lar():
 	a=int(input("first no. is"))
 	b=int(input("second no. is"))
 	c=int(input("third no. is"))
 	if a==b and a==c:
 		print("all are same")
 	elif a>b and a>c:
 		print("a is greater ")
 		return a
 	elif b>c and b>a:
 		print("b is greater ")
 		return b
 	else:
 		print("c is greater ")
 		return c
lar()

