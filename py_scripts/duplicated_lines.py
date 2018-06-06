#!/usr/bin/env python3

file = open('/home/kika/MEGAsync/diplonema_mt/comparison/in')

unique = set()
for line in file:
	if line not in unique:
		unique.add(line)
	else:
		print(line)
