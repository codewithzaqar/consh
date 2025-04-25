def parse_pipeline(input_string):
    """Parse input string into a list of (command, args) tuples for piping."""
    # Split by pipe symbol, handling redirection
    parts = input_string.split(">")
    if len(parts) > 2:
        return [("error", ["Multiple redirection operators not supported"])]

    pipeline_str = parts[0].strip()
    redirect = parts[1].strip() if len(parts) == 2 else None

    # Split pipeline by pipe symbol
    commands = [cmd.strip() for cmd in pipeline_str.split("|") if cmd.strip()]
    pipeline = []

    for cmd in commands:
        parts = cmd.split()
        if not parts:
            continue
        pipeline.append((parts[0], parts[1:]))

    # Add redirection as a pseudo-command
    if redirect:
        pipeline.append((">", [redirect]))

    return pipeline