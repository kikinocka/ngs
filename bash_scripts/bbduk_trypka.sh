#!/bin/bash

read_dir='/home/kika/diplonema/reads/merged_qtrimmed_vstrict/'
in1=$read_dir'YPF1604_adapter_trimmed_unmerged_1.fq'
in2=$read_dir'YPF1604_adapter_trimmed_unmerged_2.fq'
out1=$read_dir'YPF1604_unmerged_fully_trimmed_1.fq'
out2=$read_dir'YPF1604_unmerged_fully_trimmed_2.fq'
/home/nenarokova/tools/bbmap/bbduk.sh in1=$in1 in2=$in2 out1=$out1 out2=$out2 qtrim=r trimq=20 overwrite=true t=30
