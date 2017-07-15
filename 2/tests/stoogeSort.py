import os, timeit, math

def stoogeSort(array, a, b):
	if array[b] < array[a]:
		array[a], array[b] = array[b], array[a]
	if b - a > 1:
		split = (b - a + 1) // 3
		stoogeSort(array, a, b-split)
		stoogeSort(array, a+split, b)
		stoogeSort(array, a, b-split)
	return array


def doSort(data):
    output = open("stooge.out", 'w+') # Our output file
    with open(data, 'r') as file:
        for line in file:
            data=[int(num) for num in line.split()]
            n = data.pop(0) #pop the number of items to sort because we don't need it, we're deliminated already by newline
            
            data_length = len(data)-1
            
            start_time = timeit.default_timer()
            stoogeSort(data, 0, data_length)
            elapsed = timeit.default_timer() - start_time

            print str(n)+","+str(elapsed)
            output.write(' '.join(str(x) for x in data)+"\n")
    output.close()

def doSortAllData():
	for file in os.listdir("."):
		if file.endswith(".txt"):
			doSort(file)

doSortAllData()
