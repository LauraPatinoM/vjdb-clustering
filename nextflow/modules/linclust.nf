process LINCLUST {
    /*
     * Run MMseqs2 linclust on a single chunk.
     * This process is called once per chunk and can run in parallel.
     *
     * TODO: Implement this process.
     *   - Input:  a single chunk FASTA.gz
     *   - Output: linclust representative FASTA.gz + cluster TSV
     *   - Use params.mmseqs and params.threads
     */

    input:
    path chunk_fasta

    output:
    path "linclust_rep_seq.fasta.gz", emit: rep_fasta
    path "linclust_cluster.tsv",      emit: cluster_tsv

    script:
    """
    # TODO
    """
}
