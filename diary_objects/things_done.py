import re
from diary_objects.json_parsable import JSONSerializable


class ThingsDone(JSONSerializable):

    def convert_to_json(self):
        return {
            "time": self.time,
            "description": self.description,
            "oddness": self.oddness
        }

    def __init__(self, time, description, oddness):
        # Checks for time
        if type(time) != str:
            raise AttributeError("Time is not a string")

        if time != re.match("^[0-9]{2}:[0-9]{2}", time).group():
            raise AttributeError("Time should be in format HH:mm")

        # Checks for description
        if type(description) != str:
            raise AttributeError("Description is not a string")

        # Checks for oddness
        if type(oddness) != int:
            raise AttributeError("Oddness is not an integer")
        if oddness < 0 or oddness > 10:
            raise AttributeError("Oddness should be in range of 0-10 inclusively")

        self.time = time
        self.description = description
        self.oddness = oddness
