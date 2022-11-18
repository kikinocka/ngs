#!/bin/bash

score='/Users/kika/scripts/py_scripts/targeting-scores_mito.py'
localization='/Users/kika/scripts/py_scripts/targeting-merger_mito.py'

data='/Users/kika/ownCloud/archamoebae/targeting/rho-miro/'
prefix='amoebae'

python3 $localization -p $prefix -d $data
python3 $score -p $prefix -d $data
