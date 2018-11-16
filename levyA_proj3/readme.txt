Andrew Levy

levyA_proj3.py

Run through command prompt with the command: py levyA_proj2.py

The program will read a set of points through the input text file named 'input.txt'. This text file can be adjusted to test different points.
The program returns the time of each of the two algorithms run as well as the shortest distance that each algorithm calculated 
(which both algorithms should be the same). Test cases and time efficiencies for algorithms can be found in proffesional report.

1.	Time Efficiencies: (W is Capacity)

Brute Force	Dynamic Programming	Greedy Method
O(n2n)	  	O(nW)	   		O(nlog(n))
	
	Space Efficiencies:

Brute Force	Dynamic Programming	Greedy Method
O(n2n)		O(nW)			O(n)

2.	The greedy algorithm does not provide an optimal solution for solving the problem. This is because the greedy method does not 
search for each possible outcome but instead searches for the item with the highest ratio first. The brute force and the dynamic 
programming algorithms do provide optimal solutions for the problem. This is because they both search for the highest possible outcome 
in the problem by searching through all of the outcomes. This results in neither of the algorithms being in polynomial time because the 
knapsack problem is NP Complete.

3. 	Test cases were performed.

4.	The best knapsack solution for time is the Greedy Method. This method is the fastest throughout all of the test cases by a 
significant amount. This method has the fastest time complexity at n(log(n)). As the capacity (W) increases, nW becomes greater than nlog(n). 
(W > log(n)). However, the greedy method is not always the best solution for all cases. This is because when the number of items to be placed 
in the knapsack, and the capacity are very small, the Brute Force method becomes the fastest of the algorithms. However the greedy method does 
not always provide an optimal solution for the problem.

The best overall solution is the dynamic programming. This is because it provides the fastest solution while also being an optimal and correct 
solution to the problem. When there are a small amount of items, the brute force method is the fastest. However, when there are a larger amount 
of items, the dynamic programming solution becomes significantly faster. Therefore, it is not the most efficient for all examples, but for most 
large examples it is.

