from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

import validation
from file_write import DEFAULT_TODAY_FORMATTED, DEFAULT_TIME_NOW_FORMATTED
import file_read as fr
import file_write as fw

import json

from diary_objects.things_done import ThingsDone
from diary_objects.any_thoughts import AnyThoughts
from diary_objects.security_protocol import SecurityProtocol

console = Console()

EXIT_COMMAND = "exit"
HELP_COMMAND = "help"


def welcome_message():
    """
    Prints out welcome message to the console.
    :return: None
    """

    console.print("Dnevnichok v0.1", style="bold on dark_orange3 underline", justify="center")
    console.print(
        "[bold]Welcome! Here you can write anything you want to write about your day."
        "\nThat is a digital diary of a sort.[/bold]", justify="center")

    console.print("Here is what you can do:")
    console.print("1) See what you already have written")
    console.print("2) Write something down")
    console.print("3) Ask for help")
    console.print("To select an option write a number from 1 to 3")
    console.print(f"To get help at any point write [bold]{HELP_COMMAND}[/bold]")
    console.print(f"To exit the program just write [bold]{EXIT_COMMAND}[/bold]")
    console.print()


def parse_input():
    """
    Catches user's input. Determines to what command it corresponds
    and then calls an appropriate carry method

    :return: None
    """
    user_input = ""
    while user_input != EXIT_COMMAND:
        user_input = console.input("[green]>>[/green] ")
        if user_input == HELP_COMMAND:
            help_message()
        elif user_input == "1":
            print_table("Available Diary entries:", ["date"], fr.get_all_files())
            console.print("Enter date that you want to check. You can't escape now")
            file_name_date = select_json_file()
            print_json_file_data_description(file_name_date)
        elif user_input == "2":
            file_name_date = select_json_file()
            file_exists = print_json_file_data_description(file_name_date)
            if file_exists:
                modifiable_fields = ["emotional_happiness", "security_protocol", "thoughts", "things_done"]
                field_to_modify_index = get_acceptable_input(modifiable_fields)
                if field_to_modify_index == 0:
                    value = get_integer_value(0, 10)
                    fw.set_attribute(modifiable_fields[field_to_modify_index], value, file_name_date)
                    console.print("[green]Success![/green]")
                elif field_to_modify_index == 1:
                    security_points = json.load(
                        open("security_protocol.json"))  # contains a list with all points in the list
                    security_protocol_indexes = get_acceptable_inputs(security_points)
                    selected_security_points = [security_points[i] for i in security_protocol_indexes]
                    security_protocol = SecurityProtocol(selected_security_points)
                    fw.update_attribute_security_protocol(security_protocol, file_name_date)
                    console.print("[green]Success![/green]")
                elif field_to_modify_index == 2:
                    console.print("Give a description")
                    description = get_string_value()
                    thought = AnyThoughts(DEFAULT_TIME_NOW_FORMATTED, description)
                    fw.update_attribute(modifiable_fields[field_to_modify_index], thought, file_name_date)
                    console.print("[green]Success![/green]")
                else:
                    console.print("Give a description")
                    description = get_string_value()
                    console.print("How odd the thing is?")
                    oddness = get_integer_value(0, 10)
                    console.print("How happy did you feel doing this thing?")
                    happiness = get_integer_value(0, 10)
                    thing_done = ThingsDone(DEFAULT_TIME_NOW_FORMATTED, description, oddness, happiness)
                    fw.update_attribute(modifiable_fields[field_to_modify_index], thing_done, file_name_date)
                    console.print("[green]Success![/green]")
        elif user_input == "3":
            help_message()
        elif user_input != EXIT_COMMAND:
            unresolved_input_message()
    exit_message()


def select_json_file():
    """
    Gets from the user valid input in the form of dd-mm-YYYY for a
    JSON file present in the system.
    If user enters an empty input that
    will be interpreted as today's date.

    :return: dd-mm-YY valid string (str)
    """
    console.print("Enter date in format dd-MM-YYYY to get the file")
    console.print("If you want to get today's file, simply [bold]press Enter[/bold]")
    user_input = "-1"
    while not validation.is_json_date_format(user_input):
        user_input = console.input("[red]>>[/red] ")
        if len(user_input) == 0:
            user_input = DEFAULT_TODAY_FORMATTED
            break
    return user_input


def help_message():
    """
    Prints out a help message to the console.

    :return: None
    """
    # TODO: expand on the help message!
    console.print("Help is coming!", style="on red bold")


def exit_message():
    """
    Prints an exit message to the console before program terminates

    :return: None
    """
    # TODO: expand on the exit message!
    console.print("See you next time!", style="bold on dark_orange3")


def unresolved_input_message():
    """
    Prints a message to terminal telling that
    the inputted command cannot be resolved.

    :return: None
    """
    console.print(f"[bold]Oh no![/bold] The program does not know the command that you have entered."
                  f"\nCheck the list of commands that the program understands at the very top of the screen."
                  f"\nOr else print [bold]{HELP_COMMAND}[/bold]")


