from kmer_analyzer import count_kmers_with_context

def test_kmer_basic():

    result = count_kmers_with_context("ATGAT", 2)

    assert "AT" in result
    assert "TG" in result
