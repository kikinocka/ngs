#!/bin/bash
#PBS -N tRNAscan
#PBS -l select=1:ncpus=10:mem=1gb:scratch_local=5gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

tRNAscan='/storage/brno3-cerit/home/kika/miniconda3/bin/tRNAscan-SE'
data_dir='/storage/brno3-cerit/home/kika/p57/mtDNA'

#copy files to scratch
cp $data_dir'/'*.fa $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for genome in *.fa ; do
	echo $genome

	table=${genome%.fa}.tRNAscan_table.tsv
	seq=${genome%.fa}.tRNAscan.fa
	structures=${genome%.fa}.tRNAscan_structures.txt

	$tRNAscan --thread $PBS_NUM_PPN -O -o $table -a $seq -f $structures ${genome}
done


#copy files back
rm *.fna
cp * $data_dir
