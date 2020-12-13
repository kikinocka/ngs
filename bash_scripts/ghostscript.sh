#!/bin/sh

ghostscript='/Users/kika/miniconda3/pkgs/ghostscript-9.53.3-hb1e8313_1/bin/gs'

cd '/Users/kika/Dropbox/Docs/VZP_2020/'

infile='E901_Zahonova.pdf'
outfile='E901_Zahonova_comp.pdf'

$ghostscript -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$outfile $infile
