'''
One day, Rube Goldberg was asked to design the drain pipes for an apartment building. He did so with his usual creativity. Then, rather than turning in a diagram to his benefactors, he gave them some lists of numbers.

"The first number", he said, "is the number of apartments in the building. Each can handle eight gallons of water per minute. The rest of the numbers are when pipes split or combine."

"If you see one number," he continued, "then that pipe joins the pipe to its right.

"If you see two numbers, then the first number is the number of the pipe splits into two pipes. The second number is how much of the flow goes into the left pipe. The remainder will go into the second pipe.

"After each step, the pipes are renumbered."

He draws a little sketch for an example. (To see a large image, right-click on the drawing and choose "Open Image in New Tab".)

pipes

The architects love it so much that they ask Goldberg to design the pipes for all of their buildings. They ask you to write a program to calculate the final flows from the number of drains and the different splits and joins that Goldberg will provide you.

1
Drain pipes
1 PT

Given the number of pipes num_pipes and a list of steps, complete the function pipe_outputs to return a list that contains the flow of each pipe in the order starting with the first pipe to the last pipe.

At the beginning, each of the num_pipes has a flow of 8
In the list of steps, each step is a list
If the step has one value in it, then it joins that pipe with the one to its right
If the step has two values in it, then the first value is the pipe to split, and the second value is the flow that goes into the pipe to the left, while the remainder of the flow goes into the pipe to the right
The input from the example above would look like this:

num_pipes = 3
steps = [[2, 4], [1], [1], [1, 2]]

input:
  num of pipes in the apartment, each can handle 8 gallons of water per minute

  list of lists
    if list has one number then it joins the pipe to the right
    if list has two numbers then:
      the first number is the number of the pipe that splits into two pipes
      the second is how much water flows into the left pipe
      the rest will flow into the right pipe
    after each step, the pipes are renumbered

output: a list of the pipe with their flow
'''
data = [[2, 4], [1], [1], [1, 2]]
num_pipes = 3


def pipe_outputs(num_pipes, steps):
    pipes = [8 for num in range(0, num_pipes)]

    for step in steps:
        if len(step) == 2:
            split_pipe = step[0] - 1
            new_pipe = step[0]
            left_flow = step[1]
            # two numbers [#,#]
            # first is index of pipe
            value_of_split_pipe = pipes[split_pipe]
            value_of_new_pipe = value_of_split_pipe - left_flow
            # that pipe will split into two
            pipes.insert(new_pipe, value_of_new_pipe)
            # the second number will be flow to left
            pipes[split_pipe] = left_flow
            # the rest will flow right
        else:
            # join pipe to one to the right
            pipe_num = step[0]
            joined = pipes[pipe_num-1] + pipes[pipe_num]
            pipes[pipe_num-1] = joined
            pipes.pop(pipe_num)

    return pipes


result = pipe_outputs(num_pipes, data)

print(result)