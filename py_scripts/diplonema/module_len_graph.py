#!/usr/bin/env python3
import os
import csv
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/home/kika/MEGAsync/diplonema_mt/')
ypf1601 = csv.reader(open('1601/1601_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)
ypf1604 = csv.reader(open('1604/1604_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)
ypf1608 = csv.reader(open('1608/1608_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)
ypf1618 = csv.reader(open('1618/1618_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)
ypf1610 = csv.reader(open('1610/1610_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)

def csv_parser(file):
	module_list = []
	for row in file:
		module_list.append(row[1])
	return module_list

llan = csv_parser(ypf1601)
djap = csv_parser(ypf1604)
rhum = csv_parser(ypf1608)
sspe = csv_parser(ypf1618)
ypf10 = csv_parser(ypf1610)


y = [djap, rhum, llan, sspe, ypf10] #dosad hodnoty velkosti modulov
x = [1,2,3,4,5] #zoznam modulov, musia byt cisla myslim

data = []
for i in y:
    data.append(np.array(i))
fig = plt.figure()
plt.boxplot(data, notch=True)

for xe, ye in zip(x, y):
    plt.plot([xe] * len(ye), ye, 'o', mfc='none', c='black')
    
plt.xticks([1, 2, 3, 4, 5])
plt.axes().set_xticklabels(['D.jap', 'R.hum', 'L.lan', 'S.spe', 'YPF'])

plt.show()
