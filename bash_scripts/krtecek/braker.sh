cd '/home/users/kika/blastocystis/ASM2924151v1/'

genome='GCA_029241515.1_ASM2924151v1_genomic.fna'
prot='/home/users/kika/blastocystis/Stramenopiles.fa'
name='blastocystis_CHMP1T18'

singularity exec /home2/BW2026/braker3.sif braker.pl \
	--genome=$genome \
	--prot_seq=$prot \
	--species=$name \
	--workingdir=braker \
	--threads 20 \
	--gff3
