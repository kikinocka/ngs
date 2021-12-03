#!/bin/bash
#PBS -N mafft
#PBS -l select=1:ncpus=40:mem=20gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module add conda-modules-py37
# conda activate mafft
# module add mafft-7.453
module add mafft-7.487 

data_dir='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/ciliates/'

#copy files to scratch
cp $data_dir'ciliates_V9_above99.mafft.aln' $SCRATCHDIR
cp $data_dir'outgroup.mafft.aln' $SCRATCHDIR
cp $data_dir'ciliates_outgroup_V9_above99.table' $SCRATCHDIR
cp $data_dir'ciliates_outgroup_V9_above99.in' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

# #align de-novo
# fa='aceE.fa'
# aln=${fa%.fa}.mafft.aln
# log=${fa%.fa}.mafft.log

# mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --inputorder ${fa} > ${aln} 2> ${log}


# #add to aligned sequences
# existing='discobids_eukref.mafft_merge.aln'
# add='discobids_otus.fa'
# aln='discoba_V9.mafft.aln'
# log='discoba_V9.mafft.log'

# # mafft --add $add --thread $PBS_NUM_PPN --inputorder $existing > $aln 2> $log
# mafft --addfragments $add --thread $PBS_NUM_PPN --inputorder $existing > $aln 2> $log


#merge alignments and fasta files
maketable='/software/mafft/7.487/core/makemergetable.rb'
aln1='ciliates_V9_above99.mafft.aln'
# fasta='outgroup.fa'
aln2='outgroup.mafft.aln'
input='ciliates_outgroup_V9_above99.in'
table='ciliates_outgroup_V9_above99.table'
out='ciliates_outgroup_V9_above99.mafft.aln'
log='ciliates_outgroup_V9_above99.mafft.log'

# cat $aln1 $aln2 > $input
# # cat $aln1 $fasta > $input
# echo 'Alignments concatenated'
# ruby $makemergetable $aln1 $aln2 > $table
# # makemergetable $aln1 > $table
# echo 'Table prepared'
mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --merge $table $input > $out 2> $log
echo 'Alignments merged'

#copy files back
# rm $fa
# rm $existing $add
rm $aln1 $aln2
cp * $data_dir
