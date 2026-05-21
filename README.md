# Make Ten Solver

A small Python command-line program that checks whether four digits can be combined to make the value `10` using the operators `+`, `-`, `*`, and `/`.

The program tries different digit orders and operator combinations, then prints the first expression it finds that equals 10.

## Features

- Accepts exactly four digits from the user.
- Uses addition, subtraction, multiplication, and division.
- Supports repeated digits.
- Avoids floating-point rounding errors by using Python's `Fraction` type.
- Handles division by zero safely.
- Prints a valid expression if one exists.
- Prints a clear message if no solution is found.

## Requirements

- Python 3.x

No external libraries are required. The program only uses Python standard library modules:

- `fractions`
- `itertools`

## Files

```text
Make Ten.py
```

## How to Run

From the folder containing the file, run:

```bash
python "Make Ten.py"
```

Depending on your system, you may need to use:

```bash
python3 "Make Ten.py"
```

## Example Usage

```text
Enter 4 digits, like 3862: 3862
Found it: ((3 * 6) - (8 / 2)) = 10
```

Another possible run:

```text
Enter 4 digits, like 3862: 1111
No way to make 10 with those 4 digits using +, -, *, and /.
```

## Input Rules

The input must be exactly four numeric digits.

Valid examples:

```text
3862
1234
1111
9090
```

Invalid examples:

```text
38
38625
abcd
3 8 6 2
```

If the input is invalid, the program prints:

```text
Please enter exactly 4 digits, like 3862.
```

## How It Works

The program represents each digit as a `Fraction` so calculations remain exact. This prevents errors that can happen when using floating-point decimal math.

The solver works recursively:

1. Convert the four input digits into number-expression pairs.
2. Try every ordering of the four digits.
3. Pick two values at a time.
4. Apply each operator: `+`, `-`, `*`, and `/`.
5. Replace the two selected values with the result.
6. Repeat until only one value remains.
7. If the final value equals `10`, return the expression.

## Main Functions

### `apply_op(left, right, op)`

Applies one arithmetic operator to two values.

It supports:

- Addition
- Subtraction
- Multiplication
- Division

If division by zero would occur, it returns `None`.

### `search(items)`

Recursively searches for an arithmetic expression that evaluates to 10.

Each item is stored as:

```python
(value, expression)
```

For example:

```python
(Fraction(3, 1), "3")
```

### `solve(digits_text)`

Validates the user input and starts the search process.

Returns either:

```python
(solution, None)
```

or:

```python
(None, error_message)
```

### `main()`

Handles user input and prints the final result.

## Limitations

- The program only works with four digits.
- The target value is fixed at `10`.
- Only the four basic arithmetic operators are supported.
- It returns the first valid solution it finds, not every possible solution.

## Possible Improvements

Future versions could add:

- A custom target number.
- Support for more than four digits.
- A mode that prints all possible solutions.
- A graphical user interface.
- Better formatting for expressions.
- Unit tests for the solver functions.

## License

MIT license has been specified.
