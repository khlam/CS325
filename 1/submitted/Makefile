default: run

mergeSort: mergeSort.py
	python mergeSort.py

insertSort: insertSort.py
	python insertSort.py

printOut:
	cat merge.out
	cat insert.out

data.txt:
	echo "4 19 2 5 11" > data.txt
	echo "8 1 2 3 4 5 6 1 2" >> data.txt

run: data.txt mergeSort insertSort

genRand: clean
	python genRandom.py
	python mergeSort.py > trials.csv
	python insertSort.py >> trials.csv
	
clean:
	rm -f merge.out
	rm -f insert.out
	rm -f *.txt