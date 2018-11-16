import math
from itertools import combinations
import time
import random


with open("input.txt", "r") as f:
	W = int(f.readline())
	weights = f.readline().split(',')
	weights = [int(i) for i in weights]
	values = f.readline().split(',')
	values = [int(i) for i in values]
	f.close()

objects = list(zip(weights, values))

def exhaustiveSearch(c, o):
	currentWeight = 0
	currentCost = 0
	currentMax = 0
	bag = []
	x = len(o)
	for i in range(x):
		for j in combinations(o, i+1):
			currentWeight = sum([y[0] for y in j])
			currentCost = sum([y[1] for y in j])
			if (currentWeight <= c) and (currentCost > currentMax):
				currentMax = currentCost
				bag.clear()
				bag.append(j)
	return currentMax, list(bag[0])
		
def dynamicProgramming(c, o):
	x = len(o)
	wgts = list([x[0] for x in o])
	vals = list([x[1] for x in o])
	K = [[0 for a in range(c+1)] for a in range(x+1)]
	bag = [[ [] for a in range(c+1)] for a in range(x+1)]
	for i in range(x+1):
		for j in range(c+1):
			if i==0 or j==0:
				K[i][j] = 0
				bag[i][j] = []
			elif wgts[i-1] <= j:
				if vals[i-1] + K[i-1][j-wgts[i-1]] > K[i-1][j]:
					K[i][j] = vals[i-1] + K[i-1][j-wgts[i-1]]
					bag[i][j] = bag[i-1][j-wgts[i-1]]+[(o[i-1])]
				else:
					K[i][j] = K[i-1][j]
					bag[i][j] = bag[i-1][j]
			else:
				K[i][j] = K[i-1][j]
				bag[i][j] = bag[i-1][j]
	return K[x][c], bag[x][c]

def greedyMethod(c, o):
	x = len(o)
	currentWeight = 0
	pastWeight = 0
	inBag = []
	wgts = list([x[0] for x in o])
	vals = list([x[1] for x in o])
	ratioList = sorted([[v / w, w, v] for v,w in zip(vals,wgts)], reverse=True)
	for i in ratioList:
		if currentWeight + i[1] <= c:
			inBag.append(i)
			pastWeight = currentWeight
			currentWeight = currentWeight + i[1]
		currentMax = sum([x[2] for x in inBag])
	bagW = list([y[1] for y in inBag])
	bagV = list([y[2] for y in inBag])
	bag = list(zip(bagW, bagV))
	return currentMax, bag

def runAll():
	startBF = time.perf_counter()
	bruteForce = exhaustiveSearch(W, objects)
	endBF = time.perf_counter()

	startDP = time.perf_counter()
	dynProg = dynamicProgramming(W, objects)
	endDP = time.perf_counter()

	startGM = time.perf_counter()
	greMethod = greedyMethod(W, objects)
	endGM = time.perf_counter()

	print("Maximum value for Exhaustive Search:")
	print(bruteForce[0])
	print("Objects in bag for Exhaustive Search:")
	print(bruteForce[1])
	print("Time for Exhaustive Search:")
	print(endBF - startBF)
	print(" ")
	print("Maximum value for Dynamic Programming:")
	print(dynProg[0])
	print("Objects in bag for Dynamic Programming:")
	print(dynProg[1])
	print("Time for Dynamic Programming:")
	print(endDP - startDP)
	print(" ")
	print("Maximum value for Greedy Method:")
	print(greMethod[0])
	print("Objects in bag for Greedy Method:")
	print(greMethod[1])
	print("Time for Greedy Method:")
	print(endGM - startGM)
	
def main():
	print("What would you like to do?")
	inp = input("Type 'run' to run file and 'exit' to exit program ")
	if inp == "run":
		 runAll()
	elif inp == "exit":
		exit()
	else:
		print("invalid input")
		main()
		
main()
