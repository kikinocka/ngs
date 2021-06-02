#!/bin/bash
#PBS -N otu_table
#PBS -l select=1:ncpus=10:mem=15gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

data='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/'

#copy files to scratch
cp $data'global_dereplicated_1f.stats' $SCRATCHDIR
cp $data'global_dereplicated_1f.swarms' $SCRATCHDIR
cp $data'amplicon_table.out' $SCRATCHDIR
cp $data'stampa_global_dereplicated_1f_representatives/global_dereplicated_1f_representatives.results' $SCRATCHDIR
cp $data'stampa_global_dereplicated_1f_representatives/global_dereplicated_1f_representatives.uchime' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

STATS='global_dereplicated_1f.stats'
SWARMS='global_dereplicated_1f.swarms'
AMPLICON_TABLE='amplicon_table.out'
TAXONOMY='global_dereplicated_1f_representatives.results'
CHIMERA='global_dereplicated_1f_representatives.uchime'
OTU_TABLE='otu_table.out'

# Header
echo -e "OTU\t$(head -n 1 "${AMPLICON_TABLE}")\tchimera\tidentity\ttaxonomy\treferences" > "${OTU_TABLE}"

# Compute "per sample abundance" for each OTU
awk -v SWARM="${SWARMS}" \
    -v TABLE="${AMPLICON_TABLE}" \
    -v TAXA="${TAXONOMY}" \
    -v CHIMERA="${CHIMERA}" \
    'BEGIN {FS = " "
            while ((getline < SWARM) > 0) {
                swarms[$1] = $0
            }
            close(SWARM)
            FS = "\t"
            while ((getline < TABLE) > 0) {
                table[$1] = $0
            }
            close(TABLE)
            while ((getline < CHIMERA) > 0) {
                split($2, a, ";size=")
                chimera[a[1]] = $18
            }
            close(CHIMERA)
            while ((getline < TAXA) > 0) {
                taxa[$1] = $3"\t"$4"\t"$5
            }
            close(TAXA)
           }

     {# Parse the stat file (OTUs sorted by decreasing abundance)
      seed = $3 "_" $4
      n = split(swarms[seed], OTU, "[ _]")
      for (i = 1; i < n; i = i + 2) {
          s = split(table[OTU[i]], abundances, "\t")
          for (j = 1; j < s; j++) {
              samples[j] += abundances[j+1]
          }
      }
      printf "%s\t%s", NR, $3
      for (j = 1; j < s; j++) {
          printf "\t%s", samples[j]
      }
     printf "\t%s\t%s\n", chimera[$3], taxa[$3]
     delete samples
     }' <(sort -k2,2nr -k1,1nr "${STATS}") >> "${OTU_TABLE}"

bzip2 -9fk "${OTU_TABLE}" &


#copy files back
cp ${OTU_TABLE}'.bz2' $data
