import os
import sys
import random
import time
import math
import csv
from fractions import gcd
import decimal

def main(argv):
	
	array = []
	
	with open('stocks.csv', 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			#print(row['open'])
			array.append(row['open'])
		start = 0
		end = len(array)
		find_max_subarray(array, start, end)
		#print(A[0])
		#print(A[1])	
		#print(A[2])
	
	return
	

def find_max_crossing_subarray(A, low, mid, high):
	left_sum = -sys.maxint - 1
	asum = 0
	for i in range(int(mid), low):
		asum = asum + A[i]
		if (asum > left_sum):
			left_sum = asum
			max_left = i
	right_sum = -sys.maxint - 1
	asum = 0
	for j in range((int(mid) + 1), high):
		asum = asum + A[j]
		if (asum > right_sum):
			right_sum = asum
			max_right = j
	return max_left, max_right, left_sum + right_sum
		
			
	
def find_max_subarray(A, low, high):
	low = int(low)
	high = int(high)
	if (high == low):
		return low, high, A[low]	##base case
	else:
		print(low)
		print(high)
		mid = math.floor((low + high) / 2)
		left_low, left_high, left_sum = find_max_subarray(A, low, mid)
		right_low, right_high, right_sum = find_max_subarray(A, (mid + 1), high)
		cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
		if ((left_sum >= right_sum) & (left_sum >= cross_sum)):
			return left_low, left_high, left_sum
		elif ((right_sum >= left_sum) & (right_sum >= cross_sum)):
			return right_low, right_high, right_sum
		else:
			return cross_low, cross_high, cross_sum
			

	
if __name__ == "__main__":
    main(sys.argv)
