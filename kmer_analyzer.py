#This is the sample code from Exam 4
import sys

#This section checks whether a DNA sequence is valid based on specified parameters before the code is run and analyzed

def validate_sequence(sequence, k):
    sequence = sequence.upper() #This allows for lowercase DNA to be counted

    if len(sequence) < k:
        return False
    for nucleotide in sequence:
        if nucleotide not  in 'ACGT':
            return False
    return True

##dictionary storing kmer and character frequencies##
def update_kmer_count(kmer_data, kmer, next_char):
    if kmer not in kmer_data:
        kmer_data[kmer] = {
	    'count': 0,
	    'next_chars': {}}
    
    kmer_data[kmer]['count'] += 1
    
    if next_char not in kmer_data[kmer]['next_chars']:
        kmer_data[kmer]['next_chars'][next_char] = 0
    kmer_data[kmer]['next_chars'][next_char] += 1

    return kmer_data

##checks the kmers and finds the character after each one then counts the frequencies##

def count_kmers_with_context(sequence, k):
    kmer_data = {}
    
    for i in range(len(sequence) - k):
        kmer = sequence[i:i+k]
        next_char = sequence[i+k]
        
        kmer_data = update_kmer_count(kmer_data, kmer, next_char)
    
    return kmer_data

##results from running test are put into an output text file##

def write_results_to_file(kmer_data, output_filename):
    sorted_kmers = sorted(kmer_data.keys())

    with open(output_filename, 'w') as f:
        for kmer in sorted_kmers:
            total_count = kmer_data[kmer]['count']
            next_chars = kmer_data[kmer]['next_chars']

            next_char_str = " ".join(
                f"{char}:{freq}"
                for char, freq in sorted(next_chars.items())
            )

            f.write(f"{kmer} {total_count} {next_char_str}\n")

def main():
    sequence_file = sys.argv[1]
    k = int(sys.argv[2])
    output_file = sys.argv[3]
    
    print(f"Reading sequences from {sequence_file}...")

    with open(sequence_file, 'r') as f:
        for sequence in f:
            sequence = sequence.strip()

            if not validate_sequence(sequence, k):
                print(f"  Warning: Skipping sequence")
                continue
            
            kmer_data = count_kmers_with_context(sequence, k) 
            
            write_results_to_file(kmer_data, output_file)

if __name__ == '__main__':
    main()
