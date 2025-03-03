#!/usr/bin/env Rscript

library("edgeR")
args <- commandArgs(trailingOnly = TRUE)
conditions <- c("Exp", "Exp", "Exp", "Control", "Control", "Control")

countData <- read.table(args[1], sep='\t', header = TRUE, quote = "", row.names=1)


y <- DGEList(counts = countData, group = conditions)
y <- calcNormFactors(y)
y <- estimateDisp(y)
et <- exactTest(y)

write.table(topTags(et, n = nrow(countData), sort.by = "none"), file=args[2], sep='\t', quote=FALSE, col.names=FALSE)


