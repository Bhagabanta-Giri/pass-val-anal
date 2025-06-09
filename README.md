# pass-val-anal

A lean, no-nonsense password toolkit that validates, analyzes, and generates passwords—because weak passwords are embarrassing, and you deserve better.

## Overview

`pass-val-anal` is a simple Python command-line suite that handles:

- Password strength validation  
- Character composition analysis  
- Special character detection  
- Custom password generation (from “barely a password” to “Fort Knox in a string”)

Built entirely in Python with zero dependencies, it’s perfect for those who want to understand password logic without relying on bloated frameworks or mysterious black-box tools.

## Features

### Special Character Checker (`SpecialCharacter.py`)
- One job: determine if your input contains non-alphanumeric characters.
- No sugarcoating—just a clean `True` or `False`.
- Even I’m not sure why I added this, but hey, it works.

### Validator (`Validator.py`)
- Evaluates passwords using five criteria: length, digits, uppercase, lowercase, and special characters.
- Grades password strength from *Very Weak* to *Very Strong*.
- Breaks down character composition—alphabet count, numbers, special characters.
- Doesn’t hold back. If your password sucks, it’ll let you know.

### Password Generator (`Generator.py`)
- CLI-based interactive password generator.
- User picks strength level from 1 (Very Weak) to 5 (Very Strong).
- Customizable:
  - Letters, digits, special characters
  - Uppercase/lowercase preference
  - Length (min. 7)
- Gives you a password. What you do with it is your business.
- Built-in roast if you choose “0” (i.e., no password). You’ve been warned.

## Requirements

- Python 3.6 or above
- Zero third-party dependencies  
- If `import string` causes errors, you might need a new Python install—or a new life decision.

## Technology

- Language: Python 3.12  
- No third-party dependencies  
- Pure standard library, pure power

---

## Optional Add-Ons

Want to flex harder? You can extend this repo with:
- A proper CLI interface (argparse / click)
- Visual README enhancements (shields.io badges, ASCII logo, etc.)
- GitHub Actions integration for testing or linting

---

Feel free to clone, fork, flame, or contribute. The code’s free—your password doesn’t have to be.
