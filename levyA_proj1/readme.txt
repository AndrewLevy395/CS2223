Andrew Levy

levyA_proj1.py

Run through command prompt with the command: py levyA_proj1.py

When the program is run, the user will be prompted to input two positive integers in two seperate statements.
If the user does not input a positive integer for either of the two inputs then they will prompted once again
two input to positive integers. If the user fails to type valid inputs three seperate times then the program will end
and say "goodbye!". No test will be done and no results will be displayed. If the user provides valid inputs then
the program will run all the way through and return the time it took to run each algorithm as well as the GCD found
by each one, which should be equal for all algorithms. 

I conducted my experiment by running three algorithms given the same input and then timing each algorithm to see which one ran the fastest. 
I did this by measuring the runtime time before and after each algorithm and subtracting them to get the runtime of the algorithm. 

The most efficient algorithm for time efficiency is the Euclid Method. The running time of this algorithm is logarithmic so it is faster than the 
two other methods, which are both linear. This is proved in the runtime data. The Euclid method has the fastest runtime in every single test case. 
The least efficient method for time was the integer check method. For eight out of ten tests, this method had the longest runtime. In the two tests, 
the slowest runtime was the middle school method. This is because as the inputs get smaller, the integer check method becomes slightly faster than 
the middle school method.

The most efficient algorithm for space efficiency was the Euclid Method. This method and the integer check method are both constant in terms of space 
efficiency so it is known that they are both more space efficient than the middle school method. The Euclid method is more space efficient than the 
integer check method because it uses less variables to store information. The least space efficient algorithm is the middle school method because it 
is logarithmic.

During this test, I learned that three different algorithms that all do the same thing and return the same results do not always take the same amount 
of time or use the same amount of space. Keeping this in mind is very important when working on a larger scale. Saving space and time can be very 
important in very large programs and the more time and space saved the better. I also learned that in order to find a GCD, the most efficient method 
is Euclid’s Method because it has the fastest runtime and uses the least amount of space.
