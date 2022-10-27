from diary_objects.json_parsable import JSONSerializable
import json


class SecurityProtocol(JSONSerializable):

    def convert_to_json(self):
        return self.items

    def __init__(self, items):
        security_points = json.load(open("security_protocol.json"))  # contains a list with all points in the list
        items = set(items)  # removing all repeating elements
        for item in items:
            if item not in security_points:
                raise AttributeError("Items listed are not in the the security protocol list")

        self.items = list(items)


