library(dplyr)
library(treemap)

path <- "xxx"
setwd(path)

full_tab <- read.table("dataset.csv", header = T, sep = ";", row.names = 1, check.names = F) ### loading the dataset
tab_full <- full_tab %>% select(-c("seqs")) ### deleting sequences from dataset
full_tab_sum <- tab_full %>%  ### making summary of samples from the same location type
  mutate(BC = rowSums(across(c(BC1:BC8)))) %>%
  mutate(BM = rowSums(across(c(BM1:BM8)))) %>%
  mutate(BS = rowSums(across(c(BS1:BS8)))) %>%
  mutate(CDFC = rowSums(across(c(CDFC1:CDFC8)))) %>%
  mutate(CDFF = rowSums(across(c(CDFF1:CDFF8)))) %>%
  mutate(CDKC = rowSums(across(c(CDKC1:CDKC8)))) %>%
  mutate(CDKF = rowSums(across(c(CDKF1:CDKF8)))) %>%
  mutate(CDS = rowSums(across(c(CDS1:CDS8)))) %>%
  mutate(total = rowSums(across(c(BC:CDS))))
  
### treemap for each location type
treemap(full_tab_sum, index = c("Supergroup", "Division", "Class"), vSize = "BC")
treemap(full_tab_sum, index = c("Supergroup", "Division", "Class"), vSize = "BM")
treemap(full_tab_sum, index = c("Supergroup", "Division", "Class"), vSize = "BS")
treemap(full_tab_sum, index = c("Supergroup", "Division", "Class"), vSize = "CDFC")
treemap(full_tab_sum, index = c("Supergroup", "Division", "Class"), vSize = "CDFF")
treemap(full_tab_sum, index = c("Supergroup", "Division", "Class"), vSize = "CDKC")
treemap(full_tab_sum, index = c("Supergroup", "Division", "Class"), vSize = "CDKF")
treemap(full_tab_sum, index = c("Supergroup", "Division", "Class"), vSize = "CDS")
  