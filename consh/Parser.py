def parse_command(input_string):
    """Parse input string into command and arguments."""
    parts = input_string.strip().split()
    if not parts:
        return "", []
    return parts[0], parts[1:]