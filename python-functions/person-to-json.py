import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_to_json(person):
    # If the person is None, then return the JSON-formatted
    # version of None
    if person is None:
        # Finish this return statement with json.dumps(None)
        return json.dump(None)

    # Create a dictionary from the Person instance
    d = {
        "name":  person.name,  # Put person.name before the comma
        "age":   person.age,  # Put person.age before the comma
    }

    # Pass the d variable to json.dumps on the
    # right-hand side of the assignment operator =
    result = json.dumps(d)

    # Return the value of result as the last line
    return d