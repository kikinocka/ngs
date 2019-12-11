#!/bin/sh

# of='/home/serafim/tools/OrthoFinder-2.1.2_source/orthofinder/orthofinder.py'
# new_prot='/media/4TB1/blastocrithidia/predicted_proteins/'
prev_blast='/media/4TB1/blastocrithidia/orthofinder/Results_Jan03/WorkingDirectory/'
# blast_method=diamond

orthofinder -b $prev_blast -t 32
# -S $blast_method -f $new_prot