# vcf2depth
Uses the vcf output file from ipyrad and return stats on the average depth of alleles.  
From the vcf file, we have DP and NS:  
&nbsp;&nbsp;  NS: number of samples with depth of at least 1  
&nbsp;&nbsp;  DP: total depth across all samples  
Hence, total number of possible samples can differ from the NS value.   
Output contains stats on: DP/NS and NP/total possible samples.  
  
Example output:  
  
  stat&nbsp;&nbsp;         DP/NS&nbsp;&nbsp;        DP/all   
  count&nbsp;&nbsp;  13425.000000&nbsp;&nbsp;  13425.000000  
   mean&nbsp;&nbsp;     45.821321&nbsp;&nbsp;     31.562692  
    std&nbsp;&nbsp;     86.165466&nbsp;&nbsp;     64.912396  
    min&nbsp;&nbsp;      1.000000&nbsp;&nbsp;      0.031579  
    25%&nbsp;&nbsp;     21.954545&nbsp;&nbsp;     12.978947  
    50%&nbsp;&nbsp;     28.809524&nbsp;&nbsp;     18.400000  
    75%&nbsp;&nbsp;     42.265625&nbsp;&nbsp;     28.568421  
    max&nbsp;&nbsp;   2134.703125&nbsp;&nbsp;   1438.115789  
     
