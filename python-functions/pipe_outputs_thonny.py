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

num2 = 4
steps2 = [[2, 3], [4, 7], [1], [2], [3]]

result = pipe_outputs(num2, steps2)
print(result)

# results should be 11, 12, 9