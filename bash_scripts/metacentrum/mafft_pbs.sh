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
# module add mafft-7.453
module add mafft-7.487 

data_dir='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/euglenozoa/'

#copy files to scratch
cp $data_dir'Euglenozoa_alignment.aln' $SCRATCHDIR
cp $data_dir'outgroup_nogaps.fa' $SCRATCHDIR

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
aln1='Euglenozoa_alignment.aln'
fasta='outgroup_nogaps.fa'
input='euglenozoa_outgroup.in'
table='euglenozoa_outgroup.table'
out='euglenozoa_outgroup.mafft.aln'
log='euglenozoa_outgroup.mafft.log'

cat $aln1 $fasta > $input
echo 'Alignments concatenated'
ruby $maketable $aln1 > $table
echo 'Table prepared'
mafft --thread 7 --localpair --maxiterate 1000 --merge $table $in > $out 2> $log
echo 'Alignments merged'


#copy files back
# rm $fa
# rm $existing $add
rm $aln1 $fasta
cp * $data_dir
