#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

'''
Created on 11 mars 2013

@author: sam
'''

# IMPORT
import os , sys , argparse, re
import glob
from subprocess import Popen, PIPE
from time import time
from datetime import datetime

# ARGUMENTS
ARGS = {}       # Command line arguments dictionary
PATH = "/sequence-cardamom/SaM_Analyses/DiplonemidsTranscriptome/90_OtherMitoK/"
DNASEQLIB_1 = "Ds_Mi201505_1_a3_q20_paired.fastq" 
DNASEQLIB_2 = "Ds_Mi201505_2_a3_q20_paired.fastq"

def parseoptions( ):
        """ Docstring 
            .... """

        #print " ".join( sys.argv )

        parser = argparse.ArgumentParser( description=" " )
        parser.add_argument( '-f',  '--fasta',  help="Mitochondrial chromosomes fasta format",   required=True )
        parser.add_argument( '-g',  '--gff',  help="Mitochondrial chromosomes gff format",   required=True )
        parser.add_argument( '-c',  '--contigs',  help="Contigs from assembly fasta format",   required=True )
        parser.add_argument( '-p',  '--prefix',  help="Prefix for cassette names, ex: 'da_'",   required=True )
        parser.add_argument( '-o',  '--output', help="Output" )
        #parser.add_argument( '-b',  '--blast',  default=0, type=int,   help="bla bla",   required=True|False )
        #parser.add_argument( '--rna', help="Export RNA", action='store_true', default=False)
        # Noter que les tirets dans les noms d'arguments sont transformes en souligne
        global ARGS             # Modify global variable ARGS
        ARGS = parser.parse_args()
        #globals().update(vars(args))        # Makes variables be seen globally

