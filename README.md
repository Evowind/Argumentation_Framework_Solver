# Argumentation Framework Solver

Welcome to the **Argumentation Framework Solver**! This project is designed to parse, analyse, and solve problems within argumentation frameworks. Whether you're working with stable or complete extensions, or just testing credulous and sceptical acceptance, this tool has got you covered.

---

## Features

- **Parse .apx files**: Extract arguments and attacks from `.apx` files.
- **Compute Extensions**: Solve for stable and complete extensions.
- **Decision Problems**: Handle credulous and sceptical acceptance queries.
- **Visualisation**: Generate and save graphical representations of argumentation frameworks.
- **File Outputs**: Automatically save results to a predefined directory for easy access.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/argumentation-framework-solver.git
   cd argumentation-framework-solver
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the program using the command line interface:

```bash
python main.py -p <PROBLEM_TYPE> -f <FILE_PATH> [-a <ARGUMENT>]
```

### Arguments:
- `-p`: Specify the problem type. Options include:
  - `SE-ST`: Stable Extensions
  - `SE-CO`: Complete Extensions
  - `DC-ST`: Credulous Acceptance (Stable Extensions)
  - `DS-ST`: Sceptical Acceptance (Stable Extensions)
  - `DC-CO`: Credulous Acceptance (Complete Extensions)
  - `DS-CO`: Sceptical Acceptance (Complete Extensions)
- `-f`: Path to the `.apx` file.
- `-a`: (Optional) Specify an argument for decision problems.

### Example:

Find stable extensions for a given `.apx` file:
```bash
python main.py -p SE-ST -f examples/example1.apx
```

Test credulous acceptance for argument `A`:
```bash
python main.py -p DC-ST -f examples/example1.apx -a A
```

---

## Output

Results are saved to the `outputs/results/` directory with filenames based on the input file and problem type. For instance:

- Input File: `example1.apx`
- Problem Type: `SE-ST`
- Output File: `outputs/results/example1_st.txt`

---

## File Structure

```
argumentation-framework-solver/
├── main.py            # Main execution script
├── parser.py          # Parses .apx files
├── semantics.py       # Core logic for extensions and queries
├── outputs/           # Directory for output files and visualisations
├── examples/          # Sample .apx files
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## Requirements

- Python 3.8+
- Libraries:
  - `argparse`
  - `os`
  - `matplotlib`
  - `networkx`

Install dependencies via `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## Contributing

Feel free to fork this repository and submit pull requests. If you encounter bugs or have suggestions, open an issue. Contributions are always welcome!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

Special thanks to the developers of `networkx` and `matplotlib`, whose libraries made visualisation and graph handling a breeze.

---

Happy reasoning! 🚀

