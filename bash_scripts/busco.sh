#!/bin/sh
cd /home/tomas/GIT/busco
#python BUSCO.py --cpu 16 --species leishmania_tarentolae --long -i Paratrypanosoma_PE_MP_Newbler_500bp_up_v1.fa -o BUSCO_CUL13_genome_2euk_set -l /home/tomas/GIT/busco/eukaryota_odb9 -m geno
#python BUSCO.py --cpu 16 --species leishmania_tarentolae --long -i Lpyr_ass_v6.fa -o BUSCO_H10_genome_2euk_set -l /home/tomas/GIT/busco/eukaryota_odb9 -m geno
#python BUSCO.py --cpu 16 --species leishmania_tarentolae --long -i Paratrypanosoma_all_annotated_AA_final_modif.fasta -o BUSCO_CUL13_proteome_euk_set -l /home/tomas/GIT/busco/eukaryota_odb9 -m prot
#python BUSCO.py --cpu 16 --species leishmania_tarentolae --long -i Lpyr_ass_v6_prot.fa -o BUSCO_H10_proteome_euk_set -l /home/tomas/GIT/busco/eukaryota_odb9 -m prot
python BUSCO.py --cpu 16 --species leishmania_tarentolae --long -i /home/kika/blastocrithidia/transcriptome/p57_translated_RNA_Trinity.fasta -o BUSCO_p57_translRNA_euk_set -l /home/tomas/GIT/busco/eukaryota_odb9 -m prot -f
