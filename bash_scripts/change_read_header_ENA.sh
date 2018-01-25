#!/bin/bash

# FORWARD:
# sed -i -E 's,(SRR.*)([[:space:]]),\1/1\2,g' /media/4TB1/blastocrithidia/kika_workdir/ena_reads/SRR4017973_1.fastq
# sed -i -E 's,(SRR.*)([[:space:]]),\1/1\2,g' /media/4TB1/blastocrithidia/kika_workdir/ena_reads/SRR4017993_1.fastq

# REVERSE:
sed -i -E 's,(SRR.*)([[:space:]]),\1/2\2,g' /media/4TB1/blastocrithidia/kika_workdir/ena_reads/SRR4017973_2.fastq
# sed -i -E 's,(SRR.*)([[:space:]]),\1/2\2,g' /media/4TB1/blastocrithidia/kika_workdir/ena_reads/SRR4017993_2.fastq