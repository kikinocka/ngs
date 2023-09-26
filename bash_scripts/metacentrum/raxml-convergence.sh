#!/bin/sh
#PBS -N raxml-conv
#PBS -l select=1:ncpus=10:mem=1gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module add raxml/8.2.12-gcc-10.2.1-nu7c3k5

data='/storage/brno3-cerit/home/kika/archamoebae/raxml/ver4'

#copy files to scratch
cp $data'/'RAxML_bootstrap.* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for bs in RAxML_bootstrap.*; do
	echo $aln

	out=$bs'.conv.txt'
	raxmlHPC-PTHREADS -m PROTGAMMALG4XF -p 12345 -z $bs -I autoMRE_IGN -n $out -T $PBS_NUM_PPN
done

#copy files back
rm RAxML_bootstrap.*
cp -R * $data
