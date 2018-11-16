import time

def Euclid(m,n):
	while n != 0:
		r = m % n
		m = n
		n = r
	return m

def intCheck(m,n):
	t = min(m,n)
	while True:
		a = m % t
		if a == 0:
			b = n % t
			if b == 0:
				return t
		t=t-1

def primeFactors(n):
	i = 2
	factors = []
	while i*i <= n:
		if n % i != 0:
			i = i + 1
		else:
			n = n / i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors
	
def midSchool(m,n):
	GCDprod = 1
	GCDFactors = []
	x = primeFactors(m)
	y = primeFactors(n)
	for i in x:
		if i in y:
			GCDFactors.append(i)
			y.remove(i)	
	for x in GCDFactors:
		GCDprod *= x
	return int(GCDprod)

i = 0
isInteger = False
while i < 3 and isInteger == False:
	
	try:
		num1 = int(input("Input the first number "))
		num2 = int(input("Input the second number "))
		if num1 <= 0 or num2 <= 0:
			print("Input must be greater than 0!")
			i = i + 1
		else:
			isInteger = True
	except ValueError:
		print("Input must be an integer!")
		i = i + 1

if i == 3:
	print("Goodbye!")
	exit()
	
startEuclid = time.perf_counter()   
GCD = Euclid(num1,num2)
endEuclid = time.perf_counter()

startIntcheck = time.perf_counter() 
GCD2 = intCheck(num1,num2)
endIntcheck = time.perf_counter()  

startMidschool = time.perf_counter()  
GCD3 = midSchool(num1,num2)
endMidschool = time.perf_counter()  

print("Euclid's Algorithm:")
print("GCD is " + str(GCD))
print(str(endEuclid - startEuclid) + " seconds")
print("Integer Checking:")
print("GCD is " + str(GCD2))
print(str(endIntcheck - startIntcheck) + " seconds")
print("Middle School Method:")
print("GCD is " + str(GCD3))
print(str(endMidschool - startMidschool) + " seconds")