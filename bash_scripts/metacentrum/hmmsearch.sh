#!/bin/bash
#PBS -N hmmsearch
#PBS -l select=1:ncpus=20:mem=10gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add hmmer

hmms='/storage/brno12-cerit/home/kika/kinetoplastids/angomonas/EAPs'
db='/storage/brno12-cerit/home/kika/databases/all'

#copy files to scratch
cp $hmms'/'*.hmm $SCRATCHDIR
cp $db'/'*.faa $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

mkdir hmms databases
mv *hmm hmms
mv *faa databases

for profile in hmms/*.hmm ; do
	echo $profile
	for db in databases/*.faa ; do
		echo $db
		orgn=`echo ${db%.faa} | cut -d / -f 2`
		prot=${profile%.hmm} | cut -d / -f 2
		output=$orgn'.'$prot'.hmmsearch.tsv'
		echo $output
		hmmsearch --tblout $output --cpu $threads -E $eval $profile $db
		cd hmms/
		# sleep 5
		echo
	done
done

#copy files back
rm *.hmm 
cp *tsv $data_dir
