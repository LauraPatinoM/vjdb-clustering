# Contributing — Hackathon Guide

## Setup

1. Fork this repository and clone your fork.
2. Set up the Python environment: `bash scripts/setup_environment.sh`
3. Set tool paths:
   ```bash
   export VCLUST="python3 /path/to/vclust.py"
   ```
4. Run the test pipeline to verify your environment: `bash scripts/run_test.sh`

## Repo Structure

```
bin/           Python scripts (core logic, shared by bash and Nextflow)
scripts/       Bash reference implementation
nextflow/      Nextflow pipeline (Task 3)
test_data/     Test datasets
```

Nextflow's `bin/` convention: any executable in `bin/` at the pipeline root is automatically on `$PATH` inside Nextflow processes, so you can call `1_prepare_clustering.py --input ...` directly in your process scripts without path manipulation.

## Tasks

### Task 1 — Identify Caveats

Analyze the current workflow for edge cases and consistency issues. For each finding, **open a GitHub Issue on your fork** with:

- A clear title (e.g. "Cluster merging on update can reassign existing sequences")
- A description of the problem
- A concrete example or scenario where it matters
- Suggested severity (critical / nice-to-fix / discussion-needed)

Starting points to investigate (not exhaustive):

- What happens when a new sequence bridges two existing clusters?
- Is cluster identity stable across updates?
- Are there ordering effects (does the result depend on the sequence order in the input)?

### Task 2 — Fix and Improve

Pick issues from your Task 1 findings and implement fixes.

- Work in `bin/` for Python changes and `scripts/` if the bash orchestration needs updating.
- Create a branch: `task-2/<short-description>` (e.g. `task-2/stable-cluster-ids`)
- One branch per fix — keeps reviews manageable.
- Run `bash scripts/run_test.sh` before pushing to make sure nothing is broken.

### Task 3 — Nextflow Pipeline

Implement the pipeline in the `nextflow/` directory. A skeleton is provided with `main.nf`, `nextflow.config`, and module stubs in `nextflow/modules/`.

- Work on branch `task-3/nextflow-pipeline`.
- The skeleton defines process inputs/outputs and the DAG — you fill in the `script` blocks.
- The `main.nf` has two subworkflows (`INITIAL_CLUSTERING` and `UPDATE_CLUSTERING`) that mirror the two phases described in the README.
- Each module stub has a comment block explaining what it wraps and what the expected inputs/outputs are.
- Test with: `nextflow run nextflow/main.nf --mode update --new_seqs <test.fasta.gz> --existing_reps <reps.fna.gz> --existing_csv <reps.csv>`

## Branch Naming

| Task | Branch pattern | Example |
|------|----------------|---------|
| Task 2 fixes | `task-2/<description>` | `task-2/deterministic-hashing` |
| Task 3 pipeline | `task-3/nextflow-pipeline` | — |

## Commit Messages

Use short, descriptive messages. Prefix with the task number:

```
[task-2] Replace hash() with hashlib.md5 for deterministic dedup
[task-3] Implement LINCLUST process
```

## Before Pushing

- `bash scripts/run_test.sh` passes
- No large data files committed (check `.gitignore`)
- Changes are limited to the relevant directories (`bin/`, `scripts/`, or `nextflow/`)
