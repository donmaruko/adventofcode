def calculate_score(opponent, response):
    if opponent == response:
        return 3  # Draw
    elif (opponent == 'A' and response == 'Y') or (opponent == 'B' and response == 'X') or (opponent == 'C' and response == 'Z'):
        return 6  # Win
    else:
        return 1  # Lose

def total_score(strategy_guide):
    score = 0
    for line in strategy_guide:
        opponent, response = line.split()
        score += int(response) + calculate_score(opponent, response)
    return score

def read_strategy_guide(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Example strategy guide file path
file_path = 'AoC/2022_2.txt'

# Read strategy guide from the file
strategy_guide = read_strategy_guide(file_path)

# Calculate and print the total score
result = total_score(strategy_guide)
print(result)
