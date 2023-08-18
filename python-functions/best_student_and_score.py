'''
This year, the SAT is made up of multiple choice questions, each with three answers: A, B, or C.

Three friends, Azami, Baz, and Caris, all take the SAT on the same day. However, they didn't study and, rather, want to leave their scores up to the Fates.

Azami will fill out the answer sheet using the sequence A, B, C, A, B, C, A, B, C, ...

Baz will fill out the answer sheet using the sequence B, A, B, C, B, A, B, C, B, A, B, C, ...

Caris will fill out the answer sheet using the sequence A, A, C, C, B, B, A, A, C, C, B, B, ...

Given an answer key, which of the test takers gets the highest score and what is it?

11
SAT without studying
Given the input answer_key, determine which of the students Azami, Baz, or Caris gets the best score based on the sequences that they'll use to fill out the form.

Azami will repeat A, B, C for all of the questions
Baz will repeat B, A, B, C for all of the questions
Caris will repeat A, A, C, C, B, B for all of the questions
Constraints: 1 <= len(answer_key) <= 100

Example:

Take a look at the following input and how the students would respond:

Answer key:    A B B A A C C A C B C A A
Azami guesses: A B C A B C A B C A B C A
Baz guesses:   B A B C B A B C B A B C B
Caris guesses: A A C C B B A A C C B B A
If you tally them up, you can see that Azami got 6 right, Baz got 0 right, and Caris got 4 right. That means that you'd return 6 and "Azami".

input: an answer key of indeterminate length
output: the highest score, and corresponding name of the student

notes:


pseudocode:
1. create a list storing each student's score
2. iterate over the answer key
3. iterate char by char over each student's guess pattern, start from 0 when done
4. check if the student's answer is correct, if so then give them credit
5. compare student with highest score
6. return score and student name
'''

def best_student_and_score(answer_key):
    student_scores = [ 0,0,0 ]
    guess_count = 0
    student_name = [ "Azami", "Baz", "Caris" ]
    azami_guesses = [ 'A','B','C','A','B','C','A','B','C','A','B','C','A' ]
    baz_quesses = [ 'B','A','B','C','B','A','B','C','B','A','B','C','B' ]
    caris_guesses = [ 'A','A','C','C','B','B','A','A','C','C','B','B','A' ]

    for pos in range(len(answer_key)):
        answer = answer_key[pos]

        if guess_count == 12:
            guess_count = 0

        if azami_guesses[guess_count] == answer:
            student_scores[0] += 1
        if baz_quesses[guess_count] == answer:
            student_scores[1] += 1
        if caris_guesses[guess_count] == answer:
            student_scores[2] += 1

        guess_count += 1

    highest_score = max(student_scores)
    return highest_score, student_name[student_scores.index(highest_score)]

answerset = [
    ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C'],
    ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['C', 'C', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'C', 'C', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'C', 'C', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'C', 'C', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C', 'C', 'C', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C']
]

testset = [
    ( 33, 'Caris' ),
    ( 3, 'Caris' ),
    ( 10, 'Baz' ),
    ( 15, 'Azami' )
]

def assert_to_be_equals(actual, expected, testname):
    if actual == expected:
        print('passed')
    else:
        print(f'FAILED [{testname}].  Expected {actual}, to be {expected}')

testname = "Expected resulting student and scores to match testset"

# short run
# result = best_student_and_score(answerset[1])
# assert_to_be_equals(result, testset[1], testname)

for test in range(len(answerset)):
  result = best_student_and_score(answerset[test])
  assert_to_be_equals(result, testset[test], testname)

# print(len(['A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'A', 'C']))