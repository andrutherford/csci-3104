import os
import sys
import math
import random
import fileinput
import csv
import decimal
from collections import defaultdict
from decimal import Decimal



def main(argv):
    checker = 0
    Apple_csv_file = '/home/user/Dropbox/CSCI 3104 - Algorithms/Homework 3/aapl.csv'
    Google_csv_file = "/home/user/Dropbox/CSCI 3104 - Algorithms/Homework 3/goog.csv"
    Microsoft_csv_file = "/home/user/Dropbox/CSCI 3104 - Algorithms/Homework 3/msft.csv"
    Apple_open,Apple_dates = specific_columns(Apple_csv_file)
    Google_open, Google_dates = specific_columns(Google_csv_file)
    Microsoft_open,Microsoft_dates = specific_columns(Microsoft_csv_file)
    Apple_differences = open_differences(Apple_open)
    Google_differences = open_differences(Google_open)
    Microsoft_differences = open_differences(Microsoft_open)
    left_index_apple, right_index_apple, Maximum_Profit_Apple = find_max_subarray(Apple_differences,0,len(Apple_differences)-1)
    left_index_google, right_index_google, Maximum_Profit_google = find_max_subarray(Google_differences,0,len(Google_differences)-1)
    left_index_microsoft, right_index_microsoft, Maximum_Profit_microsoft = find_max_subarray(Microsoft_differences,0,len(Microsoft_differences)-1)

    print "Company", " symbol", " Start date", " End date", " Buy date", " Sell date", " Maximum Profit", "\n"
    print "Apple ", "  AAPL  ", Apple_dates[0],"  ", Apple_dates[len(Apple_dates)-1],"  ", Apple_dates[left_index_apple],\
        "  ", Apple_dates[right_index_apple],"  ", Maximum_Profit_Apple, "\n"
    print "Google ", "  GOOG  ", Google_dates[0]," ", Google_dates[len(Google_dates)-1]," ", Google_dates[left_index_google],"  ", Google_dates[right_index_google],"  "\
        , Maximum_Profit_google, "\n"
    print "Microsoft ", "MSFT  ", Microsoft_dates[0],"  "\
        , Microsoft_dates[len(Microsoft_dates)-1],"  ", Microsoft_dates[left_index_microsoft],"  ", Microsoft_dates[right_index_microsoft],"  ", Maximum_Profit_microsoft


    return
def findmaxcrossingsubarray(A,Low,Mid,High):
    left_sum = Decimal('-Infinity')
    sum = 0
    max_left = 0
    max_right = 0
    for i  in range  (Mid,Low,-1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = Decimal('-Infinity')
    sum = 0
    for j in range (Mid+1,High):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return(max_left,max_right,(left_sum+right_sum))

def find_max_subarray(A ,low, high):
    if high==low:
        return(low,high,A[low])
    else:
        mid = (low+high)/2
        (left_low,left_high,left_sum)= find_max_subarray(A,low,mid)
        (right_low,right_high,right_sum)= find_max_subarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum) = findmaxcrossingsubarray(A,low,mid,high)
    if (left_sum>=right_sum)and (left_sum>=cross_sum):
        print left_low , left_high
        print(left_sum)
        return (left_low,left_high,left_sum)
    elif(right_sum>=left_sum)and (right_sum>=cross_sum):
        #print(right_sum)
        return (right_low,right_high,right_sum)
    else:
        #print(cross_sum)
        return (cross_low,cross_high,cross_sum)




def specific_columns(file):
    date_list = []
    date_list_final = []
    open_list = []
    open_list_final = []
    sum = 0
    with open(file) as csvfile:
        reader = csv.reader(open(file, 'rU'))
        for row in reader:
            date_list.append(row[0])
            open_list.append(row[3])
    for i in range (2,len(open_list)):
        open_list_final.append(Decimal(open_list[len(open_list)+1-i]))
        date_list_final.append(date_list[len(date_list)+1-i])


    return open_list_final, date_list_final

def open_differences(open_prices):
    differences = [0]
    for i in range(1,len(open_prices)-1):

        differences.append(open_prices[i]-open_prices[i-1])
    return differences






if __name__=="__main__":
    main(sys.argv)
