#!/bin/sh
#PBS -N orthofinder
#PBS -l select=1:ncpus=20:mem=15gb:scratch_local=5gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add orthofinder-2.0.0

data='/storage/brno3-cerit/home/kika/archamoebae/'

#copy files to scratch
cp $data'prot_assemblies_filtration-20220127/'*_renamed.faa $SCRATCHDIR
cp $data'prot_assemblies_filtration-20220127/AmoebaDB-53_EhistolyticaHM1IMSS_AnnotatedProteins.faa' $SCRATCHDIR
cp $data'prot_assemblies_filtration-20220127/mei.trinity.NRfilt.faa' $SCRATCHDIR
cp $data'prot_assemblies_filtration-20220127/Masba_prot_LATEST.faa' $SCRATCHDIR
cp $data'prot_assemblies_filtration-20220127/pelomyxa_predicted_proteins_corr.faa' $SCRATCHDIR
cp $data'refs/'*.faa $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for file in *.faa; do
	echo $file
done

orthofinder -f $SCRATCHDIR

#copy files back
rm *.faa
cp -R * $data
