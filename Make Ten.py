from fractions import Fraction
from itertools import permutations


TARGET = Fraction(10, 1)
OPS = ("+", "-", "*", "/")


def apply_op(left, right, op):
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "*":
        return left * right
    if right == 0:
        return None
    return left / right


def search(items):
    if len(items) == 1:
        value, expr = items[0]
        return expr if value == TARGET else None

    for i in range(len(items)):
        for j in range(len(items)):
            if i == j:
                continue

            remaining = [items[k] for k in range(len(items)) if k not in (i, j)]
            left_value, left_expr = items[i]
            right_value, right_expr = items[j]

            for op in OPS:
                result = apply_op(left_value, right_value, op)
                if result is None:
                    continue

                new_expr = f"({left_expr} {op} {right_expr})"
                found = search(remaining + [(result, new_expr)])
                if found:
                    return found

    return None


def solve(digits_text):
    if len(digits_text) != 4 or not digits_text.isdigit():
        return None, "Please enter exactly 4 digits, like 3862."

    items = [(Fraction(int(ch), 1), ch) for ch in digits_text]

    for ordered_items in set(permutations(items)):
        found = search(list(ordered_items))
        if found:
            return found, None

    return None, "No way to make 10 with those 4 digits using +, -, *, and /."


def main():
    digits_text = input("Enter 4 digits, like 3862: ").strip()
    solution, error = solve(digits_text)

    if error:
        print(error)
        return

    print(f"Found it: {solution} = 10")


if __name__ == "__main__":
    main()
