def file_loader(file_path):
    """
    Load a Markdown file and return its content as a string.

    Args:
        file_path (str): The path to the Markdown file.

    Returns:
        str: The content of the Markdown file.
    """
    with open(file_path, "r") as f:
        return f.read()
    