import re

def part1(lines):
    total_sum = 0
    for line in lines:
        match = re.search(r'\d', line)
        if match:
            first_digit = int(match.group())
            last_digit = int(re.findall(r'\d', line)[-1])
            total_sum += int(f'{first_digit}{last_digit}')
    return total_sum

def part2(lines):
    total_sum = 0
    spelled_out_digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for line in lines:
        digits = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', line)
        if digits:
            first_digit = digits[0] if digits[0].isdigit() else spelled_out_digits[digits[0]]
            last_digit = digits[-1] if digits[-1].isdigit() else spelled_out_digits[digits[-1]]
            total_sum += int(f'{first_digit}{last_digit}')
    return total_sum

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

file_path = '1.txt'
lines = read_input_file(file_path)
result1 = part1(lines)
result2 = part2(lines)
print("Part 1:",result1)
print("Part 2:", result2)
