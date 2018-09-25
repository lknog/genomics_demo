# genomics_demo_workshop

This is a demo of a genomics python workshop

## Installation

````
pip install git+https://github.com/lknog/dna
````

## Usage

````python
from genomics_demo import DNA
dna_strand = DNA('AATTCG') # make DNA strand
dna_strand.complementary_sequence # get matching strand
````
