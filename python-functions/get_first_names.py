class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


def get_first_names(people):
    # results = []
    # for person in people:
    #     results.append(person.first_name)
    # return results
    return [item.first_name for item in people]