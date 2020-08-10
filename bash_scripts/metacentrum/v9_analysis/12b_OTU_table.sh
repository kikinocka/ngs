#!/bin/bash
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

#STATS="sediment_v9_17_samples_1f.stats"
#SWARMS="sediment_v9_17_samples_1f.swarms"
#AMPLICON_TABLE="sediment_v9_17_samples.amplicon.table"
#TAXONOMY="sediment_v9_17_samples_1f_representatives.results"
#CHIMERA="sediment_v9_17_samples_1f_representatives.uchime"
#OTU_TABLE="sediment_v9_17_samples.OTU.table"

STATS=$1
SWARMS=$2
AMPLICON_TABLE=$3
TAXONOMY=$4
CHIMERA=$5
OTU_TABLE=$6

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

echo "bzip2 -9fk "${OTU_TABLE}" &"

