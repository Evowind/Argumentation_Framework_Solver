# Main file for program execution
# main.py
import argparse
import os
from parser import parse_apx
from semantics import compute_stable_extensions, compute_complete_extensions, compute_credulous_acceptance, compute_skeptical_acceptance

def write_to_file(output_path, extensions):
    """
    Writes computed extensions to a file in the specified output directory.

    Args:
        output_path (str): Path to the output file.
        extensions (list): List of computed extensions.
    """
    with open(output_path, "w") as f:
        for ext in extensions:
            formatted_ext = f"[{','.join(sorted(ext))}]"
            f.write(formatted_ext + "\n")
            print(formatted_ext)

def main():
    # Argument parser for command-line interface
    parser = argparse.ArgumentParser(description="Argumentation Framework Solver")
    parser.add_argument("-p", required=True, help="Problem type (e.g., SE-CO, SE-ST, etc.)")
    parser.add_argument("-f", required=True, help="Path to the .apx file")
    parser.add_argument("-a", required=False, help="Argument for acceptability queries")
    args = parser.parse_args()

    # Parse the argumentation framework file
    arguments, attacks = parse_apx(args.f)

    # Define output directory
    output_dir = "../outputs/results"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Output file name based on input file name
    input_file_name = os.path.basename(args.f).replace(".apx", "")

    # Problem type dispatcher
    if args.p == "SE-ST":
        stable_extensions = compute_stable_extensions(arguments, attacks)
        output_file = os.path.join(output_dir, f"{input_file_name}_st.txt")
        write_to_file(output_file, stable_extensions)
    elif args.p == "SE-CO":
        complete_extensions = compute_complete_extensions(arguments, attacks)
        output_file = os.path.join(output_dir, f"{input_file_name}_co.txt")
        write_to_file(output_file, complete_extensions)
    elif args.p.startswith("DC") or args.p.startswith("DS"):
        if not args.a:
            print("Error: -a argument is required for decision problems.")
            return
        target_argument = args.a
        result = ""
        if args.p == "DC-ST":
            credulous = target_argument in compute_credulous_acceptance(arguments, attacks, "stable")
            print("Credulous ", compute_credulous_acceptance(arguments, attacks, "stable")) #TODO Delete when testing is done
            result = "YES" if credulous else "NO"
        elif args.p == "DS-ST":
            skeptical = target_argument in compute_skeptical_acceptance(arguments, attacks, "stable")
            print("Skeptical ", compute_skeptical_acceptance(arguments, attacks, "stable")) #TODO Delete when testing is done
            result = "YES" if skeptical else "NO"
        elif args.p == "DC-CO":
            credulous = target_argument in compute_credulous_acceptance(arguments, attacks, "complete")
            print("Credulous ", compute_credulous_acceptance(arguments, attacks, "complete")) #TODO Delete when testing is done
            result = "YES" if credulous else "NO"
        elif args.p == "DS-CO":
            skeptical = target_argument in compute_skeptical_acceptance(arguments, attacks, "complete")
            print("Skeptical ", compute_skeptical_acceptance(arguments, attacks, "complete")) #TODO Delete when testing is done
            result = "YES" if skeptical else "NO"
        else:
            print("Error: Unsupported problem type.")
            return
        # Write decision result to file
        output_file = os.path.join(output_dir, f"{input_file_name}_{args.p.lower()}.txt")
        with open(output_file, "w") as f:
            f.write(result + "\n")
            print(result)
    else:
        print("Error: Unsupported problem type.")

if __name__ == "__main__":
    main()

