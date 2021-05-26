#!/bin/bash

scripts='/Users/kika/programs/Binning/'
wrapper=$scripts'esomWrapper.pl'

data='/Users/kika/ownCloud/oil_sands/metagenome/'
out='/Users/kika/ownCloud/oil_sands/metagenome/esom'
ext=fa

perl $wrapper -path $data -ext $ext -dir $out -min 250 -scripts $scripts
