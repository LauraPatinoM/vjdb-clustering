import glob
import os, gzip
import pandas as pd
from Bio import SeqIO

path = "chunks"
out_file = os.path.join(path, "vjdb1_vclust_reps_merged.fna.gz")

chunk_dirs = sorted(glob.glob(os.path.join(path, "vjdb1_[0-9]*", "clusterreps_leiden.tsv")))
print(f"Found {len(chunk_dirs)} chunks")

with gzip.open(out_file, "wt", 2) as out_handle:
    for leiden_file in chunk_dirs:
        chunk_dir = os.path.dirname(leiden_file)
        chunk_name = os.path.basename(chunk_dir)
        clusters = set(pd.read_csv(leiden_file, sep="\t", dtype=str)["cluster"])
        print(f"{chunk_name}: {len(clusters)} clusters")
        in_file = os.path.join(chunk_dir, "linclust_rep_seq.fasta.gz")
        with gzip.open(in_file, "rt") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                if record.id in clusters:
                    out_handle.write(record.format("fasta"))
