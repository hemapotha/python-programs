try:
	x=int(input("enter a number"))
	if x==4:
		raise NameError
	elif x>=4:
		raise TypeError
except NameError:
	print("error value is 4")
except TypeError:
	print("error value  greater is than 4")
else:
	print("no error",x)
finally:
	print("execution completed")

