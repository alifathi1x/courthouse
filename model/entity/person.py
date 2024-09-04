# noinspection PyTypeChecker
class Person:
    def __init__(self, id, name, family):
        self.id = id
        self._name = name
        self._family = family

    def __repr__(self):
        return f"Person(id: {self.id}, name: {self.name}, family: {self.family})"

    def get_id(self):
        return self._id

    def set_id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            raise ValueError("Invalid id type")

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Invalid Name")

    def get_family(self):
        return self._family

    def set_family(self, family):
        if family == str:
            self._family = family
        else:
            raise ValueError("Invalid Family")

    # noinspection PyTypeChecker
    id = property(get_id, set_id)
    # noinspection PyTypeChecker
    name = property(get_name, set_name)
    # noinspection PyTypeChecker
    family = property(get_family, set_family)



