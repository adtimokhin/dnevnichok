from abc import ABC, abstractmethod


class JSONSerializable(ABC):
    @abstractmethod
    def convert_to_json(self):
        """
        Converts the object into a dictionary that can be serialized.
        :return: dictionary that imitates JSON object
        """
        pass
