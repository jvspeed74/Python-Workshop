class Utils:
    """
    This class contains utility/helper functions.
    """
    
    @staticmethod
    def print_header(text=None, decor="=", width=50) -> None:
        """
        Prints a header to the console with a given text inside
        :param text: Optional var to use for the text inside the header.
        :param decor: Optional str to replace "=" with a custom item
        :param width: Optional int to set the width of the header.
        """
        
        # Print header without text.
        if text is None:
            print(decor * width)
            return
        
        # Declare header margins.
        padding: int = (width - len(text)) // 2
        
        # Print header with text.
        print(decor * padding, text, decor * padding)


def encode_protein(rna_sequence, print_length=False, print_common_codon=False) -> str:
    """
    Translates an RNA sequence into a protein sequence using a codon table.

    :param string rna_sequence: The input RNA sequence (a string).
    :param bool print_length: If True, prints the length of the encoded protein.
    :param bool print_common_codon: If True, prints the most commonly occurring codon.
    :return: The protein sequence.
    """
    # Handle invalid arguments
    if type(rna_sequence) is not str:
        raise TypeError(f"Invalid argument type {rna_sequence} Received {type(rna_sequence)}; expected str")
    elif type(print_length) is not bool:
        raise TypeError(f"Invalid argument type {print_length}. Received {type(print_length)}; expected bool")
    elif type(print_common_codon) is not bool:
        raise TypeError(f"Invalid argument type {print_common_codon}. "
                        f"Received {type(print_common_codon)}; expected bool")
    
    # Store Amino-acid:[codons] as key, value pair
    codon_table = {
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
        "Isoleucine": ["AUU", "AUC", "AUA"],
        "Methionine": ["AUG"],
        "Valine": ["GUU", "GUC", "GUA", "GUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
        "Proline": ["CCU", "CCC", "CCA", "CCG"],
        "Threonine": ["ACU", "ACC", "ACA", "ACG"],
        "Alanine": ["GCU", "GCC", "GCA", "GCG"],
        "Tyrosine": ["UAU", "UAC"],
        "Stop": ["UAA", "UAG", "UGA"],
        "Histidine": ["CAU", "CAC"],
        "Glutamine": ["CAA", "CAG"],
        "Asparagine": ["AAU", "AAC"],
        "Lysine": ["AAA", "AAG"],
        "Aspartic acid": ["GAU", "GAC"],
        "Glutamic acid": ["GAA", "GAG"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
        "Arginine": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
        "Glycine": ["GGU", "GGC", "GGA", "GGG"]
    }
    protein_sequence = []  # Stores the protein sequence
    codon_counts = {}  # Keeps track of codon occurrences
    
    # Process the RNA sequence into chucks of 3
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i + 3]
        if len(codon) == 3:
            # Check if codon matches any defined in the codon_table
            for protein, codons in codon_table.items():
                # Append to sequence and update occurrence count
                if codon in codons:
                    protein_sequence.append(protein)
                    codon_counts[codon] = codon_counts.get(codon, 0) + 1
                    break
    
    # Optional param to print length of protein
    if print_length:
        print("Length of encoded protein:", len(protein_sequence))
    
    # Optional param to print most common codon
    if print_common_codon:
        most_common_codon = max(codon_counts, key=codon_counts.get)
        print("Most commonly occurring codon:", most_common_codon)
    
    # Send result
    return ", ".join(protein_sequence)


def main():
    test_cases = [
        "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGT",
        """AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGT
GGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCG
TGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGC
CTGTCTCCCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTG
GCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAG
CTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCT
GCAGGGTGAGCCAACTGCCCATTGCTGCCCCTGGCCGCCCCCAGCCACCCCCTGCTCCTGGCGCTCCCAC
CCAGCATGGGCAGAAGGGGGCAGGAGGCTGCCACCCAGCAGGGGGTCAGGTGCACTTTTTTAAAAAGAAG
TTCTCTTGGTCACGTCCTAAAAGTGACCAGCTCCCTGTGGCCCAGTCAGAATCTCAGCCTGAGGACGGTG
TTGGCTTCGGCAGCCCCGAGATACATCAGAGGGTGGGCACGCTCCTCCCTCCACTCGCCCCTCAAACAAA
TGCCCCGCAGCCCATTTCTCCACCCTCATTTGATGACCGCAGATTCAAGTGTTTTGTTAAGTAAAGTCCT
GGGTGACCTGGGGTCACAGGGTGCCCCACGCTGCCTGCCTCTGGGCGAACACCCCATCACGCCCGGAGGA
GGGCGTGGCTGCCTGCCTGAGTGGGCCAGACCCCTGTCGCCAGGCCTCACGGCAGCTCCATAGTCAGGAG
ATGGGGAAGATGCTGGGGACAGGCCCTGGGGAGAAGTACTGGGATCACCTGTTCAGGCTCCCACTGTGAC
GCTGCCCCGGGGCGGGGGAAGGAGGTGGGACATGTGGGCGTTGGGGCCTGTAGGTCCACACCCAGTGTGG
GTGACCCTCCCTCTAACCTGGGTCCAGCCCGGCTGGAGATGGGTGGGAGTGCGACCTAGGGCTGGCGGGC
AGGCGGGCACTGTGTCTCCCTGACTGTGTCCTCCTGTGTCCCTCTGCCTCGCCGCTGTTCCGGAACCTGC
TCTGCGCGGCACGTCCTGGCAGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGC
CCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCT
CTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACC""",
        "GAGAGAGATGGAATAAAGCCCTTGAACCAGC"
    ]
    
    # Iterate over each test case and print result
    for test_num, rna_seq in enumerate(test_cases):
        Utils.print_header(f"Test {test_num + 1}: ")
        print(f"Encoded Protein: {encode_protein(rna_seq, print_length=True, print_common_codon=True)}")
    else:
        Utils.print_header("All Tests Complete")


main()
