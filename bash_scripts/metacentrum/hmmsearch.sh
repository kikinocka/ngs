#!/bin/bash
#PBS -N hmmsearch
#PBS -l select=1:ncpus=20:mem=10gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add hmmer

hmm_dir='/storage/brno12-cerit/home/kika/kinetoplastids/angomonas/EAPs'
db_dir='/storage/brno12-cerit/home/kika/databases/all'

#copy files to scratch
cp $hmms_dir'/'*.hmm $SCRATCHDIR
cp $db_dir'/'*.faa $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

mkdir hmms databases
mv *hmm hmms
mv *faa databases

eval=1e-10
for profile in hmms/*.hmm ; do
	echo $profile
	for db in databases/*.faa ; do
		echo $db
		orgn=`echo ${db%.faa} | cut -d / -f 2`
		prot=`echo ${profile%.hmm} | cut -d / -f 2`
		output=$orgn'.'$prot'.hmmsearch.tsv'
		echo $output
		hmmsearch --tblout $output --cpu $PBS_NUM_PPN -E $eval $profile $db
		cd hmms/
		# sleep 5
		echo
	done
done

#copy files back
rm -r hmms databases
cp *tsv $hmm_dir
