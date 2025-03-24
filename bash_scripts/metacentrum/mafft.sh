#!/bin/bash
#PBS -N mafft
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load mafft

data_dir='/storage/brno12-cerit/home/kika/kinetoplastids/angomonas/EAPs/trees/ver8'

#copy files to scratch
cp $data_dir'/'*'.fa' $SCRATCHDIR
# cp $data_dir'apicomplexa.mafft.aln' $SCRATCHDIR
# cp $data_dir'V9.fa' $SCRATCHDIR
# cp $data_dir'mesozoa_outgroup_V9_above99.table' $SCRATCHDIR
# cp $data_dir'mesozoa_outgroup_V9_above99.in' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

#align de-novo
for file in *.fa ; do
	echo $file
	aln=${file%.fa}.mafft.aln
	log=${file%.fa}.mafft.log

	mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --inputorder ${file} > ${aln} 2> ${log}
	# mafft --thread $PBS_NUM_PPN --auto --inputorder ${file} > ${aln} 2> ${log}
done


# #add to aligned sequences
# existing='apicomplexa.mafft.aln'
# add='V9.fa'
# aln='apicomplexans_V9.mafft.aln'
# log='apicomplexans_V9.mafft.log'

# mafft --version 2> $log
# # mafft --add $add --thread $PBS_NUM_PPN --inputorder $existing > $aln 2> $log
# mafft --addfragments $add --thread $PBS_NUM_PPN --inputorder --keeplength $existing > $aln 2> $log


# #merge alignments and fasta files
# # maketable='/software/mafft/7.487/core/makemergetable.rb'
# aln1='euglenozoa.mafft.aln'
# # fasta='outgroup.fa'
# aln2='v9_0.mafft.aln'
# input='euglenozoa_V9_0.in'
# table='euglenozoa_V9_0.table'
# out='euglenozoa_V9_0.mafft_merge.aln'
# log='euglenozoa_V9_0.mafft_merge.log'

# cat $aln1 $aln2 > $input
# # cat $aln1 $fasta > $input
# echo 'Alignments concatenated'
# makemergetable.rb $aln1 $aln2 > $table
# # ruby $makemergetable $aln1 > $table
# echo 'Table prepared'
# # mafft --thread $PBS_NUM_PPN --localpair --maxiterate 1000 --merge $table $input > $out 2> $log
# mafft --thread $PBS_NUM_PPN --merge $table $input > $out 2> $log
# echo 'Alignments merged'

#copy files back
# rm *.fa
# rm $existing $add
# rm $aln1 $aln2
cp *mafft* $data_dir
