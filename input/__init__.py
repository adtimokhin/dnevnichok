from rich.console import Console

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
        "\nThat is a digital diary of a sort.[/bold]" , justify="center")

    console.print("Here is what you can do:")
    console.print("1) See what you already have written")
    console.print("2) Write something down")
    console.print("3) Ask for help")
    console.print("To select an option write a number from 1 to 3")
    console.print(f"To get help at any point write [bold]{HELP_COMMAND}[/bold]")
    console.print(f"To exit the program just write [bold]{EXIT_COMMAND}[/bold]")
    console.print()
    parse_input()


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
            print("We need to display what the user has stored in the file")
        elif user_input == "2":
            print("Call a method that will describe how to update contents of the JOSN file")
        elif user_input == "3":
            help_message()
        elif user_input != EXIT_COMMAND:
            unresolved_input_message()
    exit_message()


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