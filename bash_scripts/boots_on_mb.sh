#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/archamoebae/trees/hydA/ver6/combined/'
# cd '/Users/kika/ownCloud/membrane-trafficking/trees/RABs/endocytic/ver4/combined/'
# cd '/Users/kika/ownCloud/anaeramoeba/trees/TBCs/ver6/combined/'

tree=$path'hydA.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.hydA'
out=$path'hydA.trimal_gt-0.8.nex.mb+raxml.tre'

$placer $tree $bootstrap $out
