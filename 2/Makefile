default: run

stoogeSort: stoogeSort.py
	python stoogeSort.py

printOut:
	cat stooge.out

data.txt:
	echo "4 19 2 5 11" > data.txt
	echo "8 1 2 3 4 5 6 1 2" >> data.txt

genRand: clean
	python genRandom.py
	python stoogeSort.py >> stooge.csv

run: data.txt stoogeSort printOut

clean:
	rm -f *.out
	rm -f *.txt