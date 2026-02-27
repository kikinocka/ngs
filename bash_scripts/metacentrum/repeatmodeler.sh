#!/bin/bash
#PBS -N RepeatModeler
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=20gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

genome_dir='/storage/brno12-cerit/home/kika/paratrimastix/'

#copy files to scratch
cp $genome_dir'PaPyr_JAPMOS01.fna' $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

genome='PaPyr_JAPMOS01.fna'
name=${genome%.fna}

#Generate the RepeatModeler sequence database
singularity run -B $SCRATCHDIR /cvmfs/singularity.metacentrum.cz/TE-Tools/TE-tools-1.4.sif BuildDatabase \
	-name $name $genome
#Run RepeatModeler
singularity run -B $SCRATCHDIR /cvmfs/singularity.metacentrum.cz/TE-Tools/TE-tools-1.4.sif RepeatModeler \
	-database $name -pa $PBS_NUM_PPN -LTRStruct
#How many consensus sequences have been predicted?
grep -c '>' $name'-families.fa'
#How is the distribution of repeats by types?
grep '>' $name'-families.fa' | sed -r 's/.+#//' | sed -r 's/\s+.+//' | sort | uniq -c > $name'.repeat_types.txt'
#Run RepeatMasker - USE SOFT MASKING (-xsmall)
singularity run -B $SCRATCHDIR /cvmfs/singularity.metacentrum.cz/TE-Tools/TE-tools-1.4.sif RepeatMasker \
	-lib $name'-families.fa' -xsmall -pa $PBS_NUM_PPN $genome
#Transform the .out file into a .gff file
perl -ne 'BEGIN{ $l=0; print "##gff-version 3\n"} chomp($_); $l++; if ($l > 3) { $_ =~ s/^\s+//; @a=split(/\s+/, $_); $strand = $a[8]; if ($strand eq "C") { $strand = "-"; } @feats=("ID=RepeatMaskerHitId".$a[14], "Name=".$a[9], "Note=Family:".$a[9]."|Superfamily:".$a[10]."|ConsensusPercSNP:".$a[1]."|ConsensusPercDel:". $a[2]."|ConsensusPercIns:".$a[3]."|ConsensusHit:\"".$a[9]." ".$a[11]." ".$a[12]." ".$a[13]."\""); $featp=join(";", @feats); print "$a[4]\tRepeatMasker\tmatch\t$a[5]\t$a[6]\t$a[0]\t$strand\t$featp\n"} ' $genome'.out' > $name'.repeats_by_repeatmasker.gff'
#Count the different types of repeats
perl -ne 'BEGIN{ $l=0; %rep_cnt=(); %rep_siz=(); } chomp($_); $l++; if ($l > 3) { $_ =~ s/^\s+//; @a=split(/\s+/, $_); $len=$a[6]-$a[5]; $repid=$a[10]."\t".$a[9]; if (exists $rep_cnt{$repid}) { $rep_cnt{$repid}++; $rep_siz{$repid} += $len; } else { $rep_cnt{$repid} = 1; $rep_siz{$repid} = $len; } } END{ print "#Superfamily\tFamily\tCount\tSize (bp)\n"; foreach $t (sort keys %rep_cnt) { print "$t\t$rep_cnt{$t} \t$rep_siz{$t}\n"; } }' $genome'.out' > $name'.repeats_by_repeatmasker.stats.txt'


#copy files back
rm $genome
cp -r * $genome_dir'repeatmodeler_JAPM/'
