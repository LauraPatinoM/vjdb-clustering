import random
import gzip
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

random.seed(42)

reps_file = "vjdb1_merged_reps.fna.gz"
out_file = "vjdb1_test_new_sequences.fna.gz"

records = []

# Generate 20 random sequences of varying lengths
for i in range(20):
    length = random.randint(500, 50000)
    seq = "".join(random.choices("ACGT", k=length))
    records.append(SeqRecord(Seq(seq), id=f"random_seq_{i}", description=""))

# Duplicate a few of them to test hash deduplication
for i in [3, 7, 7, 12]:
    rec = records[i]
    dup = SeqRecord(rec.seq, id=f"dup_of_{rec.id}", description="")
    records.append(dup)

# Grab top 10 sequences from existing cluster reps (should land in existing clusters)
with gzip.open(reps_file, "rt") as handle:
    for j, record in enumerate(SeqIO.parse(handle, "fasta")):
        if j >= 10:
            break
        record.id = f"existing_{record.id}"
        record.description = ""
        records.append(record)

random.shuffle(records)

with gzip.open(out_file, "wt", 2) as handle:
    SeqIO.write(records, handle, "fasta")

print(f"Wrote {len(records)} sequences to {out_file}")
print(f"  - 20 random sequences")
print(f"  - 4 duplicates (of random_seq_3, random_seq_7 x2, random_seq_12)")
print(f"  - {min(j+1, 10)} sequences from existing reps")
