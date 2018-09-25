complimentary_nucleotides = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

class RNA:

    def __init__(self, sequence):
        self.sequence=sequence
        if not self._check_validity():
            raise ValueError("Bad RNA sequence. Sequence must contain only A, U, G, or C.")

    def __str__(self):
        return self.sequence

    def _check_validity(self):
        are_good = (nucleotide.upper() in 'GCAU' for nucleotide in self.sequence)
        return True if all(are_good) else False

    def transcribe_RNA_from_DNA(self,dna):
        return ''.join(complimentary_nucleotides[nt.upper()] for nt in dna)

import pytest

with pytest.raises(ValueError):
    RNA('ATGC')


assert RNA('ATGC') == "UACG"
