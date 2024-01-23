###########################################################################
### R script for processing the TARA Oceans metabarcoding data with DADA2
### Can be run on a laptop (although 8GB of memory recommended)
###
### Benjamin Callahan (benjamin.j.callahan AT gmail.com)
###
###########################################################################

library(dada2); packageVersion("dada") # This script expects 1.4 or higher
library(biomformat)

### Set path and create directories

path <- "~/TARA" # Should exist, and contain metabar.csv
fn <- file.path(path, "metabar.csv")
path.fq <- file.path(path, "fastq")
dir.create(path.fq)

### Download the TARA Oceans metabarcoding sequence data (need wget)

samdf <- read.csv(fn, header=TRUE, stringsAsFactors = FALSE)
setwd(path.fq)
index <- 1
for(fni in samdf$Corresponding.nucleotides.data.published.at.ENA) {
  erri <- strsplit(fni, "/")[[1]][[7]]
  ftp.pathF <- paste0("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/", substr(erri, 1, 6), "/", erri, "/", erri, "_1.fastq.gz")
  ftp.pathR <- paste0("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/", substr(erri, 1, 6), "/", erri, "/", erri, "_2.fastq.gz")
  system(paste("wget", ftp.pathF))
  system(paste("wget", ftp.pathR))
  cat("Got", index, "\n")
  index <- index+1
}

### Filter and Trim

fnFs <- list.files(path.fq, pattern="_1.fastq.gz", full.names = TRUE)
fnRs <- list.files(path.fq, pattern="_2.fastq.gz", full.names = TRUE)
all(sapply(strsplit(basename(fnFs), "_"), `[`, 1)==sapply(strsplit(basename(fnRs), "_"), `[`, 1)) # TRUE

bcF <- "TTGTACACACCGCCC"
bcR <- "CCTTCYGCAGGTTCACCTAC"
path.filt <- file.path(path.fq, "filtered")
filtFs <- file.path(path.filt, basename(fnFs))
filtRs <- file.path(path.filt, basename(fnRs))
# Primer sequences are trimmed off the reads
# Additionally, the forward barcode is used to orient the paired reads, which are randomly oriented
#    in the raw data
track <- filterAndTrim(fwd=fnFs, rev=fnRs, filt=filtFs, filt.rev=filtRs, trimLeft=nchar(c(bcF, bcR)),
                       truncLen=125, maxEE=0.6, rm.phix=TRUE, barcode="TTGTACACACCGCCC", multithread=TRUE)

# saveRDS(track, file.path(path, "filtered","track.rds")) # If breaking into multiple scripts

### Infer ASVs with DADA2

# PLEASE NOTE: This section takes about 8 days to run on a 2016 Macbook Pro.
# PLEASE NOTE: The specific processing steps here, in particular learning the error rates from
#   each sample individually, are not typically recommended. Please see the online Big Data tutorial
#   for our recommendations for most large datasets: http://benjjneb.github.io/dada2/bigdata.html
# This workflow deviates from the Big Data workflow because this data has two unusual features:
#   we don't know what sequencing run each sample came from (as it wasnt in the public metadata),
#   and the samples are all large enough (>1M reads on average) that a single sample contains
#   enough reads to very accurately estimate the error rates. Thus it is conservative to estimate
#   error rates from each sample individually to guard against the possibility of variation in the
#   error rates between runs, with the cost of additional computation time.
# PLEASE NOTE: This section would be much faster (1-2 days on a 2016 Macbook Pro) if a subset
#   of the data from eah run was used to estimate the error rates, as in the Big Data workflow.
# PLEASE NOTE: This is intended as a demonstration of how DADA2 and ASV methods in general can
#   process large dataset on cheap commodity hardware (eg. a laptop). This same job can of course
#   be completed much faster -- several hours -- on common compute nodes.

filtFs <- list.files(path.filt, pattern="_1.fastq.gz", full.names = TRUE)
filtRs <- list.files(path.filt, pattern="_2.fastq.gz", full.names = TRUE)
identical(sapply(strsplit(basename(filtFs), "_"), `[`, 1), sapply(strsplit(basename(filtRs), "_"), `[`, 1)) # TRUE
sams <- sapply(strsplit(basename(filtFs), "_"), `[`, 1)

for(i in seq_along(filtFs)) {
  drpF <- derepFastq(filtFs[[i]])
  ddF <- dada(drpF, err=NULL, selfConsist=TRUE, multithread=TRUE)
  drpR <- derepFastq(filtRs[[i]])
  ddR <- dada(drpR, err=NULL, selfConsist=TRUE, multithread=TRUE)
  merger <- mergePairs(ddF, drpF, ddR, drpR)
  saveRDS(merger, file.path(path.filt, "rds", paste0(sams[[i]], "_merger.rds")))
}

### Create sequence table, and remove chimeras

# Read the merged data back in
mergers <- vector("list", length(sams))
names(mergers) <- sams
for(sam in sams) {
  mergers[[sam]] <- readRDS(file.path(path.filt, "rds", paste0(sam, "_merger.rds")))
}
# Read the metadata back in
samdf <- read.csv(fn, header=TRUE, stringsAsFactors = FALSE)
rownames(samdf) <- samdf$INSDC.run.accession.number.s.
samdf <- samdf[sams,]
identical(rownames(samdf), sams)

# Make table, chimeras not yet removed
sta <- makeSequenceTable(mergers)
saveRDS(sta, file.path(path, "sta.rds"))
write_biom(make_biom(t(sta), sample_metadata=samdf), file.path(path, "sta.biom"))

# Consensus chimera removal, recommended
st.consensus <- removeBimeraDenovo(sta, tableMethod = "consensus", multithread=TRUE)
saveRDS(st.consensus, file.path(path, "st.consensus.rds"))
write_biom(make_biom(t(st.consensus), sample_metadata=samdf), file.path(path, "st.consensus.biom"))

# Pooled chimera removal
st.nochim <- removeBimeraDenovo(sta, method="pool", multithread=TRUE)
saveRDS(st.nochim, file.path(path, "st.nochim.rds"))
write_biom(make_biom(t(st.nochim), sample_metadata=samdf), file.path(path, "st.nochim.biom"))

