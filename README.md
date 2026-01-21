# TCGA-BRCA-Gene-Expression-Analysis-
Python-based RNA-seq analysis program to identify highly expressed protein-coding genes in breast cancer tissue samples.

This project analyzes publicly available **TCGA-BRCA RNA-seq data** to compute and visualize the top protein-coding genes 

## Overview
This program processes gene-level RNA-seq expression data derived from breast invasive carcinoma (BRCA) tissue samples in the **TCGA (The Cancer Genome Atlas)** database.

Each patient dataset contains various RNA-sequencing counts
The program focuses on **protein-coding genes** expression values across patients, and identifies the genes with the highest average expression levels.

The program follows these steps:

1. Loads gene-level RNA-seq data from `.tsv` files
2. Filters rows and columns 
3. Merges patient datasets to compute averages 
4. Generates a bar plot visualization of the results

## Features
- Processes TCGA-BRCA RNA-seq gene expression data
- Collects expression values across multiple samples
- Computes average TPM expression per gene
- Visualizes top expressed genes using bar plots

## Requirements
- Python 3.8+
- pandas
- matplotlib
