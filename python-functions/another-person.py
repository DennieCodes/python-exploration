import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_to_json(person):
    # If the person is None
    if person is None:
        return json.dump(None)

        # return the JSON-formatted version of None

    # Create a dictionary from the Person instance
    d = {
        "name": person.name,
        "age": person.age,
    }
    # Pass the d variable to json.dumps on the
    # right-hand side of the assignment operator =
    result = json.dumps(d)
    # Return the value of result as the last line

    return d  # Delete this pass when you're done