#!/bin/bash

VSEARCH="vsearch"
QUERIES=$(readlink -f "${1}")
CHIMERAS=${QUERIES/.fas/_chimeras.fas}
UCHIME=${QUERIES/.fas/.uchime}
NULL="/dev/null"


## Verify the abundance annotations (expect ";size=")
if [[ ! $(head "${QUERIES}" | grep ";size=") ]] ; then
    echo "ERROR: fasta file must contain abundance annotations in usearch's style (;size=)." 1>&2
    exit 1
fi


# Dereplicate (vsearch)
"${VSEARCH}" --uchime_denovo "${QUERIES}" \
    --fasta_width 0 \
    --chimeras "${CHIMERAS}" \
    --uchimeout "${UCHIME}"

exit 0
