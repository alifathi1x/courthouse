from model.entity.person import Person


class Lawyer_Info(Person):
    def __init__(self, id, name, family, lawyer_license, lawyer_number):
        super().__init__(id, name, family)
        self._lawyer_license = lawyer_license
        self._lawyer_number = lawyer_number

    def __repr__(self):
        return f"{self.__dict__}"

    def get_lawyer_license(self):
        return self._lawyer_license

    def set_lawyer_license(self, lawyer_license):
        if isinstance(lawyer_license, bool):
            self._lawyer_license = lawyer_license
            return True
        else:
            raise ValueError("Invalid lawyer license")

    def get_lawyer_number(self):
        return self._lawyer_number

    def set_lawyer_number(self, lawyer_number):
        if isinstance(lawyer_number, int):
            self._lawyer_number = lawyer_number
            return True
        else:
            raise ValueError("Invalid lawyer number")

    lawyer_number = property(get_lawyer_number, set_lawyer_number)
    lawyer_license = property(get_lawyer_license, set_lawyer_license)


lawyer1 = Lawyer_Info(1, "ali", "mamam", True, 1234555555)
print(lawyer1)
