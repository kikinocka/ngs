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

#RNASEQLIB_1 = "DaT-Hi_R1.a3.q20-r_paired.fastq,DaT_R1.a3.q20-r_paired.fastq"
#RNASEQLIB_2 = "DaT-Hi_R2.a3.q20-r_paired.fastq,DaT_R2.a3.q20-r_paired.fastq"

#DNASEQLIB_1 = "Da_Mi201505_1_a3_q20_paired.fastq"
#DNASEQLIB_2 = "Da_Mi201505_2_a3_q20_paired.fastq"

def parseoptions( ):
        """ Docstring 
            .... """

        #print " ".join( sys.argv )

        parser = argparse.ArgumentParser( description=" " )
        parser.add_argument( '-f',  '--fasta',  help="Reference fasta file",   required=True )
        parser.add_argument( '--rna1', help="RNA library 1", required=True )
        parser.add_argument( '--rna2', help="RNA library 2", required=True )
        parser.add_argument( '--dna1', help="DNA library 1", required=True )
        parser.add_argument( '--dna2', help="DNA library 2", required=True )

        #parser.add_argument( '-o',  '--output', help="Output" )
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

    print "\n# RNA-seq: map reads with Segemehl"
    fsam = os.path.splitext( ARGS.fasta )[0] + "_X_RNA.sam"
    if not os.path.exists( fsam ) : 
        cmd     = "./runSegemehl.py -f " + ARGS.fasta + " -1 " + ARGS.rna1 + " -2 " + ARGS.rna2 + " -s " + fsam 
        o,e     = runcmd( cmd )
    printOrExit( fsam, e )

    
    print "\n# RNA-seq: Remove reads mapped with indels"
    findel = os.path.splitext( fsam )[0] + "_indel0.sam"
    if not os.path.exists( findel ) : 
        cmd     = "filterSAMbyQualityAndIndel.py -f " + findel + " -s " + fsam + " -d 0"
        o,e     = runcmd( cmd )
    printOrExit( findel, e )

    print "\n# RNA-seq: variant calling" 
    fgatk   = os.path.splitext( findel )[0] + "_RG_q35.vcf"
    if not os.path.exists( fgatk ) :
        cmd     = "./runGATK.py -s " + findel + " -f " + ARGS.fasta + " -g '-T UnifiedGenotyper -ploidy 10 -glm BOTH -stand_emit_conf 10 -stand_call_conf 30' --setmapq"
        o,e     = runcmd( cmd ) 
    printOrExit( fgatk, e )

    print "\n# RNA-seq: filter variants (keep QD [Quality by depth] > 2.0 && SOR [Strand bias] < 3.0 "
    fRNAvcf = os.path.splitext( fgatk )[0] + "_QD2Sor3.vcf"
    if not os.path.exists( fRNAvcf ) :
        cmd     = "java -jar /share/supported/apps/GenomeAnalysisTK-3.4.46-gbc02625/GenomeAnalysisTK.jar -T SelectVariants -R " + ARGS.fasta + " -o " + fRNAvcf + " --variant " + fgatk + " --selectexpressions \"QD > 2.0 && SOR < 3.0\" "
        o,e     = runcmd( cmd )
    printOrExit( fRNAvcf, e )


    print "\n# DNA-seq: map reads with Bowtie local"
    fsam    = os.path.splitext( ARGS.fasta )[0] + "_X_DNA.sam"
    # Build library
    ref  = os.path.splitext( ARGS.fasta )[0].upper()
    if not os.path.exists( ref + ".1.bt2" ) : 
        cmd = "bowtie2-build -f " + ARGS.fasta + " " + ref 
        runcmd( cmd )
    # Mapping
    if not os.path.exists( fsam ) :
        cmd = "bowtie2 --no-unal --local --rf -p 6 -x " + ref + " -1 " + ARGS.dna1  + " -2 " +  ARGS.dna2 + " -S " + fsam 
        o,e = runcmd( cmd )
    printOrExit( fsam, e )
        
    print "\n# DNA-seq: variant calling"
    fgatk   = os.path.splitext( fsam )[0] + "_RG_q35.vcf"
    if not os.path.exists( fgatk ) :
        cmd     = "./runGATK.py -s " + fsam + " -f " + ARGS.fasta + " -g '-T UnifiedGenotyper -ploidy 10 -glm BOTH -stand_emit_conf 10 -stand_call_conf 30' --setmapq"
        o,e     = runcmd( cmd )
    printOrExit( fgatk,e )

    print "\n# DNA-seq: filter variants (keep QD [Quality by depth] > 2.0 && SOR [Strand bias] < 3.0 "
    fDNAvcf = os.path.splitext( fgatk )[0] + "_QD2Sor3.vcf"    
    if not os.path.exists( fDNAvcf ) :
        cmd     = "java -jar /share/supported/apps/GenomeAnalysisTK-3.4.46-gbc02625/GenomeAnalysisTK.jar -T SelectVariants -R " + ARGS.fasta + " -o " + fDNAvcf + " --variant " + fgatk + " --selectexpressions \"QD > 2.0 && SOR < 3.0\" "
        o,e     = runcmd( cmd )
    printOrExit( fDNAvcf, e )


    print "\n# Edited Sites RDD: RNA DNA differences "
    fedited = os.path.splitext( ARGS.fasta )[0] + "_RDD.vcf"
    if not os.path.exists( fedited ) :
        cmd     = "./vcf_isec_SaM.py -r " + fRNAvcf + " -d " + fDNAvcf + " -o " + fedited
        o,e     = runcmd( cmd )
    printOrExit( fedited, e )

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
    #print "[OUT] " + afile

# o, e = runcmd( mycmd )
# OR runcmd( mycmd )
def runcmd( cmd, verbose=True ) : 
    if verbose == True :
        print cmd 
    p = Popen( cmd , shell=True, stdout=PIPE, stderr=PIPE)
    outmess,errmess  = p.communicate()
    return "".join(outmess), "".join(errmess) 
    #return "ok","ok"

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

