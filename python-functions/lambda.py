def greeter(greeting):
    return lambda name: f"{greeting}, {name}"

# hey = greeter("Hello")

print(greeter("Helle")("Dennie"))