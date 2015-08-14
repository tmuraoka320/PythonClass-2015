#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

def common_divisor(a, b):
	remain_list = []
	remain1 = max(a,b)%min(a,b)
	remain_list.append(remain1)
	remain2 = min(a,b)%remain1
	remain_list.append(remain2)
	for i in range(len(remain_list)):
		new_remain = remain_list[i]%remain_list[i+1]
		remain_list.append(new_remain)
		if new_remain == 0:
			break
	print remain_list[-2]

common_divisor(48,18)

#Exercise 2
#Write a function that returns prime numbers less than 121

import math

def prime_number(n):
	primes = [2]
	ls = xrange(3, n + 1 ,2)
	while ls:
		p = ls[0]
		if p > math.sqrt(n):
			primes += ls
			break
		primes.append(p)
		ls = filter(lambda x: x % p, ls)
	return primes

prime_number(121)

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html

def hanoi(n, tower1, tower2, tower3):
	



