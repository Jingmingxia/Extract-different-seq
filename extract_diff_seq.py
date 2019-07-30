#!/usr/bin/env python
#coding:utf-8
#by xjm

import sys
import logging
import argparse
from Bio import SeqIO

def read_fa(fa_file):
    seq_dict = {}
    for record in SeqIO.parse(fa_file,'fasta'):
      if 'HSDAV1212s' in record.id or 'HSDAV0110s' in record.id:  #You can change the strings or add them to the arguments
        seq_dict[record.id] = record.seq
      else:
        continue
    return seq_dict

def get_same(fa_file,dict_seq):
  seqs = tuple(dict_seq.values())
  if seqs[0] != seqs[1]:
    with open(fa_file+'.out','w') as fh:
      for i in dict_seq:
        fh.write(">%s\n%s\n" % (i,dict_seq[i]))
 
def set_args(parser):
  parser.add_argument('-i','--input',metavar='FILE',type=str,required=True,help='Input file')
  return parser

def main():
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
        format="[%(levelname)s] %(message)s"
    )
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
Description:
  extract_cds.py  extract the specified sample seq
''')
    args = set_args(parser).parse_args()
    d = read_fa(args.input)
    get_same(args.input,d)

if __name__ == "__main__":
  main()
