def parse_pipeline(input_string):
    """Parse input string into a list of (command, args) tuples for piping."""
    # Split by pipe symbol, preserving spaces within commands
    commands = [cmd.strip() for cmd in input_string.split("|") if cmd.strip()]
    pipeline = []

    for cmd in commands:
        parts = cmd.split()
        if not parts:
            continue
        pipeline.append((parts[0], parts[1:]))

    return pipeline