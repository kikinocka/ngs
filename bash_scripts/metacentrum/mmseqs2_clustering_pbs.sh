#!/bin/bash
#PBS -N mmseqs2
#PBS -l select=1:ncpus=20:mem=30gb:scratch_local=20gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

mmseqs='/storage/brno3-cerit/home/kika/miniconda3/bin/mmseqs'
data_dir='/storage/brno3-cerit/home/kika/trafficking/wdr/'

#copy files to scratch
cp $data_dir'wdr_interpro.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

fasta='wdr_interpro.fa'
prefix='wdr_interpro'

$mmseqs easy-linclust $fasta $prefix tmp --min-seq-id 0.95 -c 0.3 --cov-mode 1 --cluster-mode 2
# --min-seq-id FLOAT	List matches above this sequence identity (for clustering) (range 0.0-1.0) [0.000]
# -c FLOAT         		List matches above this fraction of aligned (covered) residues (see --cov-mode) [0.800]
# --cov-mode INT   		0: coverage of query and target
#                   	1: coverage of target
#                   	2: coverage of query
#                   	3: target seq. length has to be at least x% of query length
#                   	4: query seq. length has to be at least x% of target length
#                   	5: short seq. needs to be at least x% of the other seq. length [0]
# --cluster-mode INT	0: Set-Cover (greedy)
#                   	1: Connected component (BLASTclust)
#                   	2,3: Greedy clustering by sequence length (CDHIT) [0]


#copy files back
rm -r $fasta tmp
cp -r * $data_dir
