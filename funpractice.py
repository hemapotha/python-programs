#function with no parameter

def func1():
	print("hello");
	print("hiii");

func1()

#function with paramater

def func2(a):
	print("hello","\t",a);

func2(3)

#function with more parameters

def func3(a,b,c):
	d=a+b+c
	print(a,b,c,d)

func3(1,2,3)

# function with random parameter

def func4(university="IITB"):
	print("im in"+"\t"+university)
func4("IITD")
func4("IITG")
#
func4()

def func5(a,b):
	print("hii other function")
	c=a+b
	return c

def func6():
	print("hello")
	s=func5(2,6)
	print("addition is",s)

func6()

