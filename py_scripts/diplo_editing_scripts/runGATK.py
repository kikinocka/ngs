#!/usr/bin/python

import os
import sys
import glob
import argparse
from subprocess import Popen, PIPE

# ARGUMENTS
ARGS    = {}

# TOOL 
SAMTOOLS 					= "samtools"
CREATESEQUENCEDICTIONARY 	= "/share/supported/apps/picard-tools-1.119/CreateSequenceDictionary.jar" 
ADDORREPLACEREADGROUPS 		= "/share/supported/apps/picard-tools-1.119/AddOrReplaceReadGroups.jar"
GENOMEANALYSISTK 			= "/share/supported/apps/GenomeAnalysisTK-3.4.46-gbc02625/GenomeAnalysisTK.jar"

def parseoptions( ):
	""" Docstring 
        .... """
	parser = argparse.ArgumentParser( description="Call variants with GATK" )
	parser.add_argument( '-s',  '--sam',  help="sam mapping file",   required=True )
	parser.add_argument( '-f',  '--fasta',  help="Reference file",   required=True )
	# Set of param:
	# '-T UnifiedGenotyper -ploidy 10 -glm BOTH -stand_emit_conf 10 -stand_call_conf 30'
	# '-T UnifiedGenotyper -ploidy 100 -glm BOTH -stand_emit_conf 30 -stand_call_conf 30 -mbq     30 --read_filter MappingQuality -drf DuplicateRead'
	parser.add_argument( '-g',  '--gatkparam', default= "-T UnifiedGenotyper -ploidy 100 -glm BOTH -stand_emit_conf 30 -stand_call_conf 30 -mbq 30 --read_filter MappingQuality -drf DuplicateRead ", help="GATK parameters default: -g ' -T UnifiedGenotyper -ploidy 100 -glm BOTH -stand_emit_conf 10 -stand_call_conf 30'",required=False )
	#parser.add_argument( '-r',  '--run', default=1,  type=int, help="Run command : yes '1' or print only '0'" )
	parser.add_argument( '--norun', help="Just print cmd, do not run them", action='store_true', default=False)
	parser.add_argument( '--setmapq', help="Set mapping quality to 35", action='store_true', default=False)
	# parser.add_argument( '-s',  '--suffix',  default="-a",    help="Suffix to add to filtered file name",            required=False )
	# parser.add_argument( '-a',  '--adapt3', help="3' adapter", required=False )
	# parser.add_argument( '-g',  '--adapt5', help="5' adapter", required=False )

	global ARGS
	ARGS = parser.parse_args()
	
def main():
    
	parseoptions()
	prefix 	= os.path.basename(ARGS.sam).split(".")[0]

	if not os.path.isfile( ARGS.sam ) :
		sys.exit( "sam file not found. Exit program." )
	if not os.path.isfile( ARGS.fasta ) :
		sys.exit( "fasta file not found. Exit program.")

	print "\n#.sam -> .bam"
	bam 	= prefix + ".bam"
	cmd 	= "%s view -bS  %s | samtools sort - -o %s "%(SAMTOOLS, ARGS.sam,bam)
	if not os.path.exists( bam ) :
		runcmd( cmd )
	printOrExit( bam )

	print "\n#.bam -> .bam.bai"
	bami 	= bam + ".bai"
	if not os.path.exists( bami ) :
		cmd 	= "%s index %s "%(SAMTOOLS, bam)
		runcmd( cmd )
	printOrExit( bami )

	print "\n#Reference sequence dictionary"
	fastadict 	= os.path.splitext( ARGS.fasta )[0] + ".dict"
	if not os.path.exists( fastadict ) :
		cmd 		= "java -jar %s  R=%s O=%s"%( CREATESEQUENCEDICTIONARY, ARGS.fasta, fastadict)
		runcmd( cmd )
	printOrExit( fastadict )

	print "\n#Index fasta"
	
	cmd 	= "%s faidx %s "%( SAMTOOLS, ARGS.fasta)
	runcmd( cmd )
	print "[OUT] ? "

	print "\n#Add read groups: RGLB=LIB RGPL=Illumina RGPU=run RGSM=LIB"
	bamrg 	= os.path.splitext(bam)[0] + "_RG.bam"
	if not os.path.exists( bamrg ) :
		cmd 	= "java -jar %s INPUT=%s OUTPUT=%s RGLB=LIB RGPL=Illumina RGPU=run RGSM=LIB"%(ADDORREPLACEREADGROUPS,bam,bamrg)
		runcmd( cmd )
	printOrExit( bamrg )

	print "\n#.bam -> .bam.bai"
	bamrgi	= bamrg + ".bai"
	if not os.path.exists( bamrgi ) :
		cmd     = "%s index %s "%(SAMTOOLS, bamrg)
		runcmd( cmd )
	printOrExit( bamrgi )

	if ARGS.setmapq :
		print "\n#Set mapping quality to 35"
		bamrgq	=  os.path.splitext(bamrg)[0] + "_q35.bam"
		if not os.path.exists( bamrgq ) :
			cmd     = "java -jar %s -T PrintReads -R %s  -I %s -o %s -rf ReassignMappingQuality -DMQ 35"%(GENOMEANALYSISTK, ARGS.fasta, bamrg, bamrgq)
			runcmd( cmd )
		bamrg 	= bamrgq
		printOrExit( bamrgq )

	print "\n#Index Bam with read groups"
	bamrgi  = bamrg + ".bai"
	if not os.path.exists( bamrgi ) :
		cmd 	= "%s index %s"%( SAMTOOLS, bamrg)
		runcmd( cmd )
	printOrExit( bamrgi )

	print "\n#GATK"
	vcf 	= os.path.splitext(bamrg)[0] + ".vcf"
	if not os.path.exists( vcf ) :
		cmd 	= "java -Xmx2g -jar %s -R %s  -I %s %s -o %s " %(GENOMEANALYSISTK,ARGS.fasta,bamrg,ARGS.gatkparam,vcf)
		runcmd( cmd )
	printOrExit( vcf )

	print "\nDONE"

def printOrExit( afile ) :
	if not os.path.exists( afile ) :
 		sys.exit( "File " + afile + " not created. Exit program." )
 	else :
 		print "[OUT] " + afile

def runcmd( cmd ):
	print cmd
	if not ARGS.norun : 
		p = Popen( cmd, shell=True )
		p.wait()



if __name__ == "__main__":
    try:
        main()
    
    except KeyboardInterrupt:
        print >>sys.stderr, "Program canceled by user..."



