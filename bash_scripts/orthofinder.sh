#!/bin/sh

# of='/home/serafim/tools/OrthoFinder-2.1.2_source/orthofinder/orthofinder.py'
new_prot='/media/4TB1/blastocrithidia/predicted_proteins'
prev_blast='/home/anzhelika/orthofinder_dataset_for_Anna/orthofinder/Results_Jan03/WorkingDirectory/'
# blast_method=diamond

orthofinder -f $new_prot -b $prev_blast -t 32
# -S $blast_method