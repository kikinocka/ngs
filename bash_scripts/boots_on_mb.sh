#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

# cd '/Users/kika/ownCloud/archamoebae/trees/D-LDH/ver4/combined/'
cd '/Users/kika/ownCloud/membrane-trafficking/trees/RABs/endocytic/ver4/combined/'
# cd '/Users/kika/ownCloud/anaeramoeba/trees/TBCs/ver6/combined/'

tree=$path'endocytic.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.endocytic.CD'
out=$path'endocytic.CD.trimal_gt-0.8.nex.mb+raxml.tre'

$placer $tree $bootstrap $out
