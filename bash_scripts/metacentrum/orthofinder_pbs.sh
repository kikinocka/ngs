#!/bin/sh
#PBS -N orthofinder
#PBS -l select=1:ncpus=20:mem=15gb:scratch_local=5gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add orthofinder-2.0.0

data='/storage/brno3-cerit/home/kika/archamoebae/'

#copy files to scratch
cp $data'prot_assemblies_filtration-20220127/'*.fa $SCRATCHDIR
cp $data'refs/'*.faa $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for file in *.faa; do
	echo $file
done

orthofinder -f $SCRATCHDIR

#copy files back
rm *.faa
cp -R * $data
