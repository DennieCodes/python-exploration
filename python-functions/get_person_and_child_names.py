class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.children = []

    def add_child(self, person):
        self.children.append(person)


def get_person_and_child_names(person):
    # child_names = []
    # for child in person.children:
    #     child_names.append({
    #         "first_name": child.first_name,
    #         "last_name": child.last_name,
    #     })

    # return {
    #     "first_name": person.first_name,
    #     "last_name": person.last_name,
    #     "children": child_names,
    # }
    # return [{"first_name" : item.first_name, "last_name" : item.last_name }for item in people]
    children = [{"first_name": child.first_name, "last_name": child.last_name } for child in person.children]

    return {
        "first_name": person.first_name,
        "last_name": person.last_name,
        "children": [{"first_name": child.first_name, "last_name": child.last_name } for child in person.children],
        }