'''
Once upon a time, there was a person named Monty. He had four playing cards and no money. He decided to create a game of skill (and cheating), which would let him get some cash.

Monty put three cards on the table facedown and showed that the middle card was the Queen of Diamonds. The other person playing would give Monty a couple of dollars. Quickly, he shuffled them around, picking up a card, letting it drop elsewhere, until the viewer was confused about where the Queen was. Monty then asked, "Where's the Queen?" If the person didn't find the card, then Monty got to keep the money. Otherwise, the person playing got twice the money back from Monty!

You're going to write a function that keeps track of where the Queen is so that you can beat Monty. 😉

Given the input string swaps and that the Queen always starts in the middle, complete the function monty so that it returns where the Queen is after all of the swaps are done: left, middle, or right.

The string swaps contains the letters L, R, and O. This is what each means:

L means swap the left and middle cards
R means swap the right and middle cards
O means swap the left and right cards, the outside cards
Constraints:

0 <= swaps <= 50
swaps will have only the letters L, R, and O in it
Example:

Let's say that swaps is "LOLROL". Then, the following table shows the position of the Queen for each letter:

State	Left card	Middle card	Right card
Start		Q
L	Q
O			Q
L			Q
R		Q
O		Q
L	Q
The queen is the left card, so the function would return left.

'''
def monty(swaps):
    instruction = list(swaps)
    cards = [ "A", "Q", "A" ]
    answers = [ "left", "middle", "right" ]

    for step in instruction:
        if step == 'L':
            cards[0], cards[1] = cards[1], cards[0]
        elif step == "R":
            cards[1], cards[2] = cards[2], cards[1]
        else:
            cards[0], cards[2] = cards[2], cards[0]

    return answers[cards.index("Q")]

test = [ "1", "2"]
print(test)

test[0, 1] = test[1, 0]
print(test)
