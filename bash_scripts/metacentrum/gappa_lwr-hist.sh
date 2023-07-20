#!/bin/sh
#PBS -N gappa_lwr-hist
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
	prefix=${file%.jplace}.lwr-hist
	log=${file%.jplace}.lwr-hist.log

	$gappa examine lwr-histogram --jplace-path $file --file-prefix $prefix --log-file $log --num-lwrs 3 --threads $PBS_NUM_PPN
		
done

#copy files back
rm *.jplace
cp -R * $data
