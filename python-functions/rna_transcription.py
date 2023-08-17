'''
DNA is made up of two twisted strands that encode genes using long combinations of four bases: Adenine, Cytosine, Guanine, and Thymine. The strands are complementary to one another, meaning that Adenine and Thymine are always opposite each other, and Cytosine and Guanine are always opposite each other, like this:

A double strand of DNA:

ATCAAGGCCTATTCCGGGAAAGG
TAGTTCCGGATAAGGCCCTTTCC
In order for the information in a gene to be used, it has to be transcribed into a strand of RNA. During this process, a portion of one strand of DNA is transcribed. This portion is known as the transcription unit. The start of the sequence to be transcribed is signaled by a sequence of bases known as a promoter, and the end is signaled by a sequence known as the terminator. For our purposes, the promoter is the sequence TATAAT, which begins 10 bases before the start of the transcription unit, and the terminator consists of two distinct, complementary, reversed sequences of at least length 6 that cause the RNA molecule to coil back on itself and pinch off the transcribed strand. If TATAAT appears twice on a strand, only the first occurrence counts as the promoter. An example is shown below.

AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC

In this example, the promoter and terminator sequences are boldfaced, and the transcription unit is underlined.

The first step is to find the promoter, specifically the sequence TATAAT.

Starting at the first T in the promoter, count forward 10 characters and that's where the transcription unit starts, in this case the first underlined G.

After the first letter of the transcription unit, search the remainder of the string for two sequences of letters at least six characters long that, when the first is matched up to the reverse of the second, it forms a valid double strand of DNA where A matches with T and G matches with C:

GTCATGCA
CAGTACGT  (the reverse of the second sequence)
This is the terminator.

The transcription unit is the characters including the first letter of the transcription unit found in step 2 all the way up to, but not including, the first letter of the terminator found in step 3.

The resulting RNA will be complementary to the transcription unit, except that in RNA Uracil takes the place of Thymine. Here's an example of how to turn the transcription unit into RNA:

Transcription unit: GGATTTAGATTGACCC
Complement:         CCTAAATCTAACTGGG
Replace T with U:   CCUAAAUCUAACUGGG
The final string is the RNA CCUAAAUCUAACUGGG for the gene.

Your job is to write a function that performs this calculation.

Here are some sample inputs and outputs for you to test your function as you write it. The promoter, transcription unit, and terminator are marked for each strand for you to better be able to see it.

Input:  AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC
              |-P--|    |------TU------||--T---|      |--T---|
Output: CCUAAAUCUAACUGGG

Input:  AGTCTTCAAGGGGATTCCCAGGTATATAATGCAGATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA
                                |-P--|    |----TU------||--T---|                 |--T---|
Output: UAGCGCUGCUUUAU

Input:  TATAATGGGGGAGAGACCGAGTGTTTAAGTCCCGAGGGATCGGGAGTGAGATTGAGGGAATTCCGGGAATCTCACT
        |-P--|    |------TU---------||-T--|    |-T--|
Output: CUCUCUGGCUCACAAAUUC
6
DNA transcription
Given the input string dna_strand, complete the function rna_transcription to return the RNA of the

input: a dna strand (string)
output: a rna strand (string)

rules:
A and T, C and G are always opposite each other
start of a sequence is signaled by a promoter
end of a sequence is signaled by a terminator
the promoter (TATAAT) starts 10 bases before the start of the transcription unit
if the promoter (TATAAT) appears twice on a strand only the first occurence counts
the terminator consists of two sequences of at least 6 letters.  You take the first sequence and get its
    complimentary sequence and then reverse it which makes the second sequence
the transcription is the first letter of the unit up to the first letter of the terminator

promoter: TATAAT
terminator: string of at least 6 with a following reverse complimentary set
transcription: the transcription is the first letter of the unit up to the first letter of the terminator
rna: compliment to transcription unit, except replace T with U

return rna
'''
def complimentary(str, rna):
    result = ""
    for letter in str:
        if letter == "A":
            if rna:
                result += "U"
            else:
                result += "T"
        elif letter == "T":
            result += "A"
        elif letter == "C":
            result += "G"
        elif letter == "G":
            result += "C"

    return result

def rna_transcription(dna_strand):
    promoter_pos = dna_strand.find("TATAAT")
    start_transcription = promoter_pos + 10

    # start searching for terminator after the start of the transcription
    # t is at least 6 length
    # we're looking for the compliment of t in reverse
    # where the terminator begins is where the transcription ends

    search_str = dna_strand[start_transcription:]

    # iterate over the search string
    # start adding chars from string until you have at least 6 characters
    # once you have 6 characters create a compliment of it and then reverse it
    # search ahead in the string for that reversed compliment
    # if you don't find it then add another search letter and look again
    # continue looking until reversed compliment is 1/2 len of search_str
    # add another character to search string and repeat until terminator is found

    found = False
    start = 0
    count = 6
    inf_stop = 0
    terminator = search_str[:6] # start terminator with minimum 6 characters
    dna = ""

    while not found:
        terminator = search_str[start:count] # start terminator from start to count
        str_ahead = search_str[len(terminator):] # string starting after the terminator
        term_compliment = complimentary(terminator, False)[::-1] # get reverse, complimentary string

        if not term_compliment in str_ahead: # handles if the compliment is not found
            count += 1
        else:
            dna = complimentary(search_str[:start], True)
            found = True

        if len(terminator) > len(str_ahead): # if terminator string is longer than search string
            start += 1 # restart the terminator from the next position on the search string
            count = 6 + start

        # infinite loop stopper
        inf_stop += 1
        if inf_stop >= 200:
            found = True

    return dna

dataset = [
    "TTGGTATAATAAACCAATCGATCCGCTGTGAACAGCGTCTT",
    "TATCGTTATAATAACGACTCACGACGGTGTTCATAGTCACCGTCGA",
    "TGAGACTTCTCTATAATTGCCATCAGAGCTTAATATCTACAACTTTATGCAAATTGTAAAGTTGTAGATATTAAGCTCTGAGACACTAAATAACGAGA",
    "TCTTCGGTATAATTCCCCTACAATAAAAATTTATTGTTCAGGGTC",
    "TATAATGCAGTGGTTCCCCGCGGAACATTCCGCGGGGAAACTAG"
]
#   "TTGGTATAATAAAC CAATCGATC CGCTGTGAACAGCGTCTT",
#                   CAATCGATCCGCTGT
testset = [
    'GUUAGCUAG',
    'UGAGU',
    'U',
    'GA',
    'ACC'
]

# print(complimentary("CAATCGATC", True))

result = rna_transcription(dataset[0])
print(result)