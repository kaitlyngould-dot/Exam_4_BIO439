from kmer_analyzer import validate_sequence

def test_valid_sequence():
	assert validate_sequence("ATGC", 2) is True

def test_too_short():
	assert validate_sequence("AT", 3) is False

def test_invalid_chars():
	assert validate_sequence("ATXB", 2) is False
