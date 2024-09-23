"""App entry point.
"""


def main():
    """
    Main function that retrieves a message and prints it to the standard output.
    """
    msg = get_message()
    print(msg)


def get_message() -> str:
    """
    Returns a greeting message.

    Returns:
        str: A greeting message.
    """
    return "Hello, World! This is a Python app running in a dev container!"


if __name__ == "__main__":
    main()
