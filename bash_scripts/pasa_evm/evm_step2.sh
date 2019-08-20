#!/bin/bash

evm_path='/opt/evm/EVM_r2012-06-25/EvmUtils/'
genome='/home/kika/pelomyxa_schiedti/genome_assembly/pelomyxa_final_genome.fa'
transdecoder='/home/kika/pelomyxa_schiedti/pasa-evm/pasa1/pelomyxa_pasa_mysql.assemblies.fasta.transdecoder.genome.gff3'
pasa_gff='/home/kika/pelomyxa_schiedti/pasa-evm/pasa1/pelomyxa_pasa_mysql.pasa_assemblies.gff3'

#converting augustus gff 
augustus='/home/kika/pelomyxa_schiedti/augustus/pelo_augustus_100_hints.gff'
prediction='pelo_augustus_100_hints.gff3'
$evm_path'misc/augustus_to_GFF3.pl' $augustus > $prediction

#merging the prediction
merged='all_merged.gff3'
cat $prediction $transdecoder > $merged

#generate partitions
partitions='partitions_list.out'
$evm_path'partition_EVM_inputs.pl' --genome $genome \
	--gene_predictions $merged --transcript_alignments $pasa_gff \
	--segmentSize 1000000 --overlapSize 10000 --partition_listing $partitions

#generate commands
weights='/home/kika/pelomyxa_schiedti/pasa-evm/evm1/weights.txt'
output='evm.out'
commands='commands.list'
$evm_path'write_EVM_commands.pl' --genome $genome --weights $weights \
	--gene_predictions $merged --transcript_alignments $pasa_gff \
	--output_file_name $output --partitions $partitions > $commands

#run commands
$evm_path'execute_EVM_commands.pl' $commands | tee run.log

echo
echo
echo '*** Created EVM output file: evm.out ***'
$evm_path'recombine_EVM_partial_outputs.pl' --partitions $partitions --output_file_name $output
$evm_path'convert_EVM_outputs_to_GFF3.pl' --partitions $partitions --output $output --genome $genome

final_evm='evm.all.gff3'
find . -regex '.*evm.out.gff3' -exec cat {} \; > $final_evm

echo
echo
echo '*** Converted EVM output to GFF3 format***'

echo
echo 'Done.'
