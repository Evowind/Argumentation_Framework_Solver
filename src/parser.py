# Module to read and parse .apx files
# parser.py
def parse_apx(file_path):
    """
    Parses an .apx file to extract arguments and attacks.

    Args:
        file_path (str): Path to the .apx file.

    Returns:
        tuple: A tuple containing a set of arguments and a list of attack tuples.
    """
    arguments = set()
    attacks = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:  # Ignore empty lines
                continue
            if line.startswith("arg"):
                # Extract argument name from "arg(NAME)."
                argument = line[4:-2]
                arguments.add(argument)
            elif line.startswith("att"):
                # Extract attack relationship from "att(ARG1,ARG2)."
                attack = tuple(line[4:-2].split(','))
                attacks.append(attack)
    print(f"All arguments: {arguments}") #TODO delete after testing
    print(f"All attacks: {attacks}") #TODO delete after testing
    return arguments, attacks

