# Pytest Code Challenge Lab

## Overview

This project implements and tests a solution for the **Longest Palindromic Substring** problem using **Test-Driven Development (TDD)**. The goal of this lab was to first create a testing suite using **pytest**, and then implement the function that satisfies those tests.

A **palindrome** is a word, phrase, or sequence that reads the same backward as forward. The function in this project identifies the **longest palindromic substring** within a given input string.

Example:

Input:

```
babad
```

Output:

```
bab
```

or

```
aba
```

Both are valid palindromes.

---

## Project Structure

```
python-pytest-code-challenge-lab
│
├── pytest.ini
├── Pipfile
├── Pipfile.lock
├── README.md
│
└── lib
    ├── __init__.py
    ├── palindrome.py
    │
    └── testing
        └── test_palindrome.py
```

### File Descriptions

**palindrome.py**

Contains the function:

```
longest_palindromic_substring(s)
```

This function analyzes a string and returns the longest substring that is a palindrome.

---

**test_palindrome.py**

Contains the **pytest test suite** used to verify that the algorithm works correctly. The tests check for:

- Basic functionality
- Edge cases
- Different string patterns

---

**pytest.ini**

Configures pytest to correctly locate project modules so tests can import the `lib` directory.

---

## Testing Approach

The lab follows a **Test-Driven Development (TDD)** workflow:

1. Write tests first.
2. Run the tests (they fail initially).
3. Implement the function.
4. Run the tests again until they pass.

This process helps ensure the function behaves correctly before implementation is finalized.

---

## Test Cases Included

The test suite validates several scenarios:

| Test Type                | Example                        |
| ------------------------ | ------------------------------ |
| Basic Cases              | `"babad"` → `"bab"` or `"aba"` |
| Even Palindromes         | `"cbbd"` → `"bb"`              |
| Entire String Palindrome | `"racecar"`                    |
| Single Character         | `"a"`                          |
| No Long Palindrome       | `"ac"`                         |
| Repeating Characters     | `"aaaa"`                       |
| Long Internal Palindrome | `"forgeeksskeegfor"`           |

These tests help ensure the algorithm works under multiple conditions.

---

## Running the Tests

Activate the virtual environment:

```
pipenv shell
```

Run the test suite:

```
pytest
```

If the implementation is correct, pytest will report that all tests pass.

---

## Implementation Strategy

The solution uses the **Expand Around Center** technique.

For each character in the string, the algorithm:

1. Treats the character as the center of a potential palindrome.
2. Expands outward while the characters match.
3. Tracks the longest palindrome found.

This approach efficiently finds the longest palindromic substring within the input.

---

## Summary

In this lab I:

- Created a pytest testing suite
- Implemented multiple test cases for edge conditions
- Implemented the `longest_palindromic_substring` function
- Configured pytest to recognize project modules
- Verified functionality using automated tests

This project demonstrates the use of **pytest, test-driven development, and algorithm implementation in Python**.
