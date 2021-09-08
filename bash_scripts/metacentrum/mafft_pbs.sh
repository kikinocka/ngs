#!/bin/bash
#PBS -N mafft
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add conda-modules-py37
conda activate mafft

data_dir='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/metamonada/'

#copy files to scratch
cp $data_dir'metamonads_eukref.barthelona.anaeramoeba.aln' $SCRATCHDIR
cp $data_dir'metamonads_otus.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

# #align de-novo
# fa='rabs.fa'
# aln=${fa%.fa}.mafft.aln
# log=${fa%.fa}.mafft.log

# mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --inputorder ${fa} > ${aln} 2> ${log}


#add to aligned sequences
existing = 'metamonads_eukref.barthelona.anaeramoeba.aln'
add = 'metamonads_otus.fa'
aln = 'metamonads_V9.mafft.aln'
log = 'metamonads_V9.mafft.log'

# mafft --add {$add} --thread $PBS_NUM_PPN --inputorder ${existing} > ${aln} 2> ${log}
mafft --addfragments ${add} --thread $PBS_NUM_PPN --inputorder ${existing} > ${aln} 2> ${log}


#copy files back
# rm $fa
rm $existing $add
cp * $data_dir
