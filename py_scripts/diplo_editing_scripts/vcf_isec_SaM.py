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
	parser = argparse.ArgumentParser( description="Diff between RNA and DNA var for mudules only" )
	parser.add_argument( '-r',  '--rnavcf',  help="RNA vcf file",   required=True )
	#parser.add_argument( '-m',  '--module',  help="Module file",   required=True )
	parser.add_argument( '-d',  '--dnavcf',  help="DNA vcf file",   required=True )
	parser.add_argument( '-o',  '--outfile',  help="Output file name",   required=True )
	# Set of param:
	# '-T UnifiedGenotyper -ploidy 10 -glm BOTH -stand_emit_conf 10 -stand_call_conf 30'
	# '-T UnifiedGenotyper -ploidy 100 -glm BOTH -stand_emit_conf 30 -stand_call_conf 30 -mbq     30 --read_filter MappingQuality -drf DuplicateRead'
	#parser.add_argument( '-g',  '--gatkparam', default= "-T UnifiedGenotyper -ploidy 100 -glm BOTH -stand_emit_conf 30 -stand_call_conf 30 -mbq 30 --read_filter MappingQuality -drf DuplicateRead ", help="GATK parameters default: -g ' -T UnifiedGenotyper -ploidy 10 -glm BOTH -stand_emit_conf 10 -stand_call_conf 30'",required=False )
	#parser.add_argument( '-r',  '--run', default=1,  type=int, help="Run command : yes '1' or print only '0'" )
	parser.add_argument( '--norun', help="Just print cmd, do not run them", action='store_true', default=False)
	#parser.add_argument( '--setmapq', help="Set mapping quality to 35", action='store_true', default=False)
	# parser.add_argument( '-s',  '--suffix',  default="-a",    help="Suffix to add to filtered file name",            required=False )
	# parser.add_argument( '-a',  '--adapt3', help="3' adapter", required=False )
	# parser.add_argument( '-g',  '--adapt5', help="5' adapter", required=False )

	global ARGS
	ARGS = parser.parse_args()
	
def main():
    
	parseoptions()
	#prefix 	= os.path.basename(ARGS.sam).split(".")[0]

	# Sample name
	print "\n !!!!! Sample name must be the SAME, ex: 'nuc'. Change it in vcf header line if it is not the case\n"
	print "header should be:"
	print "#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  nuc"

	fziprna	= sortzipindex( ARGS.rnavcf )
	
	#print "\n#Filter for variants in modules"
	#fmod 	= ARGS.prefix + "_mod.vcf"
	#cmd 	= "tabix -h %s -R %s > %s "%( fzip, ARGS.module, fmod )
	#runcmd( cmd )
	
	#fzip 	= sortzipindex( ARGS.prefix + "_mod", fmod )
	fzipdna = sortzipindex( ARGS.dnavcf )

	print "\n#Difference RNA - DNA variants"
	if ARGS.outfile :
		fedit = ARGS.outfile
	else :
		fedit 	= os.path.basename( fziprna ).split(".")[0] + "-DNA_edited.vcf"
	cmd 	= "vcf-isec -c %s %s > %s"%( fziprna, fzipdna, fedit )  
	runcmd( cmd )

	print "\nDONE"


def sortzipindex( vcf ) :

        print "\nSort -> Zip -> index"
	prefix 	= os.path.splitext( os.path.basename( vcf ))[0]

        fsort   = prefix + "_sorted.vcf"
        if not os.path.exists( fsort ) :
		cmd     = "cat %s | vcf-sort -c > %s" %( vcf, fsort )
        	runcmd( cmd )
	
        fzip    = fsort + ".gz"
	if not os.path.exists( fzip ) :
        	cmd     = "bgzip %s" %( fsort,)
        	runcmd( cmd )
        
		cmd     = "tabix -p vcf %s"%( fzip,)
		runcmd( cmd )	

	return fzip


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



