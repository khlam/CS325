from random import randint

def genRand(n):
	array = []
	array.append(n)
	for i in range(0, n):
		array.append(randint(0, 10000))
	output = open("data"+str(n)+".txt", 'w+')
	output.write(' '.join(str(x) for x in array)+"\n")
	output.close()


n = 10
iteration = 10
for i in range (1, iteration+1):
	genRand(i * n)
