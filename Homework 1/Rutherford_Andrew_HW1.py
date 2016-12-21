import os
import sys
import random
import time

def main(argv):
	min = 0
	max = 0
	sum = 0

	n = (int(input("n = ")))
	for i in range (0,10):
		start_time=time.time()
		randomlist(n)
		run_time = time.time() - start_time
		print(run_time)
		if i == 0:
			min = run_time
			max = run_time
			sum = run_time
		else:
			sum += run_time
			if run_time < min:
				min = run_time
			if run_time > max:
				max = run_time
	avg = sum / 10
	print "Min = ", min
	print "Max = ", max
	print "Avg = ", avg
	return
	
def randomlist(n):
	intlist = []
	for i in range (0, n):
		k = random.randrange(0,(10*n))
		intlist.append(k)
	intlist = selection_sort(intlist)
	#print(intlist)
	
def selection_sort(list):
    for index in range(0, len(list)):
        iSmall = index
        for i in range(index,len(list)):
            if list[iSmall] > list[i]:
                iSmall = i
        list[index], list[iSmall] = list[iSmall], list[index]
    return list  
	
if __name__ == "__main__":
	main(sys.argv)
	
