#!/bin/bash

SWARM="swarm"
FASTA_FILE=$(readlink -f "${1}")
echo '******'
echo $FASTA_FILE
echo '******'
THREADS=15
echo '******'
echo $THREADS
echo '******'
RESOLUTION="1"
OUTPUT_SWARMS="global_dereplicated_1f.swarms"
echo '******'
echo $OUTPUT_SWARMS
echo '******'
OUTPUT_STATS="global_dereplicated_1f.stats"
echo '******'
echo $OUTPUT_STATS
echo '******'
OUTPUT_REPRESENTATIVES="global_dereplicated_1f_representatives.fas"
echo '******'
echo $OUTPUT_REPRESENTATIVES
echo '******'

## Verify the abundance annotation style
if [[ ${FASTA_FILE##*.} == "bz2" ]] ; then
    SAMPLE=$(bzcat "${FASTA_FILE}" | head -n 1 | grep -o ";size=\|_")
else
    SAMPLE=$(head -n 1 "${FASTA_FILE}" | grep -o ";size=\|_")
fi
case "${SAMPLE}" in
    ";size=")
        ANNOTATION_OPTION="-z"
        ;;
    "_")
        ANNOTATION_OPTION=""
        ;;
    *)
        echo "Unidentified abundance annotation (\"_\" or \";size=\")." 1>&2
        exit 1
        ;;
esac


if [[ ${FASTA_FILE##*.} == "bz2" ]] ; then
    if [[ ${ANNOTATION_OPTION} ]] ; then
        "${SWARM}" -d "${RESOLUTION}" -f \
            -w "${OUTPUT_REPRESENTATIVES}" \
            -t "${THREADS}" "${ANNOTATION_OPTION}" \
            -s "${OUTPUT_STATS}" <(bzcat "${FASTA_FILE}") > "${OUTPUT_SWARMS}"
    else
        "${SWARM}" -d "${RESOLUTION}" -f \
            -w "${OUTPUT_REPRESENTATIVES}" \
            -t "${THREADS}" \
            -s "${OUTPUT_STATS}" <(bzcat "${FASTA_FILE}") > "${OUTPUT_SWARMS}"
    fi
else
    if [[ ${ANNOTATION_OPTION} ]] ; then
        "${SWARM}" -d "${RESOLUTION}" -f \
            -w "${OUTPUT_REPRESENTATIVES}" \
            -t "${THREADS}" "${ANNOTATION_OPTION}" \
            -s "${OUTPUT_STATS}" < "${FASTA_FILE}" > "${OUTPUT_SWARMS}"
    else
        "${SWARM}" -d "${RESOLUTION}" -f \
            -w "${OUTPUT_REPRESENTATIVES}" \
            -t "${THREADS}" \
            -s "${OUTPUT_STATS}" < "${FASTA_FILE}" > "${OUTPUT_SWARMS}"
    fi
fi

exit 0
