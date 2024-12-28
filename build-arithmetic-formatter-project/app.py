def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid format.'

        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (operand1.isdigit() and operand2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        operand1 = int(operand1)
        operand2 = int(operand2)

        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2

        max_width = max(len(str(operand1)), len(str(operand2))) + 2

        first_line.append(str(operand1).rjust(max_width))
        second_line.append(operator + str(operand2).rjust(max_width - 1))
        dashes.append('-' * max_width)
        results.append(str(result).rjust(max_width))

    arranged_first_line = '    '.join(first_line)
    arranged_second_line = '    '.join(second_line)
    arranged_dashes = '    '.join(dashes)

    if display_answers:
        arranged_results = '    '.join(results)
        return f"{arranged_first_line}\n{arranged_second_line}\n{arranged_dashes}\n{arranged_results}"
    else:
        return f"{arranged_first_line}\n{arranged_second_line}\n{arranged_dashes}"

# Test the function with cases
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))