#!/bin/bash
#PBS -N amplicons
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add vsearch-1.4.4

data='/storage/brno3-cerit/home/kika/sl_euglenozoa/stampa_global_dereplicated_1f_representatives/'
script='/storage/brno2/home/kika/scripts/kika/bash_scripts/metacentrum/v9_analysis/'

#copy files to scratch
cp $data'global_dereplicated_1f_representatives.fas' $SCRATCHDIR
cp $script'11b_amplicon_contingency_table.py' $SCRATCHDIR

OUTPUT=
SCRIPT='11b_amplicon_contingency_table.py'


#compute on scratch
cd $SCRATCHDIR

# if [ $# != 1 ]; then
#     echo 'You need to supply an output filename - e.g. something.table';
#     exit 1;
# fi


ls -1 ./[1-9]*.fas | cut -d '/' -f 2 | sort -d | uniq -d

python '${SCRIPT}' ./[1-9]*.fas > ${OUTPUT} &



#copy files back
rm $fasta $SCRIPT
cp -r * $data
