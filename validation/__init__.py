import re


def is_time_format(string):
    """
    Checks that the string entered follows format:
    HH:mm

    :param string: string to check (str)
    :return: Boolean
    """
    try:
        return string == re.match("^[0-9]{2}:[0-9]{2}", string).group()
    except AttributeError:
        return False


def is_json_date_format(string):
    """
    Checks that the string entered follows format:
    dd-mm-YY

    :param string: string to check (str)
    :return: Boolean
    """

    try:
        return string == re.match("^[0-9]{2}-[0-9]{2}-[0-9]{4}", string).group()
    except AttributeError:
        return False
