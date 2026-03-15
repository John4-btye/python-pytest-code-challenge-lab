# Longest Palindromic Substring (Pytest Lab)

This project implements and tests a function that returns the **longest palindromic substring** within a given string, using **pytest** for automated validation.

## What This Code Does

**Goal:** Given a string `s`, return the longest contiguous substring that reads the same forward and backward.

Examples:

| Input | Output |
| --- | --- |
| `"babad"` | `"bab"` or `"aba"` |
| `"cbbd"` | `"bb"` |
| `"racecar"` | `"racecar"` |
| `"ac"` | `"a"` or `"c"` |

## How The Solution Works

The implementation in `lib/palindrome.py` uses the **expand-around-center** approach:

1. Every palindrome has a “center”.
2. For each index `i`, expand outward for:
   - an odd-length palindrome centered at `(i, i)`
   - an even-length palindrome centered at `(i, i+1)`
3. Track the best (longest) palindrome found and return it at the end.

Complexity:

- Time: `O(n^2)` in the worst case (expanding around centers)
- Space: `O(1)` extra space (not counting the returned substring)

## Project Layout

- `lib/palindrome.py` — implementation of `longest_palindromic_substring`
- `lib/testing/test_palindrome.py` — pytest test suite (basic cases, edge cases, and type/failure cases)
- `pytest.ini` — ensures imports work from the project root

## Setup

This repo is configured to use **Pipenv**.

```bash
pipenv install
```

## Run The Tests

Run all tests using the project environment:

```bash
pipenv run pytest
```

Expected output (current suite):

- 14 tests collected
- 14 tests passing

## Use The Function Interactively

```bash
pipenv run python -c "from lib.palindrome import longest_palindromic_substring; print(longest_palindromic_substring('babad'))"
```

## Notes

- The function expects a string input. Non-string inputs raise `TypeError` (covered by tests).
