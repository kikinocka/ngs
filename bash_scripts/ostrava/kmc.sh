#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N kmc
#PBS -l nodes=1:ppn=16
#PBS -l walltime=100:00:00


cd '/mnt/data/kika/blastocrithidia/genomes/o_modryi/reads/'

eval "$(/home/users/kika/miniconda3/bin/conda shell.bash hook)"
conda activate kmc

#The input is a set of trimmed genome sequencing reads, the more coverage the better 
#1st - Give KMC all the files with trimmed reads to calculate k-mer frequencies and then generate a histogram of k-mers

mkdir tmp
ls karect_modryi_trimmed_75_* > FILES  # creates a file with both read files

# kmer 27, 16 threads, 64G of memory, counting kmer coverages between 1 and 10000x
kmc -k27 -t16 -m64 -ci1 @FILES kmcdb tmp | tee kmc.log #run kmc 
kmc_tools transform kmcdb histogram kmcdb_k27.hist # create kmcdb_k27.hist

# -k<value>	kmer length
# -m<value>	approximate amount of RAM to use in GB (1 to 1024)
# -ci<value>	excludes kmers occurring less than <value> times
# -cs<value>	the maximum value of a counter
# FILES		file name with a list of input files
# kmcdb		the output file name prefix for the KMC database
# tmp			temporary directory
# -cx<value>	the maximum value of counter to be stored in the histogram file.
# -cs10000 and -cx10000 is suggested to run kmc without max. counter

conda deactivate

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: KMC done
