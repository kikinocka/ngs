#!/usr/bin/env python3
import os
import re
import pandas as pd

os.chdir('/Users/kika/ownCloud/diplonema/up-down_list/')
files = [x for x in os.listdir() if x.endswith('.list')]

os.chdir('/Users/kika/ownCloud/diplonema/metabolism/ms_data/')
msdata = pd.read_excel('200423-200513_report_diplonema.xlsx', sheet_name='Tree significant proteins comme')
accs = msdata['T: Protein IDs'].to_list()

for i in accs:
	m = re.search(r'.*.mRNA.\d+', i)
	print(i)
	print(m.group())
	