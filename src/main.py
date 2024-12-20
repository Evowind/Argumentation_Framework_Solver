#Main file for program execution
#main.py
import argparse
import os
from parser import parse_apx
from semantics import compute_stable_extensions, compute_complete_extensions, compute_credulous_acceptance, compute_skeptical_acceptance

#Save extensions to a file
def write_to_file(output_path, extensions):
    #Chuck extensions into a file and log them while you're at it
    with open(output_path, "w") as f:
        for ext in extensions:
            formatted_ext = f"[{','.join(sorted(ext))}]"  #Make the extension look pretty.
            f.write(formatted_ext + "\n")
            print(formatted_ext)  #Who doesn’t love a bit of live feedback?

def main():
    #Set up the command-line parser thingy
    parser = argparse.ArgumentParser(description="Argumentation Framework Solver")
    parser.add_argument("-p", required=True, help="Problem type (like SE-CO or SE-ST)")
    parser.add_argument("-f", required=True, help="Path to the .apx file, don't forget this one")
    parser.add_argument("-a", required=False, help="Argument for acceptability queries, if needed")
    args = parser.parse_args()

    #Read the arguments and attacks from the .apx file
    arguments, attacks = parse_apx(args.f)

    #Figure out where to stick the output
    output_dir = "../outputs/results"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  #Make the directory if it’s not already there.

    #Create the output file name based on the input file’s name
    input_file_name = os.path.basename(args.f).replace(".apx", "")

    #Work out what kind of problem we’re dealing with
    if args.p == "SE-ST":
        stable_extensions = compute_stable_extensions(arguments, attacks)
        output_file = os.path.join(output_dir, f"{input_file_name}_st.txt")
        write_to_file(output_file, stable_extensions)
    elif args.p == "SE-CO":
        complete_extensions = compute_complete_extensions(arguments, attacks)
        output_file = os.path.join(output_dir, f"{input_file_name}_co.txt")
        write_to_file(output_file, complete_extensions)
    elif args.p.startswith("DC") or args.p.startswith("DS"):
        if not args.a:  #No argument provided? That’s a no-no.
            print("Error: You need to use -a for decision problems. Don't skip this.")
            return
        target_argument = args.a
        result = ""
        if args.p == "DC-ST":
            credulous = target_argument in compute_credulous_acceptance(arguments, attacks, "stable")
            #print("Credulous ", compute_credulous_acceptance(arguments, attacks, "stable"))#TODO Bin this once testing is sorted.
            result = "YES" if credulous else "NO"
        elif args.p == "DS-ST":
            skeptical = target_argument in compute_skeptical_acceptance(arguments, attacks, "stable")
            #print("Skeptical ", compute_skeptical_acceptance(arguments, attacks, "stable"))#TODO Bin this after testing too.
            result = "YES" if skeptical else "NO"
        elif args.p == "DC-CO":
            credulous = target_argument in compute_credulous_acceptance(arguments, attacks, "complete")
            #print("Credulous ", compute_credulous_acceptance(arguments, attacks, "complete"))#TODO Bin this one too.
            result = "YES" if credulous else "NO"
        elif args.p == "DS-CO":
            skeptical = target_argument in compute_skeptical_acceptance(arguments, attacks, "complete")
            #print("Skeptical ", compute_skeptical_acceptance(arguments, attacks, "complete"))#TODO You know the drill by now.
            result = "YES" if skeptical else "NO"
        else:
            print("Error: This type of problem isn't supported. What are you doing?")
            return
        #Write the result into a file
        output_file = os.path.join(output_dir, f"{input_file_name}_{args.p.lower()}.txt")
        with open(output_file, "w") as f:
            f.write(result + "\n")
            print(result)  #Let the user know what’s what.
    else:
        print("Error: This problem type isn’t supported. Are you sure about this?")

if __name__ == "__main__":
    main()
