#Testing potential edge cases for unusual data 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kmer_analyzer import validate_sequence, count_kmers_with_context

def test_empty_sequence():
    assert validate_sequence("", 3) is False
    assert count_kmers_with_context("", 3) == {}

def test_sequence_too_short():
    assert validate_sequence("AT", 5) is False

def test_invalid_characters():
    assert validate_sequence("ATBXG", 2) is False

def test_k_equals_sequence_length():
    assert count_kmers_with_context("ATG", 3) == {}
