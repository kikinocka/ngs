#!/bin/bash
#name prefetch_wrapper

HOMEDIR='/mnt/mokosz/home/kika/workdir'
ALNDIR='/mnt/mokosz/home/kika/workdir'

#cd $HOMEDIR

while read -r sample
do
	if [ ! -e $ALNDIR/${sample/fa/muscle.aln} ]; then
		touch $ALNDIR/${sample/fa/muscle.aln}
	    muscle -super5 $HOMEDIR/$sample -output $ALNDIR/${sample/fa/muscle.aln} -threads 15
    fi
done < $HOMEDIR'/blasto_OGs.txt' #last item must end with a newline!

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py muscle5 done

