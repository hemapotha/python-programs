try:
	x=int(input("enter a number"))
	y=int(input("enter another number"))
	z=int(input("enter one more number"))
	
	if x*y*z==0:
		raise NameError
	elif xyz<=0:
		raise TypeError
except NameError:
	print("error value is x*y*z")
except TypeError:
	print("error value is less than 0")
else:
	print("no error")
finally:
	print("execution completed")