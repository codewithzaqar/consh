def parse_pipeline(input_string):
    """Parse input string into a list of (command, args) tuples for piping and redirection."""
    # Split by redirection operators
    parts = []
    current = ""
    i = 0
    while i < len(input_string):
        if input_string[i:i+2] == ">>":
            if current.strip():
                parts.append(current.strip())
            parts.append(">>")
            current = ""
            i += 2
        elif input_string[i] == ">":
            if current.strip():
                parts.append(current.strip())
            parts.append(">")
            current = ""
            i += 1
        elif input_string[i] == "|":
            if current.strip():
                parts.append(current.strip())
            current = ""
            i += 1
        else:
            current += input_string[i]
            i += 1
    if current.strip():
        parts.append(current.strip())
    
    pipeline = []
    i = 0
    while i < len(parts):
        if parts[i] in (">", ">>"):
            if i + 1 < len(parts):
                pipeline.append((parts[i], [parts[i + 1]]))
                i += 2
            else:
                pipeline.append(("error", ["Missing redirection target"]))
                break
        else:
            # Split command by spaces
            cmd_parts = parts[i].split()
            if cmd_parts:
                pipeline.append((cmd_parts[0], cmd_parts[1:]))
            i += 1
    
    return pipeline