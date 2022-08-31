#!/usr/bin/env python3

# courtesy of laelbarlow

"""
This script adds bootstrap support values from a bootstrap pseudoreplicate tree
file (newick format) to a MrBayes tree (MrBayes nexus format) with posterior
probabilities, and outputs a tree with combined support values in newick format. 
Usage:
    python3 boots_on_mb.py <MrBayes consensus tree file NEXUS> <Bootstrap tree file NEWICK> <Output tree file NEWICK>
"""

import sys
import os
import shutil
import subprocess
import re
import time
from ete3 import Tree


def reformat_combined_supports(tree_string):
    cs = re.compile(r'\)\d+:')
    inum = 0
    for instance in cs.findall(tree_string):
        inum += 1
        # Define a reformatted support string.
        supcomb = str(int(float(instance[1:-1])))
        supcomb2 = ''

        if supcomb == '0':
            supcomb2 = '0.0/0'
        elif supcomb == '1':
            supcomb2 = '0.0/1'
        else:
            boot = supcomb[-3:].lstrip('0')
            if boot == '':
                boot = '0'
            prob = str(int(supcomb[:-3])/100)

            supcomb2 = prob + '/' + boot

        # Replace the instance with a reformatted support string in the
        # tree_string.
        tree_string = tree_string.replace(instance, instance[0] +\
                supcomb2 + instance[-1])

    assert inum >= 2, """Could not parse combined supports in intermediate tree."""

    # Return modified tree string.
    return tree_string


def combine_supports(boot_newick, prob_newick, combined_figtree_newick):
    """Takes two newick files and writes another newick file that when opened
    in figtree will show posterior probabilities and bootstrap values together.
    """
    # Define function for adding zeros as necessary.
    get_3_digit = lambda x: '0'*(3 - len(x)) + x
    
    # Parse the input newick tree files.
    boot_newick_tree = Tree(boot_newick)
    prob_newick_tree = Tree(prob_newick)

    # Root trees on the same node arbitrarily.
    arbitrary_leaf_node = prob_newick_tree.get_leaves()[0]
    prob_newick_tree.set_outgroup(arbitrary_leaf_node.name)
    boot_newick_tree.set_outgroup(arbitrary_leaf_node.name)

    # Iterate through the rooted trees matching nodes and combining the support
    # values onto a single tree.
    for n1 in prob_newick_tree.traverse():
        found_boot = False
        if len(n1.get_leaf_names()) > 1:
            for n2 in boot_newick_tree.traverse():
                if set(n1.get_leaf_names()) == set(n2.get_leaf_names()):
                    found_boot = True

                    mb_support = str(n1.support)[:-2]
                    raxml_support = get_3_digit(str(n2.support)[:-2])

                    combined_support = mb_support + raxml_support
                    n1.support = int(combined_support)

        # Make sure that all the right nodes were identified.
        if not found_boot:
            if len(n1.get_leaves()) == 1:
                found_boot = True
        assert found_boot, "Error: could not identify one of the nodes in the tree with bootstrap supports."

    # Write the newick tree file to a temporary output file.
    temp_file = combined_figtree_newick + '_temp.newick'
    prob_newick_tree.write(outfile=temp_file)

    # Reformat supports in temporary file with tree so that they will be
    # displayed properly in FigTree.
    with open(temp_file) as infh, open(combined_figtree_newick, 'w') as o:
        for i in infh:
            # Call function to reformat tree string.
            new_tree_string = reformat_combined_supports(i)
            # Write reformatted tree string.
            o.write(new_tree_string)

    # Remove temporary file.
    os.remove(temp_file)


def mbcontre_to_newick_w_probs(intreepath, outtreepath):
    # Construct a taxon number: name dict.
    tax_dict = {}
    x = re.compile(r'\t\t\d')
    with open(intreepath) as infh:
        for i in infh:
            if x.search(i):
                split = i.split('\t')
                num = split[2]
                name = split[3].replace(',', '').strip()
                tax_dict[num] = name

    # Get the line with the tree as a string.
    intreestring = ''
    with open(intreepath) as infh:
        for i in infh:
            if i.startswith('   tree con_all_compat'):
                intreestring = i

    # Cleanup string.
    intreestring2 = '(' + intreestring.split('(', 1)[1]

    # Define REs to identify unnecessary information in tree string.
    extra1_external = re.compile(r'\d\[&prob=[\w\s,.+-={}_()"]+\]')
    extra1 = re.compile(r'\[&prob=[\w\s,.+-={}_()"]+\]')
    extra2 = re.compile(r'\[&length_mean=[\w\s,.+-={}_()"%]+\]')

    intreestring3 = intreestring2

    # Remove terminal node probability labels.
    for i in extra1_external.findall(intreestring3):
        intreestring3 = intreestring3.replace(i, i[0])

    # Reformat internal node probability labels.
    for i in extra1.findall(intreestring3):
        # Calculate a replacement percent probability value.
        replacement = str(round(float(i.split('=', 1)[1].split(',', 1)[0]) * 100))

        # Replace long annotation with replacement percent probability.
        intreestring3 = intreestring3.replace(i, replacement)

    # Remove unnecessary branch length annotation.
    intreestring3 = extra2.sub('', intreestring3)
    
    # Construct a list of taxon numbers in string.
    z = re.compile(r'[(|,]\d+:')
    tax_nums = z.findall(intreestring3)

    # Replace taxon numbers with names.
    intreestring4 = intreestring3
    for key in tax_dict.keys():
        for tax_num in tax_nums:
            if key == tax_num[1:-1]:
                intreestring4 = intreestring4.replace(tax_num, tax_num[0] + tax_dict[key] + tax_num[-1])

    # Replace scientific notation numbers to decimal form so RAxML can parse.
    # (May not be necessary)
    y = re.compile(r':[\w.-]+\+?\d+')
    numbers = y.findall(intreestring4)
    intreestring5 = intreestring4
    for num in numbers:
        numx = num.strip(':')
        repl = '{:.7f}'.format(float(numx))
        intreestring5 = intreestring5.replace(numx, repl)

    # Write final tree string to output file.
    with open(outtreepath, 'w') as o:
        o.write(intreestring5)


