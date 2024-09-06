from datetime import date
from model.entity.base import Base
from sqlalchemy import Integer, DateTime, Column, String


class Courthouse:
    def __init__(self, id, judge_name, meeting_date, room_number, crimes_reports):
        self._id = id
        self._judge_name = judge_name
        self._meeting_date = meeting_date
        self._room_number = room_number
        self._crimes_reports = crimes_reports

    def __repr__(self):
        return f"{self.__dict__}"

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_judge_name(self):
        return self._judge_name

    def set_judge_name(self, judge_name):
        if isinstance(judge_name, str):
            self._judge_name = judge_name
            return judge_name
        else:
            raise ValueError("Invalid judge name")

    def get_meeting_date(self):
        return self._meeting_date

    def set_meeting_date(self, meeting_date):
        if isinstance(meeting_date, date):
            self._meeting_date = meeting_date
            return meeting_date
        else:
            raise ValueError("Invalid meeting date")

    def get_room_number(self):
        return self._room_number

    def set_room_number(self, room_number):
        if room_number == int:
            self._room_number = room_number
            return room_number
        else:
            raise ValueError("Invalid room number")

    def get_crimes_reports(self):
        return self._crimes_reports

    def set_crimes_reports(self, crimes_reports):
        if isinstance(crimes_reports, str):
            self._crimes_reports = crimes_reports
            return self._crimes_reports
        else:
            raise ValueError("Invalid report")

    id = property(get_id, set_id)
    judge_name = property(get_judge_name, set_judge_name)
    meeting_date = property(get_meeting_date, set_meeting_date)
    room_number = property(get_room_number, set_room_number)
    crimes_reports = property(get_crimes_reports, set_crimes_reports)
