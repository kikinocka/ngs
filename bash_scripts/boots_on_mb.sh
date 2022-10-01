#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

# cd '/Users/kika/ownCloud/archamoebae/trees/PFO/ver4/combined/'
cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_COPII/trees/seh1/combined/'
# cd '/Users/kika/ownCloud/anaeramoeba/trees/TBCs/ver6/combined/'

tree=$path'seh1.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.seh1.CD'
out=$path'seh1.CD.trimal_gt-0.8.nex.mb+raxml.tre'

$placer $tree $bootstrap $out
