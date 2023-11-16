#!/bin/bash

HOMEDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_trimal_automated1'

while read -r sample
do
	scp $sample kika@skirit.metacentrum.cz:/storage/brno3-cerit/home/kika/metamonads/fasttree/
    fi
done < $HOMEDIR'/at1.txt' #last item must end with a newline!

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py scp done

