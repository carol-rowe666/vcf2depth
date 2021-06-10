"""
Use the vcf output file from ipyrad and return stats on the average depth of alleles.

The vcf file has a column: 'INFO' with NS and DP values.
NS: number of samples with depth of at least 1
NP: total depth across all samples
Output contains 2 columns of stats.
    1.) NP/NS
    2.) NP/total possible samples

Usage: python vcf2depth.py your_input.vcf

File Name: vcf2depth.py
Author: Carol A. Rowe
Date Created: 2021-06-09 using Python 3.9.2

"""

import argparse
import pandas as pd

__author__ = "Carol Rowe"

def vcf2depth(vcf):
    # to avoid SettingWithCopyWarning in some lines of code
    pd.options.mode.chained_assignment = None
    # read in your vcf file to a df
    vcf = pd.read_csv(vcf, delim_whitespace=True, skiprows=10)
    # get column with just the NS and DP info - the "INFO" column
    my_vcf = vcf[['INFO']]
    # put NS and DP in separate columns
    my_vcf[['NS', 'DP']] = my_vcf['INFO'].str.split(';', expand=True)
    # get numberic value from each of these columns
    my_vcf['NS'] = my_vcf['NS'].apply(lambda x: x.split('=')[1])
    my_vcf['DP'] = my_vcf['DP'].apply(lambda x: x.split('=')[1])
    # convert from object to integer dtype
    my_vcf[['DP', 'NS']] = my_vcf[['DP', 'NS']].astype(int)
    # calculate the average depth per non-zero sample
    my_vcf['DP/NS'] = my_vcf['DP'] / my_vcf['NS']
    # also want to calculate the depth for ALL samples whether or not had data
    # first get number of samples (num columns - num columns with non-sample info)
    num_samples = vcf.shape[1]- 9
    my_vcf['DP/all'] = my_vcf.loc[:,'DP'] / num_samples
    # get description of results
    output = my_vcf[['DP/NS', 'DP/all']].describe().rename_axis('stat').reset_index()

    # save your results
    output.to_csv('vcf2depth_output.csv', index=False)

# if name in main so we can run vcf2depth.py by itself (main)
# or it can still be used if you use it embedded (import vcf2depth) within another script (name)
if __name__ in '__main__':
    # This allows the --help to show the docstring at the top of this script.
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    # Add arguments:
    # First argument is mandatory
    parser.add_argument('input', metavar='vcf_input_file', help='Enter the name of your vcf file.')
    # Array for all arguments passed to script:
    args = parser.parse_args()

    # Now, we can access the arguments input by the user and apply to our function
    vcf2depth(args.input)