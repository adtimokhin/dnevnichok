import json
import os
from datetime import date

"""
Returns today's date in format dd-mm-YY
"""
DEFAULT_TODAY_FORMATTED = date.today().strftime("%d-%m-%Y")
FILES_DIRECTORY = "./data/"


def diary_file_exists(diary_date=DEFAULT_TODAY_FORMATTED):
    """
    Checks whether diary file for a given date exists in
    a directory that stores all the files.

    :param diary_date: (str) in format dd-mm-YY representing the day of the dairy entry
    :return: True is the file exists, else false. (bool)
    """
    try:
        open(f"{FILES_DIRECTORY}{diary_date}.json", "r")
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
        raise FileNotFoundError

    with open(f"{FILES_DIRECTORY}{diary_date}.json", "r") as f:
        data = json.load(f)
    return data


def get_all_files():
    """
    Makes a list of dictionaries containing all relevant information
    about the existing diary files

    :return: a list of dictionaries in format [{"date":"dd-mm-YY"}]
    """
    all_files = os.listdir(FILES_DIRECTORY)
    file_names = []
    for file in all_files:
        file_names.append({"date": file[0:10:]})
    return file_names