def mb_contre_to_newick(intreepath, outtreepath):
    """Takes a .con.tre file output from MrBayes and writes the same tree in
    newick format.
    """
    # Construct a taxon number: name dict.
    tax_dict = {}
    x = re.compile(r'\t\t\d')
    with open(intreepath) as infh:
        for i in infh:
            if x.search(i):
                split = i.split('\t')
                num = split[2]
                name = split[3].replace(',', '').strip()
                tax_dict[num] = name

    # Get the line with the tree as a string.
    intreestring = ''
    with open(intreepath) as infh:
        for i in infh:
            if i.startswith('   tree con_all_compat'):
                intreestring = i
    assert intreestring != '', """Could not find line with tree."""

    # Cleanup string.
    intreestring2 = '(' + intreestring.split('(', 1)[1]

    # Remove unnecessary information from tree string.
    extra1 = re.compile(r'\[&prob=[\w\s,.+-={}_()"]+\]')
    extra2 = re.compile(r'\[&length_mean=[\w\s,.+-={}_()"%]+\]')
    intreestring3 = extra1.sub('', extra2.sub('', intreestring2))

    # Construct a list of taxon numbers in string.
    z = re.compile(r'[(|,]\d+:')
    tax_nums = z.findall(intreestring3)

    # Replace taxon numbers with names.
    intreestring4 = intreestring3
    for key in tax_dict.keys():
        for tax_num in tax_nums:
            if key == tax_num[1:-1]:
                intreestring4 = intreestring4.replace(tax_num, tax_num[0] + tax_dict[key] + tax_num[-1])

    # Replace scientific notation numbers to decimal form so RAxML can parse.
    #y = re.compile(r':[\w.-]+')
    y = re.compile(r':[\w.-]+\+?\d+')
    numbers = y.findall(intreestring4)
    intreestring5 = intreestring4
    for num in numbers:
        numx = num.strip(':')
        repl = '{:.7f}'.format(float(numx))
        intreestring5 = intreestring5.replace(numx, repl)
    
    # Write final tree string to output file.
    with open(outtreepath, 'w') as o:
        o.write(intreestring5)


if __name__=='__main__':

    # Parse command-line arguments.
    mrbayes_tree = sys.argv[1]
    bootstrap_trees = sys.argv[2]
    output_tree = sys.argv[3]

    # Check that the output directory exists.
    outdir = os.path.abspath(os.path.dirname(output_tree))
    assert os.path.isdir(outdir), """Could not find output directory."""

    # Delete output file if it already exists.
    if os.path.isfile(output_tree):
        os.remove(output_tree)
    
    # Make temporary output directory.
    temp_outdir = os.path.join(outdir, 'boots_on_mb_TEMP_' + str(time.time()))
    os.mkdir(temp_outdir)
    
    # Convert MrBayes output .con.tre file to newick files.
    mrbayes_tree_newick1 = os.path.join(temp_outdir, 'TEMP1.tre')
    mb_contre_to_newick(mrbayes_tree, mrbayes_tree_newick1)
    mrbayes_tree_newick2 = os.path.join(temp_outdir, 'TEMP2.tre')
    mbcontre_to_newick_w_probs(mrbayes_tree, mrbayes_tree_newick2)

    # Define name of RAxML executable in $PATH (this may be different for
    # different installations).
    raxmlname='raxmlHPC'

    # Call RAxML (needs to be in $PATH) to map bootstraps onto newick of mb tree.
    outname = 'mapped'
    subprocess.call([raxmlname, '-f', 'b', '-t', mrbayes_tree_newick1, '-z', bootstrap_trees,\
    '-n', outname, '-m', 'PROTGAMMALG4X', '-w', temp_outdir], cwd=os.getcwd()) 
    raxml_output = os.path.join(temp_outdir, 'RAxML_bipartitions.' + outname)

    # Remove temporary directory.
    # shutil.rmtree(temp_outdir)
