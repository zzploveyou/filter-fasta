# coding:utf-8
"""
filter some id from fasta into a new fasta.

filter uniref90 from uniref100
according ids.
"""
import os

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

import log

mylog = log.Terminal_log()


def filter_fasta(fastafile, filters):
    n = 0
    path = os.path.dirname(fastafile)
    for seq_record in SeqIO.parse(fastafile, "fasta"):
        ID = seq_record.id
        seq = seq_record.seq
        des = seq_record.description
        rec = SeqRecord(seq, id=ID, description=des)
        idd = ID.split("_")[-1]
        if idd in filters:
            n += 1
            mylog.info("idd: %s, num: %d" % (idd, n))
            # filename = os.path.join(path, "result.fasta")
            filename = "/home/zzp/DATABASE/uniref100.fasta"
            SeqIO.write(rec, open(filename, 'a'), "fasta")

    mylog.done("done.")


def main():
    filters = []
    for line in open("/home/zzp/DATABASE/uniref90.list"):
        idd = line.strip().split("_")[-1]
        filters.append(idd)
    mylog.info("filters read over.")
    # filter_fasta("/media/zzp/temp/example.fasta", filters)
    filter_fasta("/media/zzp/temp/uniref100.fasta", filters)

if __name__ == "__main__":
    main()
