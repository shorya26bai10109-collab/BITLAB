#BitLab: Binary Logic & Digital Arithmetic Simulator

## Project Overview
BitLab is an interactive, console-based digital logic and binary arithmetic simulator developed in pure Python. It models how computer hardware and arithmetic logic units (ALUs) process binary information at the register level. The tool supports signed two's complement conversions, bit-by-bit binary full addition with explicit carry propagation, digital logic gate evaluation, and parity error-checking analysis without using external libraries or high-level built-in conversion shortcuts.

---

## Key Features
* **8-Bit Two's Complement Converter:** Converts signed integers (-128 to 127) to 8-bit binary via bit inversion and addition, and decodes 8-bit patterns evaluating the most significant bit (MSB) as negative weight.
* **Binary Full Adder with Carry Trace:** Implements manual column-by-column addition from least to most significant bit, printing a visual trace of input bits, sum, and propagated carry bits.
* **Digital Logic Gate Visualizer:** Evaluates bitwise `AND`, `OR`, and `XOR` operations across binary words using simulated truth-table dictionaries and aligns the outputs for side-by-side comparison.
* **Bit Analysis & Parity Generator:** Analyzes bit streams to compute Hamming weight (count of set bits) and generates both even and odd parity bits for data transmission verification.
* **Session History Log:** Records every completed simulation as an immutable record to provide a full audit trail during the session.

---

## Environment Setup
* **Operating System:** Windows, macOS, or Linux
* **Prerequisites:** Python 3.x installed
* **Environment:** Command Prompt, PowerShell, VS Code terminal, or Linux shell

---

## Dependencies & Installation
* **Zero External Dependencies:** Built strictly with standard Python built-in capabilities.
* No `pip install` commands or `requirements.txt` needed.

---

## Execution Instructions
1. Open your terminal or Command Prompt.
2. Navigate to the project directory where `main.py` is saved:
   ```bash
   cd path/to/project_folder
