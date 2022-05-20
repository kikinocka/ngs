#!/bin/bash

cd '/Users/kika/ownCloud/SL_Euglenozoa/V9/above14/'

TABLE="v9.no_chimera.above14.no_prokaryota.tsv"
MY_FAVORITE_TAXA="Obazoa"
LEAST_FAVORITE="Metazoa"
# FILTERED="${TABLE/.tsv/.$MY_FAVORITE_TAXA.tsv}"
FILTERED="${TABLE/.tsv/.non-$LEAST_FAVORITE$MY_FAVORITE_TAXA.tsv}"

head -n 1 "${TABLE}" > "${FILTERED}"
# grep "${MY_FAVORITE_TAXA}" "${TABLE}" >> "${FILTERED}"
grep "${MY_FAVORITE_TAXA}" "${TABLE}" | grep -v $LEAST_FAVORITE >> "${FILTERED}"
# | \
# awk '$7 == "N" && $9 <= 0.0002 && ($2 >= 3 || $8 >= 2)' >> "${FILTERED}"
