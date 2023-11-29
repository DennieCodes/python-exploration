'''

Today, Caris is learning all about circles and squares at school! Unfortunately, Caris is a llama and doesn't have a very good sense of size. As his best friend, you've been tasked with helping them determine the larger shape (it's guaranteed that one is larger than the other).

Complete the function that accepts two parameters, s and r, where s is the length of the side of a square and r is the length of the radius of a circle. Given the values r and s, return the string "SQUARE" if the square has the larger area and return the string "CIRCLE" if the circle has the larger area.

The area of a square is calculated as s * s.
The area of a circle is calculated as math.pi * r * r
s	r	Output
6	2	"SQUARE"
12	124	"CIRCLE"
Don't forget to import any modules that you may need to solve this problem.

input: s = lenght of side of square, r = length of radius of a circle
output: return "SQUARE" if it's larger or "CIRCLE" if it has larger area

'''

def find_larger_area(s, r):
    circle_area = (r * r) * 3.142
    square = s * s

    if square > circle_area:
        return "SQUARE"
    return "CIRCLE"


result = find_larger_area(s, r)

print(result)