#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N smudgeplot
#PBS -l nodes=1:ppn=16
#PBS -l walltime=100:00:00


cd '/mnt/data/kika/blastocrithidia/genomes/o_modryi/reads/'

eval "$(/home/users/kika/miniconda3/bin/conda shell.bash hook)"
conda activate smudgeplot


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


#2nd - kmer extraction
# The next step is to extract genomic kmers using reasonable coverage thresholds.
# You can either inspect the kmer spectra and choose the L (lower) and U (upper) coverage thresholds via visual inspection 
# or you can estimate them using command
# smudgeplot.py cutoff <kmcdb_k27.hist> <L/U>

L=$(smudgeplot.py cutoff kmcdb_k27.hist L)
#L='4' #trying this due to the previous warning
U=$(smudgeplot.py cutoff kmcdb_k27.hist U)

echo $L $U # these need to be sane values
# L should be like 20 - 200
# U should be like 500 - 3000


#3rd - extract kmers in the coverage range from L to U using kmc_tools
kmc_tools transform kmcdb -ci"$L" -cx"$U" reduce kmcdb_L"$L"_U"$U"


#4th - run smudge_pairs on the reduced file to compute the set of kmer pairs.
smudge_pairs kmcdb_L"$L"_U"$U" kmcdb_L"$L"_U"$U"_coverages.tsv kmcdb_L"$L"_U"$U"_pairs.tsv > kmcdb_L"$L"_U"$U"_familysizes.tsv

##if KMC is not available
#kmc_tools transform kmcdb -ci"$L" -cx"$U" dump -s kmcdb_L"$L"_U"$U".dump
#smudgeplot.py hetkmers -o kmcdb_L"$L"_U"$U" < kmcdb_L"$L"_U"$U".dump
###creates the same *tsv files


#5th - generate the smudgeplot using the coverages of the identified kmer pairs (*_coverages.tsv file).
# either supply the haploid kmer coverage (reported by GenomeScope) or let it be estimated directly from the data:
smudgeplot.py plot kmcdb_L"$L"_U"$U"_coverages.tsv

#running genomescope
kmc_tools transform kmcdb_L"$L"_U"$U" histogram kmer_k27.hist #-cx10000


python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: Smudgeplot done
