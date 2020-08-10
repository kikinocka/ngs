#!/bin/bash
#PBS -N amplicons
#PBS -l select=1:ncpus=1:mem=5gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE


data='/storage/brno3-cerit/home/kika/sl_euglenozoa/'
script_dir='/storage/brno2/home/kika/scripts/kika/bash_scripts/metacentrum/v9_analysis/'

#copy files to scratch
cp $script_dir'12b_OTU_table.sh' $SCRATCHDIR
cp $data'global_dereplicated_1f.stats' $SCRATCHDIR
cp $data'global_dereplicated_1f.swarms' $SCRATCHDIR
cp $data'amplicon_table.out' @SCRATCHDIR
cp $data'stampa_global_dereplicated_1f_representatives/global_dereplicated_1f_representatives.results' $SCRATCHDIR
cp $data'stampa_global_dereplicated_1f_representatives/global_dereplicated_1f_representatives.uchime' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

#if [ $# != 6 ]; then
#    echo "You need to supply a set of input and output filenames.";
#    echo "STATS  = X_1f.stats"
#    echo "SWARMS = X_1f.swarms"
#    echo "AMPLICON_TABLE = X.table"
#    echo "TAXONOMY = X_1f_representatives.results"
#    echo "CHIMERA = X_1f_representatives.uchime"
#    echo "OTU_TABLE = your_otu_table_name.table"
#    exit 1;
#fi

SCRIPT='12b_OTU_table.sh'
STATS='global_dereplicated_1f.stats'
SWARMS='global_dereplicated_1f.swarms'
AMPLICON_TABLE='amplicon_table.out'
TAXONOMY='global_dereplicated_1f_representatives.results'
CHIMERA='global_dereplicated_1f_representatives.uchime'
OTU_TABLE='global_dereplicated_1f.OTU_table.out'

bash ${SCRIPT} ${STATS} ${SWARMS} ${AMPLICON_TABLE} ${TAXONOMY} ${CHIMERA} ${OTU_TABLE}

#copy files back
cp ${OTU_TABLE} $data
