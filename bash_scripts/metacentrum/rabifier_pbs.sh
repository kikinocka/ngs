#!/bin/bash
#PBS -N rabifier
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add rabifier-2.0.2 

datadir='/storage/brno12-cerit/home/kika/anaeramoeba/RABs'

#copy files to scratch
cp $datadir'/'*.fa $SCRATCHDIR


#run on scratch
cd $SCRATCHDIR

for fasta in *.fa; do
	echo $fasta
	rabifier --cpu $PBS_NUM_PPN $fasta
	echo ***Rabifier done***
done
# optional arguments:
#   -h, --help            show this help message and exit
#   -v, --version         show program's version number and exit
#   -o OUTPUT, --output OUTPUT
#                         output file name [-]
#   --outfmt {text,json,csv}
#                         output format [text]
#   --show_positive       include only Rab positive predictions in the output
#   --cpu CPU             maximal number of threads to use [1]
#   --fast                phase 1 speedup: stop if it is not a G protein (does
#                         not show the full summary)
#   --bh_evalue BH_EVALUE
#                         e-value threshold for best hit search [1e-10]
#   --motif_evalue MOTIF_EVALUE
#                         e-value threshold for motif search [1e-04]
#   --motif_number MOTIF_NUMBER
#                         minimum number of RabF motifs [1]
#   --subfamily_identity SUBFAMILY_IDENTITY
#                         minimum sequence identity with subfamily's best hit
#                         [0.4]
#   --subfamily_score SUBFAMILY_SCORE
#                         minimum subfamily score [0.2]


#copy files back
rm *.fa
cp -r * $datadir
