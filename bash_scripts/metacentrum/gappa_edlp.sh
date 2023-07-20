#!/bin/sh
#PBS -N gappa_edlp
#PBS -l select=1:ncpus=20:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

gappa='/storage/brno3-cerit/home/kika/miniconda3/bin/gappa'
data='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/heterolobosea/placement'

#copy files to scratch
cp $data'/'*.jplace $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for file in *.jplace ; do
	echo $file
	prefix=${file%.jplace}
	log=${file%.jplace}.edlp.log

	$gappa examine edpl --jplace-path $file --file-prefix $prefix --log-file $log --threads $PBS_NUM_PPN
		
done

#copy files back
rm *.jplace
cp -R * $data
