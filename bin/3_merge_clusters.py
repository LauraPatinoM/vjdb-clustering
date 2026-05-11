import glob
import os
import pandas as pd
from collections import Counter

vjdb_hashed_df = pd.read_csv("chunks/vjdb1_hashed_reps.csv", sep=",")
merged_df = pd.read_csv("chunks/vjdb1_merged/clusterreps_leiden.tsv", sep="\t")

chunk_dirs = sorted(glob.glob("chunks/vjdb1_[0-9]*/clusterreps_leiden.tsv"))
print(f"Collecting {len(chunk_dirs)} chunks")

linclust_count = 0
cluster_dicts = []
for leiden_file in chunk_dirs:
    chunk_dir = os.path.dirname(leiden_file)
    linclust_df = pd.read_csv(os.path.join(chunk_dir, "linclust_cluster.tsv"), sep="\t", names=["cluster", "object"])
    linclust_count += len(Counter(linclust_df["cluster"]))
    vclust_df = pd.read_csv(leiden_file, sep="\t")
    vclust_dict = {row.object: row.cluster for row in vclust_df.itertuples()}
    cluster_dicts.append({row.object: vclust_dict[row.cluster] for row in linclust_df.itertuples()})

merged_dict = {row.object: row.cluster for row in merged_df.itertuples()}
vclust_dict = {}
for d in cluster_dicts:
    vclust_dict |= d

print("Mapping to final clusters")
final_clusters = [""] * len(vjdb_hashed_df)
cant_map = []
cant_map_merged = []
for i, row in enumerate(vjdb_hashed_df.itertuples()):
    if row.copy_of in vclust_dict:
        a = vclust_dict[row.copy_of]
        if a in merged_dict:
            final_clusters[i] = merged_dict[a]
        else:
            final_clusters[i] = a
            cant_map_merged.append(a)
    else:
        cant_map.append(row.copy_of)
        final_clusters[i] = row.copy_of

print("cant map merged:", Counter(cant_map_merged).most_common(10))
print("cant map:", Counter(cant_map).most_common(10))

all_count = len(vjdb_hashed_df)
hash_count = len(Counter(vjdb_hashed_df["copy_of"]))
vclust_count = len(merged_df)
merged_count = len(Counter(merged_df["cluster"]))

print(f"all: {all_count}, hashed: {hash_count}, linclust: {linclust_count}, vclust: {vclust_count}, merged: {merged_count}")

vjdb_hashed_df["cluster_rep"] = final_clusters
vjdb_hashed_df.to_csv("vjdb1_merged_reps.csv", index=False)
