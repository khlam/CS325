from random import randint
import random

def genArray(n):
	array = [1]
	array+=(random.sample(xrange(1,n+1), n-1))
	return array


def generate(n, A, docName):
	output = open(docName, 'a+')
	output.write(' '.join(str(x) for x in n)+"\n")
	output.write(str(A)+"\n")
	output.close()

n = genArray(randint(1, 50)) # n constant, vary A 
for i in range(1, 1001):
	A = i
	generate(n, A, "0.txt")

A = randint(1, 49) 			# A constant, vary n
for i in range(1, 1001): 
	n = genArray(i)
	generate(n, A, "1.txt")

for i in range(1, 1001): 	#increase/vary both n and A
	n = genArray(i)
	A = i
	generate(n, A, "2.txt")