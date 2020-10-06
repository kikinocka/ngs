#!/bin/bash

cd /Users/kika/ownCloud/pelomyxa_schiedti/pasa-evm/
gff='pelomyxa_prediction_final_corr.gff3'
out='pelo_intron_count.txt'

if [ -f $out ]; then 
	rm $out
fi

for i in `cat $gff | grep gene | cut -f 9 | cut -c4-`; do 
	d=${#i}
	d=$(($d-1))
	i=`echo $i | cut -c1-$d`
	count=`cat $gff | grep "$i\." | grep exon | wc -l`
	echo "$i:	$(($count-1))" >> $out
	echo $i
done
