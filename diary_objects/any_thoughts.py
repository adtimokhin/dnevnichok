import re
from diary_objects.json_parsable import JSONSerializable
import validation


class AnyThoughts(JSONSerializable):

    def convert_to_json(self):
        return {
            "time": self.time,
            "description": self.description,
        }

    def __init__(self, time, description):
        # Checks for time
        if not validation.is_time_format(time):
            raise AttributeError("Time should be in format HH:mm")

        # Checks for description
        if type(description) != str:
            raise AttributeError("Description is not a string")

        self.time = time
        self.description = description
