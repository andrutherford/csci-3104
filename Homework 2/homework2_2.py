import os
import sys
import random
import time
import math
from fractions import gcd

def main(argv):
	
	x = int(input("Message: "))
	print " "
	
	start_time_total = time.time()
	start_time_a = time.time()
	p, q, N = public_key()
	run_time_a = time.time() - start_time_a
	
	
	start_time_b = time.time()
	primes = prime_numbers()
	e = get_e(primes, (p-1), (q-1))
	print " "
	print "p = ", p
	print "q = ", q
	print "N = ", N
	print "e = ", e
	k = modinv(((p-1) * (q-1)),e)
	print "k = ", k, "\n"
	y = encrypt(x, N, e)
	run_time_b = time.time() - start_time_b
	print "Encrypted message = ", y, "\n"
	
	start_time_c = time.time()
	x = decryption(y, k, N)
	run_time_c = time.time() - start_time_c
	run_time_total = time.time() - start_time_total
	print "Decrypted message = ", x, "\n"
	

	print "Generated public and private keys in: ", run_time_a, " sec."
	print "Encoded message in: ", run_time_b, " sec."
	print "Decoded message in: ", run_time_c, " sec."
	print "Total run time: ", run_time_total, " sec."

	return
	
	
	
	
def public_key():
	list = prime_numbers()
	p, q = get_N(list)
	while(p == q):
		while(len(bin(p))!= len(bin(q))):
			p,q = get_N(list)
	N = p * q
	return(p, q, N)
	
def prime_numbers():
	n = 300
	min = 2
	max = n
	Primes_generator = [0, 0]
	primes = []
	for k in range(min, max ** 2):
		Primes_generator.append(1)
	for i in range(min, len(Primes_generator)):
		if Primes_generator[i] == 1:
			for j in range(min, len(Primes_generator)):
				ji = j * i
				if(ji < len(Primes_generator)):
					ji = j * i
					Primes_generator[ji] = 0
	for num in range(0,max ** 2):
		if Primes_generator[num] == 1:
			primes.append(num)
	print "n = ", n
	return primes
    
def get_e(primes, p, q):
	totient = p * q
	d = 0 
	i = 1
	while d != 1:
		e = primes[i]
		d = gcd(totient, e)
		i = i +1
	return e

def get_N(primes):
	IndexP = random.randint(0, len(primes)-1)
	IndexQ = random.randint(0, len(primes)-1)
	p = primes[IndexP]
	q = primes[IndexQ]
	return p, q
    
def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q,r = b//a,b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y
    
def modinv(a, m):
	d, y, x = egcd(a, m)
	if d != 1:
		return None
	else:
		return x % a


def encrypt(x, N, e):
	y = x**e % N
	return y
    
def decryption(x, y, N):
	if y == 0: return 1
	z  = decryption(x, (y/2), N)
	if y % 2 == 0:
		return z**2 % N
	else:
		return x * z**2 % N
        
if __name__ == "__main__":
    main(sys.argv)
