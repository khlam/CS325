default: change

run:
	python change.py 2> change.txt

change: clean amount.txt
	python change.py 2> change.txt

amount.txt:
	echo "1 2 5" >amount.txt
	echo "10" >>amount.txt
	echo "1 3 7 12" >>amount.txt
	echo "29" >>amount.txt
	echo "1 2 4 8" >>amount.txt
	echo "15" >>amount.txt

clean:
	rm -f *.txt