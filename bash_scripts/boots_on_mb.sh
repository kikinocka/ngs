#!/bin/bash

# placer='/Users/kika/ownCloud/lab_documents/Joel/lael_scripts/hmmer_tools/boots_on_mb_2.py'
placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

# path='/Users/kika/ownCloud/archamoebae/trees/D-LDH/ver4/combined/'
# path='/Users/kika/ownCloud/membrane-trafficking/trees/SNAREs/r_new/combined/'
path='/Users/kika/ownCloud/anaeramoeba/trees/TBCs/ver6/combined/'
tree=$path'rabs.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'rabs.trimal_gt-0.8.RAxML_bootstrap.result'

$placer $tree $bootstrap $path