def print_json_file_data_description(file_name):
    """
    Prints out all contents of a file with the given filename.
    If no file is found an appropriate message would be displayed.

    :param file_name: string that represents filename without extension.
                      Must be in format dd-mm-YY (str)
    :return: Whether the file exists (bool)
    """
    if not fr.diary_file_exists(file_name):
        if file_name.startswith(DEFAULT_TODAY_FORMATTED):
            fw.create_empty_diary_file()
        else:
            console.print("Oh! This file does not exist!", style="on red bold")
            return False

    # Parsing the values in the file to look good in terminal
    file_contents = fr.read_file_json_data(file_name)

    emotional_happiness_value = "Not set" if file_contents["emotional_happiness"] == -1 \
        else str(file_contents["emotional_happiness"])
    security_protocol_values = file_contents["security_protocol"]
    thoughts = file_contents["thoughts"]
    things_done = file_contents["things_done"]

    console.print(f"[bold dark_violet]Date:[/bold dark_violet] {file_name}")
    console.print(f"[bold]Emotional Happiness:[/bold] {emotional_happiness_value}", style="dark_violet")

    if len(security_protocol_values) != 0:
        security_protocol_md = Markdown("- " + "\n- ".join(security_protocol_values))
        console.print(f"[bold]Security Protocol:[/bold]", style="dark_violet")
        console.print(security_protocol_md, style="dark_violet")
    else:
        console.print(f"[bold]Security Protocol:[/bold] Empty", style="dark_violet")

    print_table("Thoughts", ["time", "description"], thoughts)
    print_table("Things done", ["time", "description", "oddness", "happiness"], things_done)

    # If file exists then we can print its contents
    return True


def print_table(table_title, col_names, values):
    """
    Prints the table to the console using the data passed in arguments.

    :param table_title: title of the table (str)
    :param col_names: list of names of the column names. Must be in order
                      they appear in the list of values passed ([str])
    :param values: list of dictionaries of the values that will fill in the table ([{}])
    :return: None
    """
    table = Table(title=table_title, title_style="bold dark_violet")
    for column in col_names:
        table.add_column(column, justify="center")
    for value in values:
        row_contents = []
        for column in col_names:
            row_contents.append(value[column])
        table.add_row(*row_contents)

    console.print(table)


def get_acceptable_input(expected_inputs):
    """
    Returns an index of an input selected from the list passed as a parameter.
    User gets an option of either entering the input fully or its index in the list.
    Do not put any numbers into the expected_inputs

    :param expected_inputs: list of acceptable inputs for user to chose from ([str])
    :return: index of the element (int)
    """
    console.print("Select one input from the list below. Either type the number or the words that follow it")
    # Printing accepted inputs
    for i, input_val in enumerate(expected_inputs):
        console.print(f"{i + 1}) {input_val}")

    user_input = ""
    while user_input == "":
        user_input = console.input("[red]>>[/red] ")
        for input_index, input_val in enumerate(expected_inputs):
            if input_val == user_input or str(input_index + 1) == user_input:
                return input_index

        console.print("Unknown command")
        user_input = ""


def get_acceptable_inputs(expected_inputs):
    """
    Returns indexes of all input selected from the list passed as a parameter.
    User gets to enter all numbers of the indexes in one line separated by a whitespace.

    :param expected_inputs: list of acceptable inputs for user to chose from ([str])
    :return: indexes of the elements ([int])
    """
    console.print("Select one input from the list below. Either type the number or the words that follow it")
    # Printing accepted inputs
    for i, input_val in enumerate(expected_inputs):
        console.print(f"{i + 1}) {input_val}")

    user_input = ""
    while user_input == "":
        user_input = console.input("[red]>>[/red] ")
        if len(user_input) == 0:
            return []
        user_inputs = user_input.split(" ")
        accepted_inputs = []
        all_inputs_accepted = True
        for user_input in user_inputs:
            if int(user_input) in range(len(expected_inputs) + 1):
                accepted_inputs.append(int(user_input) - 1)
            else:
                console.print(f"Value {user_input} is not in the set of options you can chose from!")
                all_inputs_accepted = False
                break
        if all_inputs_accepted:
            return accepted_inputs
        user_input = ""


def get_integer_value(min, max):
    """
    Gets an integer value from the user within the given range.

    :param min: lowest (inclusive) bound (int)
    :param max: highest (inclusive) bound (int)
    :return: (int)
    """

    console.print(f"Type in the value within the following range: {min}-{max}")
    user_input = min - 1
    while user_input not in range(min, max + 1):
        user_input = console.input("[red]>>[/red] ")
        try:
            user_input = int(user_input)
        except Exception:
            user_input = min - 1
    return user_input


def get_string_value():
    """
    Gets a non-empty string from the user. No other checks.

    :return: (str)
    """
    console.print("Type anything you want to tell!")
    user_input = ""
    while len(user_input) == 0:
        user_input = console.input("[red]>>[/red] ")

    return user_input
