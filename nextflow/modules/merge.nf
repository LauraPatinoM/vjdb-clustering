process EXTRACT_MERGE_CHUNK_REPS {
    /*
     * Collect Leiden cluster reps from all chunks into a single FASTA.
     * Wraps: bin/2_extract_and_merge_vclust_reps.py
     *
     * TODO: Implement this process.
     */

    input:
    path leiden_tsvs   // collected from all chunks
    path rep_fastas    // collected from all chunks

    output:
    path "vjdb1_vclust_reps_merged.fna.gz"

    script:
    """
    # TODO
    """
}

process MERGE_FINAL_CLUSTERS {
    /*
     * Map all sequences through the clustering hierarchy to final cluster IDs.
     * Wraps: bin/3_merge_clusters.py
     *
     * TODO: Implement this process.
     */

    input:
    path hashed_csv
    path merged_leiden_tsv
    path chunk_leiden_tsvs   // collected
    path chunk_linclust_tsvs // collected

    output:
    path "vjdb1_merged_reps.csv"

    script:
    """
    # TODO
    """
}

process EXTRACT_REPS_OF_REPS {
    /*
     * Extract final representative sequences from the merged FASTA.
     * Wraps: bin/4_extract_reps_of_reps.py
     *
     * TODO: Implement this process.
     */

    input:
    path merged_fasta
    path leiden_tsv

    output:
    path "vjdb1_merged_reps.fna.gz"

    script:
    """
    # TODO
    """
}

process PREPARE_UPDATE {
    /*
     * Hash-dedup new sequences and combine with existing reps.
     * Wraps: bin/5_prepare_update.py
     *
     * TODO: Implement this process.
     */

    input:
    path new_seqs
    path existing_reps

    output:
    path "combined_for_vclust.fna.gz", emit: combined_fasta
    path "new_hashed_reps.csv",        emit: hashed_csv

    script:
    """
    # TODO
    """
}

process FINALIZE_UPDATE {
    /*
     * Remap clusters after update, produce final CSVs and rep FASTA.
     * Wraps: bin/6_finalize_update.py
     *
     * TODO: Implement this process.
     */

    input:
    path leiden_tsv
    path new_hashed_csv
    path existing_csv
    path combined_fasta

    output:
    path "*_merged_reps.csv",  emit: merged_csv
    path "*_merged_reps.fna.gz", emit: rep_fasta

    script:
    """
    # TODO
    """
}
