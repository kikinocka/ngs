#!/bin/bash

sdir='/home/kika/ownCloud/pelomyxa/mito_proteins/complexII/'
msa=$sdir'aox_pfam.aln'
out_hmm=$sdir'aox_pfam_profile.hmm'
name='aox_pfam'
summary=$sdir'aox_pfam_build.out'
seq_type=amino
threads=4

hmmbuild -n $name -o $summary --$seq_type --cpu $threads $out_hmm $msa