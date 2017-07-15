import timeit, os
#Kin-Ho Lam
#Summer 2017 
#CS 325 Assignment 1
#Merge Sort Python
# mergeSort source: https://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def doSort(data):
    output = open("merge.out", 'w+') # Our output file
    with open(data, 'r') as file:
        for line in file:
            data=[int(num) for num in line.split()]
            n = data.pop(0) #pop the number of items to sort because we don't need it, we're deliminated already by newline
            start_time = timeit.default_timer()
            mergeSort(data)
            elapsed = timeit.default_timer() - start_time
            print str(n)+","+str(elapsed)
            output.write(' '.join(str(x) for x in data)+"\n")
    output.close()

def doSortAllData():
	for file in os.listdir("."):
		if file.endswith(".txt"):
			doSort(file)
doSortAllData()
