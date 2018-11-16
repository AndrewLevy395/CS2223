import math
import time
import ast

with open('input.txt', 'r') as f:
    setZ = ast.literal_eval(f.read())
    
def ptDist(pt1,pt2):
	ins = ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)
	answer = (math.sqrt(ins))
	return answer


def bruteForce(A):
	length = len(A)
	minDist = ptDist(A[0],A[1])
	for i in range(length-1):
		for j in range(i+1,length):
			if ptDist(A[i],A[j]) < minDist:
				minDist = ptDist(A[i],A[j])
	return minDist

def EfficientClosestPair(P,Q):
	n = len(P)
	if n <= 3:
		return bruteForce(P)
	else:
		Pl = P[0:n//2+1]
		Pr = P[n//2:n]
		Ql = sorted(Pl, key = lambda x: x[1])
		Qr = sorted(Pr, key = lambda x: x[1])
		dl = EfficientClosestPair(Pl,Ql)
		dr = EfficientClosestPair(Pr,Qr)
		d = min(dl,dr)
		m = P[(n//2)-1][0]
		S = [x for x in Q if abs(x[0]-m) < d]
		dminsq = d*d
		num = len(S)
		for i in range(0,num-1):
			k = i+1
			while (k < num) and ((S[k][1]-S[i][1])**2 < dminsq):
				dminsq = min(((S[k][0]-S[i][0])**2)+((S[k][1]-S[i][1])**2),dminsq)
				k = k+1
	return math.sqrt(dminsq)
		
startBrute = time.perf_counter()   
bruFor = bruteForce(setZ)
endBrute = time.perf_counter()

startConq = time.perf_counter()
divConq = EfficientClosestPair(sorted(setZ, key=lambda x: x[0]), sorted(setZ, key=lambda y: y[1]))
endConq = time.perf_counter()

print("Divide and Conquer Distance:")
print(divConq)
print("Brute Force Distance:")
print(bruFor)
print("Divide and Conquer Time:")
print(endConq-startConq)
print("Brute Force Time:")
print(endBrute-startBrute)