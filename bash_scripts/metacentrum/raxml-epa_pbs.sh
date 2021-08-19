#!/bin/sh
#PBS -N raxml-epa
#PBS -l select=1:ncpus=20:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add raxml-8.2.8

data='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/18S_trees/test_EPA/'

#copy files to scratch
cp $data'18S_green_ref.tre' $SCRATCHDIR
cp $data'18S_trimmed.fasta.aln' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

aln='18S_trimmed.fasta.aln'
tree='18S_green_ref.tre'
out='EPARUN'

raxmlHPC-PTHREADS -f v -G 0.2 -m GTRCATI -n $out -s $aln -t $tree -T $PBS_NUM_PPN


#copy files back
rm $aln $tree
cp -R * $data
