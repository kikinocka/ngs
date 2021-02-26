#!/bin/bash
#PBS -N tblastn
#PBS -l select=1:ncpus=15:mem=50gb:scratch_local=50gb
#PBS -l walltime=168:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno3-cerit/home/kika/oil_sands/18S'

#copy files to scratch
cp $datadir'/'*.fa $SCRATCHDIR

program=blastn
db='/storage/projects/BlastDB/nt'
outfmt=5
word=11


#run on scratch
cd $SCRATCHDIR

for query in *.fa; do
	echo $query
	out=${query%.fa}'.blastn.xml'
	$program -query $query -db $db -out $out -outfmt $outfmt -word_size $word -num_threads $PBS_NUM_PPN
	echo ***BLAST done***
done

#copy files back
rm *fa
cp * $datadir
