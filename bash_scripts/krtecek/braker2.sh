cd '/home/users/kika/blastocystis/ASM2924127v1/'

genome='GCA_029241275.1_ASM2924127v1_genomic.fna'
prot='/home/users/kika/blastocystis/Stramenopiles.fa'
name='blastocystis_CHMP1T30'

singularity exec /home2/BW2026/braker3.sif braker.pl \
	--genome=$genome \
	--prot_seq=$prot \
	--species=$name \
	--workingdir=braker \
	--threads 20 \
	--gff3
