#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N kat
#PBS -l nodes=1:ppn=20
#PBS -l walltime=600:00:00

ulimit -n 4096
conda activate kat

work_dir='/mnt/data/kika/blastocrithidia/b_frustrata/kat/'
read_dir='/mnt/data/kika/blastocrithidia/b_frustrata/reads/'
fwd=$read_dir'karect_4FEM_trimmed_75_1.fq'
rev=$read_dir'karect_4FEM_trimmed_75_2.fq'
assembly='/mnt/data/kika/blastocrithidia/b_frustrata/spades_75_karect/contigs.fasta'
hist_prefix='hist_m27'
comp_prefix='comp_m27'

cd $work_dir

#k-mer spectra on reads
kat hist -m 27 -t 10 -o $hist_prefix.hist $fwd $rev 2> $hist_prefix.hist.log

#adjusting x-axis
kat plot spectra-hist -p pdf $hist_prefix.hist -x 250 -o $hist_prefix.x250.hist 2> $hist_prefix.plot.log

#k-mer spectra for assembly
kat comp -t 10 -m 27 -o $comp_prefix -p pdf $fwd $assembly 2> $comp_prefix.log
