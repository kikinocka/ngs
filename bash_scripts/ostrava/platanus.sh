#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N platanus
#PBS -l nodes=1:ppn=80
#PBS -l walltime=02:00:00

platanus='/home/users/kika/platanus'
work_dir='/mnt/data/kika/blastocrithidia/o_volfi/'

cd $work_dir'scaff_gap/'
read_dir='/mnt/data/kika/blastocrithidia/o_volfi/reads/'
fwd=$read_dir'CC37A_trimmed_1.fq'
rev=$read_dir'CC37A_trimmed_2.fq'
# contigs=$work_dir'spades_all_careful/contigs.fasta'
contigs='Ovol.platanus_rnd1_scaffold.l500.gapcloser.fa'
out='Ovol.platanus_rnd2'
report='Ovol.platanus_rnd2.log'

$platanus scaffold -o $out -c $contigs -IP1 $fwd $rev -t 40 2> $report

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: platanus done


# -o STR                             : prefix of output file (default out, length <= 200)
# -c FILE1 [FILE2 ...]               : contig_file (fasta format)
# -b FILE1 [FILE2 ...]               : bubble_seq_file (fasta format)
# -ip{INT} PAIR1 [PAIR2 ...]         : lib_id inward_pair_file (reads in 1 file, fasta or fastq)
# -IP{INT} FWD1 REV1 [FWD2 REV2 ...] : lib_id inward_pair_files (reads in 2 files, fasta or fastq)
# -op{INT} PAIR1 [PAIR2 ...]         : lib_id outward_pair_file (reads in 1 file, fasta or fastq)
# -OP{INT} FWD1 REV1 [FWD2 REV2 ...] : lib_id outward_pair_files (reads in 2 files, fasta or fastq)
# -n{INT} INT                        : lib_id minimum_insert_size
# -a{INT} INT                        : lib_id average_insert_size
# -d{INT} INT                        : lib_id SD_insert_size
# -e FLOAT                           : coverage depth of homozygous region (default auto)
# -s INT                             : mapping seed length (default 32)
# -v INT                             : minimum overlap length (default 32)
# -l INT                             : minimum number of link (default 3)
# -u FLOAT                           : maximum difference for bubble crush (identity, default 0.1)
# -t INT                             : number of threads (<= 1, default 1)
# -tmp DIR                           : directory for temporary files (default .)


# Outputs:
#     PREFIX_scaffold.fa
#     PREFIX_scaffoldBubble.fa
#     PREFIX_scaffoldComponent.tsv
