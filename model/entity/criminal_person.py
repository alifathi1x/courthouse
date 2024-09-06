from model.entity.person import Person
from model.tools.validator import *


class Criminal_Person(Person):
    def __init__(self,id,name,family,national_id,address,crime_type):
        super().__init__(id,name,family)
        self._national_id = national_id
        self._address = address
        self._crime_type = crime_type

    def __repr__(self):
        return f"{self.__dict__}"

    def get_national_id(self):
        return self._national_id

    def set_national_id(self, national_id):
        if national_id_validator(national_id):
            self._national_id = national_id
            return True
        else:
            raise ValueError("Invalid national id")

    def get_address(self):
        return self._address

    def set_address(self, address):
        if isinstance(address, str):
            self._address = address
        else:
            raise ValueError("Invalid address")

    def get_crime_type(self):
        return self._crime_type

    def set_crime_type(self, crime_type):
        if crime_type == ["murder" or "rubbery" or "Hijack"]:
            self._crime_type = crime_type

        else:
            raise ValueError("Invalid crime type")

    national_id = property(get_national_id, set_national_id)
    address = property(get_address, set_address)
    crime_type = property(get_crime_type, set_crime_type)


criminal1 = Criminal_Person(1,"ali","mmmmm","1234567899","hughtughtughtughtug","rubbery")
print(criminal1)


