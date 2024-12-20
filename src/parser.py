#Module to read and parse .apx files
#parser.py
def parse_apx(file_path):
    """
    Reads an .apx file and pulls out arguments and attacks.

    Args:
        file_path (str): Path to the .apx file.

    Returns:
        tuple: A set of arguments and a list of attack relationships.
    """
    arguments = set()  #All the arguments will live here.
    attacks = []       #This is where the attacks go.
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  #Clean up spaces and newlines.
            if not line:         #Skip empty lines.
                continue
            if line.startswith("arg"):    #Found an argument, grab it.
                argument = line[4:-2]     #Snag the name from "arg(NAME)."
                arguments.add(argument)   #Stick it in the set.
            elif line.startswith("att"):  #Found an attack, get the details.
                attack = tuple(line[4:-2].split(','))  #Break it into (ARG1, ARG2).
                attacks.append(attack)    #Add it to the list.
    #print(f"All arguments: {arguments}") #TODO delete after testing, it's messy.
    #print(f"All attacks: {attacks}")     #TODO delete after testing, it's messy.
    return arguments, attacks             #Finally, ship the results.