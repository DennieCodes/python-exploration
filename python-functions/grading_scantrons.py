'''
Then, there's the ubiquitous Scantron  form. As much as it may plague your nightmares, you've decided to take on a contract from the company that makes them.

It seems they need an update to their software. The old code had a small bug in it, and they need you to write new code that doesn't have a bug in it.

5
Grading Scantrons
Given two strings, submission and answer_key, complete the function grade_scantron to compare the two strings and return the number of correct answers the student received in their submission based on the value of the answer_key.

A correct answer occurs when the characters in both the submission and the answer_key at the same position are the same letters.

Constraints:

submission and answer_key will be the same length
answer_key will contain only the letters "A", "B", "C", "D", or "E"
submission will contain only the characters "A", "B", "C", "D", "E", or a space " "
0 <= answer_key <= 10000
Example:

Let's say your function receives the following two values. The student didn't study and just answered "E", but missed one spot.

submission: EEEEEEEEEEEE EEEEEEEEEEEE
answer_key: CEEACEABABBDCDABDBEDCAEDC
matches:     ★★  ★            ★   ★
The submission and answer_key match in five places, so your function grade_scantron will return 5.
'''
def grade_scantron(submission, answer_key):
    combined = tuple(zip(submission, answer_key))

    return len(list(filter(lambda item: item[0] == item[1], combined)))

submission = "EEEEEEEEEEEE EEEEEEEEEEEE"
answer_key = "CEEACEABABBDCDABDBEDCAEDC"

result = grade_scantron(submission, answer_key)
print(result)
