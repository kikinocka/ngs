#!/usr/bin/python3

#file in format Acc. number \t name of organism \n
names = open('/home/kika/MEGAsync/Publikacie/Rheb/figures/species.txt', 'r')
tree = open('/home/kika/MEGAsync/Publikacie/Rheb/figures/Euglenozoa_rheb_tree.txt', 'r')

name_dict = {}
for name in names:
    split_line = name.split('\t')
    name_dict[split_line[0]] = split_line[1][:-1]

tree_line = tree.readline()

for key in name_dict:
    tree_line = tree_line.replace(key, name_dict[key])


#2 ways of writting results to the file:
##1) can't forget to close the file in the end of the code
##result = open('Tree_renamed.txt', 'w')
##result.write(tree_line)
##result.close()

#2) closes result file automatically
with open('/home/kika/MEGAsync/Publikacie/Rheb/figures/Euglenozoa_rheb_tree_renamed.txt', 'w') as result:
    result.write(tree_line)