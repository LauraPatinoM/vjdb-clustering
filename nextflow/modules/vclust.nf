process VCLUST_CLUSTER {
    /*
     * Run vclust prefilter → align → cluster (Leiden) on a FASTA.
     * Used both per-chunk and on the merged representatives.
     *
     * TODO: Implement this process.
     *   - Input:  a representative FASTA.gz
     *   - Output: clusterreps_leiden.tsv
     *   - Use params.vclust and params.threads
     *   - Clustering thresholds: --ani 0.95 --qcov 0.85
     */

    input:
    path rep_fasta

    output:
    path "clusterreps_leiden.tsv", emit: leiden_tsv

    script:
    """
    # TODO
    """
}
