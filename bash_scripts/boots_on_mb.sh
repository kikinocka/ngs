#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

# cd '/Users/kika/ownCloud/archamoebae/trees/PFO/ver4/combined/'
cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/HOPS-CORVET/combined/'
# cd '/Users/kika/ownCloud/anaeramoeba/trees/TBCs/ver6/combined/'

tree=$path'vps3-39.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.vps3-39'
out=$path'vps3-39.trimal_gt-0.8.nex.mb+raxml.tre'

$placer $tree $bootstrap $out