# MAIN
def main() :
    t1    = time()
    #print "BEGIN " + str( datetime.now() )

    # ARGS                                                                           
    parseoptions( )     # Parse sys.argv if you want quick and dirty script
                        # sys.argv[ 0 ] : name of the pgm
                        # ARGS.output to access "output" argument value
    
    # splittext removes the last extension (even if more than one '.' in the file name
    # fileout = os.path.splitext(ARGS.input)[0]
    # basename WITHOUT the complete path
    # fileout = os.path.basename(ARGS.input).split(".")[0]

    e   = ""
    o   = ""
    print "\n# EXTRACT CODING AND NON-CODING FEATURES"
    fcodnoncod = os.path.splitext( ARGS.fasta )[0] + "_Cod+NonCod.fasta"
    if not os.path.exists( fcodnoncod ) : 
        # An example of shell cmd
        cmd     = PATH + "/extractCodingANDNonCodingSeq.py -f " + ARGS.fasta + " -g " + ARGS.gff
        o,e     = runcmd( cmd )
    printOrExit( fcodnoncod, e )

    print "\n# RUN BLAST CONTIGS AGAINST MITO CODING AND NON-CODING SEQ"
    if not os.path.exists( "MITO.nhr" ) :
        cmd     = "makeblastdb -in " + fcodnoncod + " -dbtype 'nucl' -out MITO "
        o,e     = runcmd( cmd )
    printOrExit( "MITO.nhr", e )

    fblast       = os.path.splitext( ARGS.contigs )[0] + "_X_MITO.m6.out"
    fblastlist      = os.path.splitext( ARGS.contigs )[0] + "_X_MITO.m6.list"
    fblastfasta      = os.path.splitext( ARGS.contigs )[0] + "_X_MITO.m6.fasta" 
    if not os.path.exists( fblast ) :
        cmd     = "blastn -query " + ARGS.contigs + " -db MITO -out " + fblast + " -perc_identity 95 -max_target_seqs 100000 -culling_limit 1 -outfmt 6 "
        o,e     = runcmd( cmd )
    printOrExit( fblast, o+e )

    print "\n# TOTAL NB CONTIGS FOUND"
    cmd     = "cut -f 1 " + fblast + " | sort | uniq > " + fblastlist + " && wc -l " + fblastlist
    o,e     = runcmd( cmd )
    print o

    print "\n# EXTRACT FASTA "
    if not os.path.exists( fblastfasta ) :
        cmd     = "fasta_filter_on_ID.py -f " + ARGS.contigs + " -l " + fblastlist + " -o " + fblastfasta
        o,e     = runcmd( cmd )
    printOrExit( fblastfasta, e )

    # Detection of chimeric contigs
    print "\n# CHIMERIC CONTIGS DETECTION"
    fchimer    = os.path.splitext( fblastfasta )[0] + "_chimer.gff"
    if not os.path.exists( fchimer ) :
        cmd = "chimericContigsDetection.py -f " + fblastfasta + " -1 " + DNASEQLIB_1 + " -2 " + DNASEQLIB_2 + " -p '--rf --end-to-end --no-unal -p 6 --very-fast' -o " + fchimer
        runcmd( cmd )
    printOrExit( fchimer, e ) 

    print "\n# FILTER CONTIGS "
    ffilt   = os.path.splitext( fblast )[0] + ".gff3"
    if not os.path.exists( ffilt ) :
        cmd = PATH + "/filterNconvertBLASTm6_2_GFF_diplonemids.py -b " + fblast + " -g " + ffilt + " -p " + ARGS.prefix + " -l " + fchimer
        o,e     = runcmd( cmd )
    printOrExit( ffilt, e )   
    cmd     = "cut -f 1 " + ffilt + " |  sort | uniq | wc -l"
    o,e     = runcmd( cmd )
    print   o



    print "\n# EXTRACT CASSETTE THAT COULD BE EXTENDED "
    fextcass    = os.path.splitext( ffilt )[0] + "_extendedCass.gff3"
    fextlist    = os.path.splitext( ffilt )[0] + "_extendedCass.list"
    fextfasta   = os.path.splitext( ffilt )[0] + "_extendedCass.fasta"
    if not os.path.exists( fextcass ) :
        cmd     = "cat " + ffilt + " | grep 'Known_K7' > " + fextcass
        o,e     = runcmd( cmd )
    printOrExit( fextcass, e ) 
    cmd     = "cut -f 1 " + fextcass + " |  sort | uniq > " + fextlist + " && wc -l " + fextlist
    o,e     = runcmd( cmd )
    print o
    if not os.path.exists( fextfasta ) :
        cmd     = "fasta_filter_on_ID.py -f " + ARGS.contigs + " -l " + fextlist + " -o " + fextfasta
        o,e     = runcmd( cmd ) 
    printOrExit( fextfasta, e )

    print  "\n# EXTRACT CONTIGS WITH NON-CODING AND EMPTY SPACE "
    fempty      = os.path.splitext( ffilt )[0] + "_emptyspace.gff3"
    femptylist  = os.path.splitext( ffilt )[0] + "_emptyspace.list"
    femptyfasta = os.path.splitext( ffilt )[0] + "_emptyspace.fasta"

    if not os.path.exists( fempty ) :
        cmd     = "cat " + ffilt + " | grep 'empty_space' > " + fempty
        o,e     = runcmd( cmd )
    printOrExit( fempty, e ) 
    cmd     = "cut -f 1 " + fempty + " |  sort | uniq > " + femptylist + " && wc -l " + femptylist
    o,e     = runcmd( cmd )
    print   o
    if not os.path.exists( femptyfasta ) :
        cmd     = "fasta_filter_on_ID.py -f " + ARGS.contigs + " -l " + femptylist + " -o " + femptyfasta
        o,e     = runcmd( cmd )
    printOrExit( femptyfasta, e )


    print  "\n# EXTRACT CONTIGS WITH CANDIDATES (non-coding flanking empty space > 50bp)"
    fcand       = os.path.splitext( ffilt )[0] + "_candidate.gff3"
    fcandlist   = os.path.splitext( ffilt )[0] + "_candidate.list"
    fcandfasta  = os.path.splitext( ffilt )[0] + "_candidate.fasta"
    if not os.path.exists( fcand ) :
        cmd     = "cat " + ffilt + " | grep 'candidate' > " + fcand
        o,e     = runcmd( cmd ) 
    printOrExit( fcand, e )
    cmd     = "cut -f 1 " + fcand + " |  sort | uniq > " + fcandlist + "&& wc -l " + fcandlist
    o,e     = runcmd( cmd )
    print   o   
    if not os.path.exists( fcandfasta ) :
        cmd     = "fasta_filter_on_ID.py -f " + ARGS.contigs + " -l " + fcandlist + " -o " + fcandfasta
        o,e     = runcmd( cmd )
    printOrExit( fcandfasta, e )

    print "\nDONE"


    dt = time()-t1
    print " ---- time(s) = " + str(dt) + " // @SaM"

