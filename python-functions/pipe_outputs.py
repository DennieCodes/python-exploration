'''
One day, Rube Goldberg  was asked to design the drain pipes for an apartment building. He did so with his usual creativity. Then, rather than turning in a diagram to his benefactors, he gave them some lists of numbers.

"The first number", he said, "is the number of apartments in the building. Each can handle eight gallons of water per minute. The rest of the numbers are when pipes split or combine."

"If you see one number," he continued, "then that pipe joins the pipe to its right.

"If you see two numbers, then the first number is the number of the pipe splits into two pipes. The second number is how much of the flow goes into the left pipe. The remainder will go into the second pipe.

"After each step, the pipes are renumbered."

He draws a little sketch for an example. (To see a large image, right-click on the drawing and choose "Open Image in New Tab".)

pipes

The architects love it so much that they ask Goldberg to design the pipes for all of their buildings. They ask you to write a program to calculate the final flows from the number of drains and the different splits and joins that Goldberg will provide you.

3
Drain pipes
Given the number of pipes num_pipes and a list of steps, complete the function pipe_outputs to return a list that contains the flow of each pipe in the order starting with the first pipe to the last pipe.

At the beginning, each of the num_pipes has a flow of 8
In the list of steps, each step is a list
If the step has one value in it, then it joins that pipe with the one to its right
If the step has two values in it, then the first value is the pipe to split, and the second value is the flow that goes into the pipe to the left, while the remainder of the flow goes into the pipe to the right
The input from the example above would look like this:

num_pipes = 3
steps = [[2, 4], [1], [1], [1, 2]]

input: number of pipes, list of lists indication steps
output: a list that contains the flow of each pipe from 1st to last pipe

single number: merge the value of the pipe provided with the one to the right of it
double number: first # indicates which pipe that you're going to split, the second number is the amount of flow
               from that pipe that will go to the left, the rest goes to the right

'''

def pipe_outputs(num_pipes, steps):
    pipes = [8 for num in range(num_pipes)] # create a list of pipes with default value of 8

    for step in steps: # iterate over each step
        if len(step) == 1: # step[0] refers to pipes[step[0]]
            pos = step[0]-1
            pipes[pos] = pipes[pos] + pipes[pos+1] # merge value of both pipes
            pipes.pop(pos+1) # remove pipe to the right
        elif len(step) == 2: # remember step here has two values so # of pipe is step[0]
            pos = step[0]-1
            left_flow = step[1]
            current_value = pipes[pos] # get value of pipe
            pipes[pos] = current_value - left_flow # put remaining difference into current pipe
            pipes.insert(pos, left_flow) # insert value of step[1] into new list entry
    return pipes

num1 = 1
steps1 = [[1, 4], [2, 2], [1, 2]]
num2 = 4
steps2 = [[2, 3], [4, 7], [1], [2], [3]]
num3 = 3
steps3 = [[2], [1]]

result = pipe_outputs(num2, steps2)
print(result)

# results should be 11, 12, 9