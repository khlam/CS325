import timeit, os
#Kin-Ho Lam
#Summer 2017 
#CS 325 Assignment 1
#Insertion Sort Python
#insertSort source: https://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
def insertSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue


def doSort(data):
    output = open("insert.out", 'w+') # Our output file
    with open(data, 'r') as file:
        for line in file:
            data=[int(num) for num in line.split()]
            n = data.pop(0) #pop the number of items to sort because we don't need it, we're deliminated already by newline
            start_time = timeit.default_timer()
            insertSort(data)
            elapsed = timeit.default_timer() - start_time
            print str(n)+","+str(elapsed)
            output.write(' '.join(str(x) for x in data)+"\n")
    output.close()

def doSortAllData():
   # print "Insert Sort"
  #  print "n,Time(Seconds)"
    for file in os.listdir("./ec/worst/"):
        if file.endswith(".credit"):
            doSort("./ec/worst/"+file)
doSortAllData()

#doSort("data.txt")