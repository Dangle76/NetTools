#!/usr/bin/python

def digit_sum(n):
	x = str(n)
	total = 0
	for i in x:
		total += int(i)
	print total


digit_sum(434)
