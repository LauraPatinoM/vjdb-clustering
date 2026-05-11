process HASH_DEDUP {
    /*
     * Hash-deduplicate input sequences and split into chunks.
     * Wraps: bin/1_prepare_clustering.py
     *
     * TODO: Implement this process.
     *   - Input:  a single FASTA.gz
     *   - Output: chunked FASTA.gz files + hashed_reps CSV
     *   - The script accepts --input, --outdir, --block-size
     */

    input:
    path fasta
    val  block_size

    output:
    path "chunks/vjdb1_*.fna.gz", emit: fasta_chunks
    path "chunks/vjdb1_hashed_reps.csv", emit: hashed_csv

    script:
    """
    # TODO
    """
}
