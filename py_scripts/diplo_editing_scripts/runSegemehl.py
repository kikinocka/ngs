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

def parseoptions( ):
        """ Docstring 
            .... """

        #print " ".join( sys.argv )

        parser = argparse.ArgumentParser( description=" " )
        parser.add_argument( '-f',  '--fasta',  help="reference genome fasta file",   required=True )
        parser.add_argument( '-1',  '--lib1', help="fastq lib file", required=True )
        parser.add_argument( '-2',  '--lib2', help="fastq lib file", required=True )
        parser.add_argument( '-s',  '--sam', help="sam output file name" )
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
    
    print "\n# PREPARING REF SEQUENCE"
    frefidx = os.path.basename(ARGS.fasta).split(".")[0] + ".idx"
    if not os.path.exists( frefidx ) :
        cmd = "segemehl_diplonema.x -d " + ARGS.fasta + " -x " + frefidx
        o,e = runcmd( cmd )
    print "\t[OUT] " + frefidx

    frefaidx = os.path.basename(ARGS.fasta).split(".")[0] + ".ctgaidx"
    if not os.path.exists( frefaidx ) :
        cmd = "segemehl_diplonema.x -d " + ARGS.fasta + " -x " + frefaidx  + " -F 5"
        o,e = runcmd( cmd )
        if not os.path.exists( frefaidx ) and e :
            sys.exit( "ERROR: " + e)
    print "\t[OUT] " + frefaidx
    #cmd = "samtools " + ARGS.fasta
    #o,e = runcmd( cmd )

    frefdict = os.path.basename(ARGS.fasta).split(".")[0] + ".dict"
    if not os.path.exists( frefdict ) :
        cmd = "java -jar /share/supported/apps/picard-tools-1.119/CreateSequenceDictionary.jar R=" + ARGS.fasta + " O=" + frefdict 
        o,e = runcmd( cmd )
        if not os.path.exists( frefdict ) and e :
            sys.exit( "ERROR: " + e)
    print "\t[OUT] " + frefdict
    
    print "\n# PREPARING LIB"
    # Change name of reads from '_1' to ' 1'
    llib1 = ARGS.lib1.split(',') 
    llib2 = ARGS.lib2.split(',')
    lliboutgz = []
    i = 0
    for llib in [llib1,llib2] :
        i += 1
        flib = "+".join( [ os.path.splitext(os.path.basename(x))[0] for x in llib ] )
        flib += "_%i.fastq"%(i,)
        lliboutgz.append( flib + ".gz" ) 
        print flib
        if  not os.path.exists( flib + ".gz" ) :
            for lib in llib :
                cmd = "sed  's/_%i:N:/ %i:N:/' "%(i,i) + lib + " >> " + flib
                o,e = runcmd( cmd )
            cmd = "gzip " + flib
            o,e = runcmd( cmd )
            if not os.path.exists( flib + ".gz" ) and e :
                sys.exit( "ERROR: " + e)
    flib1gz = lliboutgz[0]
    print "\t[OUT] " + flib1gz
    flib2gz = lliboutgz[1]
    print "\t[OUT] " + flib2gz    
            
    print "\n# MAPPING"
    fsam    = os.path.basename(ARGS.fasta).split(".")[0] + ".sam"
    if ARGS.sam :
        fsam    = ARGS.sam
    if not os.path.exists( fsam ):
        cmd = "nice -n 19 segemehl_diplonema.x -d " + ARGS.fasta + " -i  " + frefidx + " -q " + flib1gz + " -p " + flib2gz + " -o " + fsam + " -t 10 -s -F 6 -A 95 2>" + fsam + ".log "
        o,e = runcmd( cmd )
        if not os.path.exists( fsam ) and e :
            sys.exit( "ERROR: " + e)
    print "\t[OUT] " + fsam


    dt = time()-t1
    print " ---- time(s) = " + str(dt) + " // @SaM"

def printandflush( mess ) :
    sys.stdout.write('\r')
    sys.stdout.write( mess )
    sys.stdout.flush()

# o, e = runcmd( mycmd )
# OR runcmd( mycmd )
def runcmd( cmd, verbose=True ) : 
    if verbose == True :
        print cmd 
    p = Popen( cmd , shell=True, stdout=PIPE, stderr=PIPE)
    outmess,errmess  = p.communicate()
    
    o = "".join(outmess)
    e = "".join(errmess)
    return o,e

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

