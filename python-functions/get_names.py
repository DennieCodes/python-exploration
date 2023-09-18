class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


def get_names(people):
    # results = []
    # for person in people:
    #     results.append({
    #         "first_name": person.first_name,
    #         "last_name": person.last_name,
    #     })
    # return results
    return [{"first_name" : item.first_name, "last_name" : item.last_name }for item in people]