def printandflush( mess ) :
    sys.stdout.write('\r')
    sys.stdout.write( mess )
    sys.stdout.flush()

# How to run a shell command
def runshellcmd( infile ):
    print "\n# COMMENT ABOUT MY CMD"
    outfile = os.path.splitext( infile )[0] + ".EXTENSION"
    if not os.path.exists( outfile ) :
        # An example of shell cmd
        cmd     = "cp %s %s" %( infile, outfile )
        runcmd( cmd )
    printOrExit( outfile )
    print "\nDONE"

def printOrExit( afile, err="" ) :
    if not os.path.exists( afile ) :
        mess = "File " + afile + " not created.\n"
        if len(err) > 0 :
             mess += err + "\n" 
        sys.exit( mess + "Exit program." )
    else :
        print "[OUT] " + afile

# o, e = runcmd( mycmd )
# OR runcmd( mycmd )
def runcmd( cmd, verbose=True ) : 
    if verbose == True :
        print cmd 
    p = Popen( cmd , shell=True, stdout=PIPE, stderr=PIPE)
    outmess,errmess  = p.communicate()
    return "".join(outmess), "".join(errmess) 

# Read a fasta file
# head,seq    = readFasta( MYFILE ).next()
# OR
#for head,seq in readFasta( MYFILE ) :
def readFasta( filename ) :
    ffasta  = open( ARGS.fasta, "r")
    #pathead = re.compile( ">\s*(\S+)\s+(.*)$")
    #recid   = ""
    rechead = ""
    recseq  = ""

    # For each line in file 1
    for line in ffasta :
        # New record found
        #mathead = pathead.match( line )
        #if mathead :
        if line[0] == '>' :
            # Print previous record
            if len(recid) > 0 :
                yield rechead,recseq
                #print "%s\t%s\n%s"%( recid, recdesc, recseq )
            # Get info for new record
            #recid   = mathead.group( 1 )
            rechead = line.strip()
            recseq  = ""
        else :
            recseq += line.strip()

    # Print last record
    yield rechead, recseq
    #print "%s\t%s\n%s"%( recid, recdesc, recseq )    



def readfile( filename ) :
    f = open( filename , "r" )
    # Line by line ; If all lines at once lines = f.readlines()
    # for n,line in enumerate( f ) :
    for line in f : 
        # do some stuff
        col     = line.split( "\t" )
        print line
    f.close()

    # All lines at once
    #with open( filename , 'r' ) as f :
    #    alist = [ line.strip() for line in f ]

def writeinfile( filename , content ) :
    f  = open( filename , "a" )    # a : append ; w : overwrite
    if isinstance( content , str ) :
        f.write( content + "\n" )
    else :
        f.write( "\n".join(content) )
    f.close()

def removefile( filename ) :
    if os.path.exists( filename ) :
                os.remove( filename )

def outfilename( infile , suffix ) :
    fpat    = re.compile( r"(.*)\.(.*)" )
    match   = fpat.match( infile )
    fout    = match.group(1) + suffix
    return fout

# http://biopython.org/DIST/docs/api/Bio.SeqIO._convert-module.html
def fastq_illumina_to_fastq_sanger_Dico() :
    mapping = "".join([chr(0) for ascii in range(0, 64)] 
                + [chr(33 + q) for q in range(0, 62 + 1)]
                + [chr(0) for ascii in range(127, 256)])
    assert len(mapping) == 256 
    return mapping







if __name__ == "__main__":
    try:
        main()
    
    except KeyboardInterrupt:
        print >>sys.stderr, "Program canceled by user..."

