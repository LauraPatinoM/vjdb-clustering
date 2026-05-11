# VJDB Sequence Clustering

Hierarchical dereplication and clustering pipeline for the VirJenDB viral genome database, using hash deduplication, MMseqs2 linclust, and vclust (Leiden community detection).

## Dependencies

- Python 3.9+ with `biopython` and `pandas`
- [MMseqs2](https://github.com/soedinglab/MMseqs2) (v14+)
- [vclust](https://github.com/refresh-bio/vclust) (v1.3+)

## Quick Start

```bash
bash scripts/setup_environment.sh     # creates py3env/

export VCLUST="python3 /path/to/vclust.py"
export MMSEQS="/path/to/mmseqs"       # only needed for Phase 1
export THREADS=24                     # optional, defaults to 24
```

## Repo Structure

```
bin/           Python scripts (core logic)
scripts/       Bash reference implementation
nextflow/      Nextflow pipeline skeleton
test_data/     Test datasets
```

---

## Phase 1 — Initial Clustering

Clusters the full VJDB dataset from scratch. Run once to produce the baseline cluster representatives and membership CSV.

```
VJDB FASTA
  │
  ├─ 1_prepare_clustering.py ──► chunked FASTAs + hash-dedup CSV
  │
  ├─ mmseqs linclust (per chunk) ──► linclust representatives
  │
  ├─ vclust prefilter/align/cluster (per chunk)
  │        ──► Leiden clusters per chunk
  │
  ├─ 2_extract_and_merge_vclust_reps.py
  │        ──► merged representative FASTA across chunks
  │
  ├─ vclust prefilter/align/cluster (merged reps)
  │        ──► global Leiden clusters
  │
  ├─ 3_merge_clusters.py ──► vjdb1_merged_reps.csv
  │
  └─ 4_extract_reps_of_reps.py ──► vjdb1_merged_reps.fna.gz
```

```bash
bash scripts/run_initial_clustering.sh <input.fasta.gz>
```

**Outputs:** `vjdb1_merged_reps.csv` (full membership table) and `vjdb1_merged_reps.fna.gz` (cluster representative sequences).

---

## Phase 2 — Update Clustering (new sequences)

Integrates new sequences into the existing clusters without re-running from scratch. New sequences are hash-deduped, combined with existing representatives, and re-clustered with vclust.

```
New FASTA + existing reps
  │
  ├─ 5_prepare_update.py ──► combined FASTA + new_hashed_reps.csv
  │
  ├─ vclust prefilter/align/cluster (combined)
  │        ──► updated Leiden clusters
  │
  └─ 6_finalize_update.py ──► updated CSVs + updated rep FASTA
```

```bash
bash scripts/run_update_clustering.sh <new_sequences.fasta.gz> [workdir]
```

**Outputs:** `<prefix>_merged_reps.csv`, `<prefix>_new_clusters.csv`, `<prefix>_merged_reps.fna.gz`.

---

## Testing

```bash
bash scripts/run_test.sh
```

Generates 20 random sequences (with some duplicates) plus 10 from existing reps, then runs Phase 2 end-to-end.

---

## Clustering Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| linclust `--min-seq-id` | 0.95 | Pre-clustering identity threshold |
| vclust `--ani` | 0.95 | ANI threshold for Leiden clustering |
| vclust `--qcov` | 0.85 | Query coverage threshold |
| Leiden algorithm | community detection | Resolves transitive clusters |

---

## Hackathon

See [CONTRIBUTING.md](CONTRIBUTING.md) for task descriptions, branch conventions, and getting started.
