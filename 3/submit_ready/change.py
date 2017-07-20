#Kin-Ho Lam
#Summer 2017 
#CS 325 Assignment 3
#Make Change Python
from __future__ import print_function
import os, timeit, itertools, sys

def stErrPrint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def stOutPrint(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)

def getCoins(A, n): # Get the exact coins we use to form our solution
	coinCount = [0] * (len(n))
	coinCount[formedby[A]] = 1
	while(A != 0):
		A = A - n[formedby[A]]
		if (A != 0):
			coinCount[formedby[A]] += 1
	return coinCount
	
def doChange(n, A): # My change algorithm implimented in python from Question 3
	global formedby
	total = [A+1] * (A+1)
	formedby = [0] * (A+1)
	total[0] = 0
	for i in range(0, len(n)):
		for j in range(0, len(total)):
			if n[i] <= j:
				if (total[j] > 1+total[j-n[i]]): 
					total[j] = 1+total[j-n[i]] # Needed to make a small change so we keep track of the coins
					formedby[j] = i;
	return str(total[A])

def getChange(data):
    with open(data) as file:
    	for line1,line2 in itertools.izip_longest(*[file]*2):
    		stErrPrint(' '.join(str(i) for i in map(int ,line1.split(' '))))
    		stErrPrint(str(int(line2)))
    		start_time = timeit.default_timer() #Start timer
    		minCoins = doChange(map(int ,line1.split(' ')), int(line2))
    		elapsed = timeit.default_timer() - start_time #End timer
    		#stOutPrint(str(elapsed))
        	stErrPrint(' '.join(str(i) for i in getCoins(int(line2), map(int ,line1.split(' ')))))
        	stErrPrint(minCoins)

getChange("amount.txt")

