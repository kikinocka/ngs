#!/bin/bash
#PBS -N mafft
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module add conda-modules-py37
# conda activate mafft
module add mafft-7.453

data_dir='/storage/brno3-cerit/home/kika/diplonema/aceE/ver5/'

#copy files to scratch
cp $data_dir'aceE.fa' $SCRATCHDIR
# cp $data_dir'discobids_otus.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

#align de-novo
fa='aceE.fa'
aln=${fa%.fa}.mafft.aln
log=${fa%.fa}.mafft.log

mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --inputorder ${fa} > ${aln} 2> ${log}


# #add to aligned sequences
# existing='discobids_eukref.mafft_merge.aln'
# add='discobids_otus.fa'
# aln='discoba_V9.mafft.aln'
# log='discoba_V9.mafft.log'

# # mafft --add $add --thread $PBS_NUM_PPN --inputorder $existing > $aln 2> $log
# mafft --addfragments $add --thread $PBS_NUM_PPN --inputorder $existing > $aln 2> $log


#copy files back
rm $fa
# rm $existing $add
cp * $data_dir
