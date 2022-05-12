import os, argparse
import Bio
parser = argparse.ArgumentParser()
parser.add_argument("--input" ,required=False, default='./demo/input.tsv',dest='Input Gene Feature data. e.g.: *.csv, *.txt, *.tsv')
parser.add_argument("--output", required=False, default='./demo/output.tsv', dest='Export translation gene data.')
# parser.add_argument("-h", "--help", default='help',required=False)
args = parser.parse_args()
print(args)

# --help data formate = [csv, txt, tsv]
# --input {dataname}.tsv, {dataname}.csv
# --output {dataname}.tsv, {dataname}.csv
# --dtype pandas, tsv
# function 
    # translation Gene -> compare group of 3 rna    