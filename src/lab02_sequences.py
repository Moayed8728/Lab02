"""Lab 2 - biological sequences as strings (becomes sequence_utils.py in Week 5)."""

DNA_BASES = frozenset("ACGT")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    result = ""

    for letter in raw:
        if letter.isalpha():
            result = result + letter.upper()

    return result


def is_valid_dna(seq: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (and N when allowed)."""
    if seq == "":
        return False

    seq = seq.upper()

    if allow_n:
        valid_bases = "ACGTN"

    else:
        valid_bases = "ACGT"


    for letter in seq:
        if letter not in valid_bases:
            return False

    return True


def gc_content(seq: str) -> float:
    """Return GC percentage (0-100); ValueError if empty or not A/C/G/T."""
    seq = seq.upper()

    if seq == "":
        raise ValueError("sequence cannot be empty")

    total = 0

    for letter in seq:
        if letter not in "ACGT":
            raise ValueError("invalid DNA sequence")

    

        if letter == "C" or letter == "G":  
         total+= 1

    return ((total * 100) / len(seq))



def transcribe(dna: str) -> str:
    """Return the RNA copy of a DNA sequence (T becomes U)."""
    dna = dna.upper()

    for letter in dna:
        if letter not in "ACGT":
            raise ValueError("invalid DNA sequence")

    rna = ""

    for letter in dna:
        if letter == "T":
            rna = rna + "U"

        else:
            rna = rna + letter

    return rna


def find_motif(seq: str, motif: str) -> list[int]:
    """Return every 0-based start of motif in seq (overlaps allowed)."""
    seq = seq.upper()
    motif = motif.upper()

    if motif == "":
        raise ValueError("motif cannot be empty")

    positions = []
    start = 0

    while True:
        position = seq.find(motif, start)

        if position == -1:
            break

        positions.append(position)
        start = position + 1

    return positions
