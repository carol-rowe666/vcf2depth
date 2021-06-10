# vcf2depth
Uses the vcf output file from ipyrad and return stats on the average depth of alleles.
From the vcf file, we have NP and NS:
  NS: number of samples with depth of at least 1
  NP: total depth across all samples
Hence, total number of possible samples can differ from the NS value.
Output contains stats on: NP/NS and NP/total possible samples

Example output:

  stat         DP/NS        DP/all   
  count  13425.000000  13425.000000  
   mean     45.821321     31.562692  
    std     86.165466     64.912396  
    min      1.000000      0.031579  
    25%     21.954545     12.978947  
    50%     28.809524     18.400000  
    75%     42.265625     28.568421  
    max   2134.703125   1438.115789  
     
