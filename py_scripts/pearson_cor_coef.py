#!/usr/bin/python3
import os
import pandas as pd
import numpy as np
from skbio import DistanceMatrix
from skbio.stats.distance import mantel

os.chdir('/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution-test/pearson_correlation/')
opa1 = pd.read_csv('opa1.tsv', sep='\t')
mic60 = pd.read_csv('mic60.tsv', sep='\t')
enol = pd.read_csv('enol.tsv', sep='\t')
out = open('correlation.tsv', 'w')
IDs = ["Diphylleia_rotans 1", "Corallochytrium_limacisporum 2", "Helgoeca_nana 3", "Acanthoeca_spectabilis 4", 
	"Salpingoeca_rosetta 5", "Mylnosiga_fluctuans 6", "Choanoeca_flexa 7", "Branchiostoma_floridae 8", 
	"Ciona_intestinalis 9", "Salmo_salar 10", "Danio_rerio 11", "Physeter_macrocephalus 12", "Homo_sapiens 13", 
	"Mus_musculus 14", "Gallus_gallus 15"]

opa1 = opa1.set_index('Unnamed: 0')
opa1 = np.asarray(opa1)
opa1 = DistanceMatrix(opa1, IDs)

mic60 = mic60.set_index('Unnamed: 0')
mic60 = np.asarray(mic60)
mic60 = DistanceMatrix(mic60, IDs)

enol = enol.set_index('Unnamed: 0')
enol = np.asarray(enol)
enol = DistanceMatrix(enol, IDs)


c_OM, p_OM, n = mantel(opa1, mic60)
print(c_OM)
print(p_OM)

c_ME, p_ME, n = mantel(mic60, enol)
print(c_ME)
print(p_ME)

c_OE, p_OE, n = mantel(opa1, enol)
print(c_OE)
print(p_OE)

out.write('{}\t{}\t{}'.format(round(c_OM, 3), round(c_ME, 3), round(c_OE, 3)))
