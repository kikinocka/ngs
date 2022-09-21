#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

# cd '/Users/kika/ownCloud/archamoebae/trees/PFO/ver4/combined/'
cd '/Users/kika/ownCloud/membrane-trafficking/trees/ARFs/sar1-sarB/ver2/combined/'
# cd '/Users/kika/ownCloud/anaeramoeba/trees/TBCs/ver6/combined/'

tree=$path'sar1-sarB.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.sar1-sarB.CD'
out=$path'sar1-sarB.CD.trimal_gt-0.8.nex.mb+raxml.tre'

$placer $tree $bootstrap $out
