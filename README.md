# 🧮 String Calculator (TDD Kata)

## Overview
This project is an implementation of the **String Calculator Kata**.

The goal of this exercise was **not just to make the code work**, but to demonstrate a **Test-Driven Development (TDD)** approach and showcase **clean, maintainable design**.

---

## 🧠 Thought Process
I approached this problem using the **Red → Green → Refactor** TDD cycle:

1. **Red** – Start with a small, failing test that describes the desired behavior.  
2. **Green** – Write the simplest code possible to make the test pass.  
3. **Refactor** – Clean and simplify the implementation without changing behavior.

Each commit in this repository reflects one of these steps — so you can trace how the solution evolved over time.

---

## ✅ Features Implemented
- Returns `0` for empty input  
- Handles single and multiple comma-separated numbers  
- Supports newline (`\n`) as a valid delimiter  
- Allows custom delimiters using the syntax `//<delimiter>\n<numbers>`  
- Raises an exception when negative numbers are provided, listing all negatives  

---

## 🧩 Example Usages

```python
from string_calculator.calculator import add

add("")           # 0
add("1")          # 1
add("1,2")        # 3
add("1\n2,3")     # 6
add("//;\n1;2")   # 3
add("-1,2,-3")    # raises Exception("negative numbers not allowed -1,-3")
```

## ⚙️ Setup and Run

1. Clone the repo

```bash
git clone https://github.com/gurpal-04/TDD.git
cd TDD
```

2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install pytest
```

4. Run tests
```bash
pytest
```