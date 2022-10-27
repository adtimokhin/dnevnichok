from datetime import date
import json
from diary_objects.security_protocol import SecurityProtocol

"""
Returns today's date in format dd-mm-YY
"""
DEFAULT_TODAY_FORMATTED = date.today().strftime("%d-%m-%Y")


def create_empty_diary_file():
    """
    Creates an empty json file (with prefilled fields) that will
    store data about the current day.

    The JSON structure is as follows:
    {
        "date":"dd/mm/YY",
        "emotional_happiness": 0-10,
        "security_protocol": [str],
        "thoughts":[{"time":"HH:mm" , "description": ""}],
        "things_done":[{
                    "time":"HH:mm",
                    "description":"",
                    "oddness": 0-10
        }]

    }
    :return: None
    """

    # We do not want to overwrite data that is stored in a file
    if diary_file_exists():
        raise FileExistsError

    today_json_formatted = date.today().strftime("%d/%m/%Y")
    today_file_name_formatted = DEFAULT_TODAY_FORMATTED

    empty_diary_entry = {
        "date": f"{today_json_formatted}",
        "emotional_happiness": -1,
        "security_protocol": [],
        "thoughts": [],
        "things_done": []
    }

    json_object = json.dumps(empty_diary_entry, indent=len(empty_diary_entry))
    with open(f"{today_file_name_formatted}.json", "w") as f:
        f.write(json_object)


def diary_file_exists(diary_date=DEFAULT_TODAY_FORMATTED):
    """
    Checks whether diary file for a given date exists in
    a directory that stores all the files.

    :param diary_date: (str) in format dd-mm-YY representing the day of the dairy entry
    :return: True is the file exists, else false. (bool)
    """
    try:
        open(f"{diary_date}.json", "r")
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False


def read_file_json_data(diary_date=DEFAULT_TODAY_FORMATTED):
    """
    Returns contents of a JSON file by its date of creation.
    If the file does not exist it will either create it (if the
    diary_date is set for today), else will raise an error.

    :param diary_date: date in format: dd-mm-YY (str)
    :return: JSON object converted to python dictionary (dict)
    """
    if not diary_file_exists(diary_date):
        if DEFAULT_TODAY_FORMATTED.__eq__(diary_date):
            # We can create the file
            create_empty_diary_file()
        else:
            # Else we need to raise an error
            raise FileNotFoundError

    with open(f"{diary_date}.json", "r") as f:
        data = json.load(f)
    return data


def __write_file_json_data(diary_date, json_object):
    """
    Rewrites a JSON file (located by diary_date) to the data passed as json_object.
    Do not call this method outside the module.

    :param diary_date: date in format: dd-mm-YY (str)
    :param json_object: dictionary that mimic the JSON structure (dict)
    :return: None
    """
    json_object_to_save = json.dumps(json_object, indent=len(json_object), ensure_ascii=False)
    with open(f"{diary_date}.json", "w", encoding="utf8") as f:
        f.write(json_object_to_save)


def set_attribute(attribute_name, value, diary_date=DEFAULT_TODAY_FORMATTED):
    """
    Updates the value for the given date of the attributes
    that are allowed to be updated.
    Also validates that the values passed and the
    attribute_name are within the given range of allowed values.

    :param attribute_name: name of the attribute that is present in JSON file (str)
    :param value: value in the allowed rage (int)
    :param diary_date: date in format: dd-mm-YY (str)
    :return: None
    """

    limits_for_allowed_properties = {
        "emotional_happiness": (0, 10)
    }

    try:
        lowest, biggest = limits_for_allowed_properties[attribute_name]
        if lowest > value or biggest < value:
            raise AttributeError("Attribute out of bound")
    except KeyError:
        raise AttributeError("Unknown attribute name")

    updated_json_data = read_file_json_data(diary_date)

    updated_json_data[attribute_name] = value

    __write_file_json_data(diary_date, updated_json_data)


def update_attribute(attribute_name, value, diary_date=DEFAULT_TODAY_FORMATTED):
    """
    Updates the value for the given date of the attributes
    that are allowed to be updated. This method is called
    on the attributes that are in form of lists
    Also validates that the values passed and the
    attribute_name are within the given range of allowed values.

    :param attribute_name: name of the attribute that is present in JSON file (str)
    :param value: an object from the /diary_objects folder (obj)
    :param diary_date: date in format: dd-mm-YY (str)
    :return: None
    """

    # Checking that this attribute exists and allowed to be modified in this way
    allowed_attribute_names = ["things_done", "thoughts"]
    if attribute_name not in allowed_attribute_names:
        raise Exception("You cannot change this property")

    updated_json_data = read_file_json_data(diary_date)

    updated_json_data[attribute_name].append(value.convert_to_json())

    __write_file_json_data(diary_date, updated_json_data)


def update_attribute_security_protocol(value, diary_date=DEFAULT_TODAY_FORMATTED):
    """
    Updates values for the security_protocol attribute in
    JSON file. Values in the value attribute should contain only
    new unique elements that will be appended to the already
    existing security_protocol

    :param value: SecurityProtocol object from
                  /diary_objects directory (obj)
    :param diary_date: date in format: dd-mm-YY (str)
    :return: None
    """
    updated_json_data = read_file_json_data(diary_date)

    old_list = updated_json_data["security_protocol"]
    new_list = value.convert_to_json()
    new_protocol = SecurityProtocol(old_list + new_list)

    updated_json_data["security_protocol"] = new_protocol.convert_to_json()

    __write_file_json_data(diary_date, updated_json_data)
