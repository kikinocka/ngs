#!/bin/bash

## Usage
function usage () {
    echo "Usage:"
    echo "$(basename ${0}) /path/to/target/file.fasta reference_dataset"
    echo "    (reference_dataset can be SSU_V4, SSU_V9)"
}


## Variables
SCRIPT_NAME="stampa.sh"
VSEARCH="vsearch"
SSU_V4="/storage/brno3-cerit/home/kika/pr2db/4.12.0/pr2_version_4.12.0_18S_taxo_CCAGCASCYGCGGTAATTCC_TYRATCAAGAACGAAAGT.fas"
# SSU_V9="/storage/brno3-cerit/home/kika/pr2db/4.13.0/pr2_version_4.13.0_18S_TTGTACACACCGCCC_GTAGGTGAACCTGCNGAAGG.fas"
SSU_V9="/storage/brno3-cerit/home/kika/databases/V9_DeepSea.fas"
OUTPUT_PREFIX="fasta."
INPUT_FILE=$(readlink -f "${1}")  # Works if $1 is a symbolic link
PATH_TO_FILE=$(readlink -f $(dirname "${1}"))
TARGET="${2}"
INPUT_FILE_BASENAME=${INPUT_FILE##*/}
INPUT_FILE_BASENAME=${INPUT_FILE_BASENAME%.*}
STAMPA_FOLDER="stampa_${INPUT_FILE_BASENAME}"
NULL="/dev/null"

## Check arguments
if [[ -z "${INPUT_FILE}" ]] ; then
        echo -e "You must specify a fasta file - *1f_representatives.fas\n" 1>&2
        usage
        exit 1
fi
if [[ -z "${TARGET}" ]] ; then
        echo -e "You must specify a target database (SSU_V4 or SSU_V9).\n" 1>&2
        usage
        exit 1
fi


## Select database
case "${TARGET}" in
    "SSU_V9")
        DATABASE="${SSU_V9}"
        THRESHOLD="10000"
        ;;
    "SSU_V4")
        DATABASE="${SSU_V4}"
        THRESHOLD="10000"
        ;;
    *)
        echo -e "You must specify a target database (SSU_V4 or SSU_V9).\n" 1>&2
        usage
        exit 1
        ;;
esac


## Verify the uniqueness of reference sequence names
duplicates=$(grep "^>" "${DATABASE}" | cut -d " " -f 1 | sort -d | uniq -d)
if [[ "${duplicates}" ]] ; then
    echo -e "WARNING!\nThe reference database contains duplicated accession numbers\n${duplicates}\n" 1>&2
fi


## Verify the abundance annotations (expect "_")
if [[ $(head "${INPUT_FILE}" | grep ";size=") ]] ; then
    echo -e "WARNING!\nThe fasta file contains abundance annotations in usearch's style (;size=).\n" 1>&2
fi


## Go where the work is.
cd "${PATH_TO_FILE}/"


## Remove old analysis and create a work folder
if  [[ -d "${STAMPA_FOLDER}" ]] ; then
    echo "Removing old stampa analysis."
    rm -rf "${STAMPA_FOLDER}/"
fi
mkdir "${STAMPA_FOLDER}"
cd "${STAMPA_FOLDER}/"

# We won't be splitting the file into chunks, due to our server setup, but we still need
# to do some of the downstream analysis..

## Where are we?
PWD=$(pwd)

# this part sends to a queue all of the chunks and splits them across multiple servers
# we don't have that set up in our servers
# so we will just run the whole file in one go

# I have move the stampa_vsearch process in to this script...

# copy not symlink *_1f_representatives.fas to STAMP DIR
# as we are about to modify it...
FILE=$(basename ${INPUT_FILE})
cp ${INPUT_FILE} ${PWD}/${FILE}

# remove the abundance information - not needed for this step
sed -i '/^>/ s/_/;size=/' ${PWD}/${FILE}
sed -i '/^>/ s/;$//' ${PWD}/${FILE}

QUERIES="${PWD}/${FILE}"
ASSIGNMENTS="${QUERIES/.fas/.hits}"
IDENTITY="0.5"
MAXREJECTS=32
THREADS=15

# Dereplicate (vsearch)
"${VSEARCH}" --usearch_global "${QUERIES}" \
    --threads "${THREADS}" \
    --dbmask none \
    --qmask none \
    --rowlen 0 \
    --notrunclabels \
    --userfields query+id1+target \
    --maxaccepts 0 \
    --maxrejects "${MAXREJECTS}" \
    --top_hits_only \
    --output_no_hits \
    --db "${DATABASE}" \
    --id "${IDENTITY}" \
    --iddef 1 \
    --userout "${ASSIGNMENTS}" > "${NULL}" 2> "${NULL}"

#err.log 2> stdout.log 
#"${NULL}" 2> "${NULL}"

# Since we are not splitting the file in to chunks then we don't need to do a merge BUT
# the script does do some parsing and sorting so we do need to do that...

#echo "DIR: ${PWD}"

python2 "../9c_stampa_merge.py" "${PWD}"

RESULTS="${ASSIGNMENTS/.hits/.results}"

sort --key=2,2nr --key=1,1d --output=${RESULTS} ${RESULTS}

exit 0
