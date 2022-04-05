#! /bin/bash

INPUT="${1}"
CUTADAPT="cutadapt"
VSEARCH="vsearch"
HASHING="hashing.py"
REGION="${2}"

## Select database
case "${REGION}" in
    "V4")
        PRIMER_F="CCAGCASCYGCGGTAATTCC"
        PRIMER_R="TYRATCAAGAACGAAAGT"
        ANTI_PRIMER_F="GGAATTACCGCRGSTGCTGG"
        ANTI_PRIMER_R="ACTTTCGTTCTTGATYRA"
        ;;
    "V9")
        PRIMER_F="TTGTACACACCGCCC"
        PRIMER_R="GTAGGTGAACCTGCNGAAGG"
        ANTI_PRIMER_F="GGGCGGTGTGTACAA"
        ANTI_PRIMER_R="CCTTCNGCAGGTTCACCTAC"
        ;;
    *)
        echo "You must specify a set of primers." 1>&2
        exit 1
        ;;
esac

# Define temporary files and output files
TMP_FORWARD=$(mktemp)
TMP_ANTI_FORWARD=$(mktemp)
TMP_REVERSE=$(mktemp)
TMP_ANTI_REVERSE=$(mktemp)
TMP_FASTA=$(mktemp)
# TMP_FASTA_DEREPLICATED=$(mktemp)
FINAL_FASTA=${INPUT/.fastq/.fasta}
LOG=${INPUT/.fastq/.log}

# Get reads containing forward primer
${CUTADAPT} --discard-untrimmed -g PRIMER_F=${PRIMER_F} -o ${TMP_FORWARD} ${INPUT} > ${LOG}

# Get reads containing reverse primer
${CUTADAPT} --discard-untrimmed -a PRIMER_R=${PRIMER_R} -o ${TMP_REVERSE} ${TMP_FORWARD} >> ${LOG}

# Get reads containing anti-reverse primer (in 5' position)
${CUTADAPT} --discard-untrimmed -g ANTI_PRIMER_R=${ANTI_PRIMER_R} -o ${TMP_ANTI_FORWARD} ${INPUT} >> ${LOG}

# Get reads containing anti-forward primer (in 3' position)
${CUTADAPT} --discard-untrimmed -a ANTI_PRIMER_F=${ANTI_PRIMER_F} -o ${TMP_ANTI_REVERSE} ${TMP_ANTI_FORWARD} >> ${LOG}

# Convert fastq to fasta (reverse-complement the second file)
(awk '(NR - 2) % 4 == 0' ${TMP_REVERSE}
 awk '(NR - 2) % 4 == 0' ${TMP_ANTI_REVERSE} | \
     tr "acgturykmbdhvACGTURYKMBDHV" "tgcaayrmkvhdbTGCAAYRMKVHDB" | rev) | \
     grep -v [^ACGTacgt] | awk '{printf ">a%d\n%s\n", NR, $1}' > ${TMP_FASTA}

rm -f ${TMP_FORWARD} ${TMP_ANTI_FORWARD} ${TMP_REVERSE} ${TMP_ANTI_REVERSE}

# Dereplicate (vsearch)
"${VSEARCH}" --threads 1 \
    --derep_fulllength ${TMP_FASTA} \
    --sizeout \
    --relabel_md5 \
    --fasta_width 0 \
    --output ${FINAL_FASTA}
    # --output ${TMP_FASTA_DEREPLICATED}
    
# # Compute hash values
# python ${HASHING} ${TMP_FASTA_DEREPLICATED} > ${FINAL_FASTA}

# Get some basic statistics
awk -F "=" 'BEGIN {OFS = "\t"}
            /^>/ {c += 1 ; s += $2}
            END {
                printf "\n%s\n%s\t%d\n%s\t%d\n", "Basic stats:", "uniques", c, "reads", s
            }' ${FINAL_FASTA} >> ${LOG}

rm -f ${TMP_FASTA} #${TMP_FASTA_DEREPLICATED}

exit 0
