# PassVault - Secure Password Generator

A simple yet powerful terminal-based Random Secure Password Generator written in Python. This tool uses the cryptographically secure `secrets` library to generate robust passwords.

## Features
- **Strong & Random**: Uses Python's `secrets` module for secure randomness.
- **Comprehensive Characters**: Includes uppercase, lowercase, numbers, and special symbols.
- **Customizable Length**: You can specify how long you want your passwords to be.
- **Bulk Suggestions**: Generates 5 strong passwords at once.
- **Clean Terminal UI**: Minimalist and easy-to-use command-line interface.

## Prerequisites
- Python 3.x installed on your system.

## How to Run
Once you have the script, simply run it using Python in your terminal:

```bash
python3 generator.py
```

## Usage
1. Run the script.
2. Enter the desired password length (default is 16).
3. The script will output 5 secure password suggestions.
4. Copy whichever one you like!

## Security Note
This tool uses `secrets.choice()` which is much more secure than the standard `random.choice()` as it is designed for cryptographic purposes, making it ideal for generating passwords.

## License
This project is under MIT LICENSE. SEE [LICENSE](LICENSE) file for details.
