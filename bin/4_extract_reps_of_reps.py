from Bio import SeqIO
import os, gzip, sys
import pandas as pd

in_file = os.path.join("chunks", "vjdb1_vclust_reps_merged.fna.gz")
out_file = "vjdb1_merged_reps.fna.gz"
clusters = set(pd.read_csv(os.path.join("chunks", "vjdb1_merged", "clusterreps_leiden.tsv"), sep="\t", dtype=str)["cluster"])

with gzip.open(out_file, "wt", 2) as out_handle:
    with gzip.open(in_file, "rt") as handle:
        for i, record in enumerate(SeqIO.parse(handle, "fasta")):
            if record.id in clusters:
                out_handle.write(record.format("fasta"))
