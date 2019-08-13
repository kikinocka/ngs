#!/bin/bash

evm_path='/opt/evm/EVM_r2012-06-25/EvmUtils'
genome='/home/kika/pelomyxa_schiedti/genome_assembly/pelomyxa_final_genome.fa'
transdecoder='pasa1/pelomyxa_pasa_mysql.assemblies.fasta.transdecoder.genome.gff3'
pasa_genes='pasa2/pelomyxa_pasa_mysql.gene_structures_post_PASA_updates.updated.gff3'
pasa_gff='pasa1/pelomyxa_pasa_mysql.pasa_assemblies.gff3'
final_evm='evm.all.gff3'

#merging the prediction
merged='evm2/all_merged.gff3'
cat $pasa_genes $transdecoder > $merged

#generate partitions
partitions='partitions_list.out'
$evm_path/partition_EVM_inputs.pl --genome $genome \
	--gene_predictions $merged --transcript_alignments $pasa_gff \
	--segmentSize 1000000 --overlapSize 10000 --partition_listing $partitions

# generate commands
weights='/home/kika/pelomyxa_schiedti/pasa-evm/evm2/weights.txt'
output='evm.out'
commands='commands.list'
$evm_path/write_EVM_commands.pl --genome $genome --weights $weights \
	--gene_predictions $merged --transcript_alignments $pasa_gff \
	--output_file_name $output --partitions $partitions > $commands

#run commands
$evm_path/execute_EVM_commands.pl $commands | tee run.log

echo
echo
echo '*** Created EVM output file: evm.out ***'
$evm_path/recombine_EVM_partial_outputs.pl --partitions $partitions --output_file_name $output
$evm_path/convert_EVM_outputs_to_GFF3.pl --partitions $partitions --output $output --genome $genome

find . -regex '.*evm.out.gff3' -exec cat {} \; > $final_evm

echo
echo
echo '*** Converted EVM output to GFF3 format: evm.out.gff3 ***'

echo
echo 'Done.'
