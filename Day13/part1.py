from sympy import symbols, Eq, solve, Integer
import re

# Read and process the file
def file_to_list(filename:str):

    with open(filename, "r") as file:
        lines = file.readlines()
        return lines

# Group the lines into chunks of 3 (Button A, Button B, Prize)
def extract_list_info(lines:list):

    # Initialize the result list
    result = []

    for i in range(0, len(lines), 4):
        # Extract values from each group
        button_a_match = re.search(r"X\+(\d+), Y\+(\d+)", lines[i])
        button_b_match = re.search(r"X\+(\d+), Y\+(\d+)", lines[i+1])
        prize_match = re.search(r"X=(\d+), Y=(\d+)", lines[i+2])
    
        if button_a_match and button_b_match and prize_match:
            # Append extracted values to the result as a list
            result.append([
                int(button_a_match.group(1)),  # X of Button A
                int(button_b_match.group(1)),  # X of Button B
                int(prize_match.group(1)),     # X of Prize
                int(button_a_match.group(2)),  # Y of Button A
                int(button_b_match.group(2)),  # Y of Button B
                int(prize_match.group(2)),     # Y of Prize
            ])

    return result

def calculate_tokens(values_list:list):

    # Define variables
    A, B = symbols('A B')

    # Token count
    token_count = 0

    for i in range(0, len(values_list)):

        X_button_A = values_list[i][0]
        X_button_B = values_list[i][1]
        X_prize = values_list[i][2]
        Y_button_A = values_list[i][3]
        Y_button_B = values_list[i][4]
        Y_prize = values_list[i][5]

        # Define equations
        eq1 = Eq(A * X_button_A + B * X_button_B, X_prize)
        eq2 = Eq(A * Y_button_A + B * Y_button_B, Y_prize)

        # Solve the equations
        solutions = solve((eq1, eq2), (A, B))
        #print(solutions)

        A_value = solutions[A]
        B_value = solutions[B]

        if isinstance(A_value, Integer) and isinstance(A_value, Integer):
            # Perform calculations
            token_count += A_value * 3 + B_value

    return token_count

#file_path = "Day13/test.txt"
file_path = "Day13/input.txt"
#print(f"result: {extract_list_info(file_to_list(file_path))}")
# [[94, 22, 8400, 34, 67, 5400], [26, 67, 12748, 66, 21, 12176], [17, 84, 7870, 86, 37, 6450], [69, 27, 18641, 23, 71, 10279]]
#test = [[94, 22, 8400, 34, 67, 5400], [26, 67, 12748, 66, 21, 12176], [17, 84, 7870, 86, 37, 6450], [69, 27, 18641, 23, 71, 10279]]
print(f"total: {calculate_tokens(extract_list_info(file_to_list(file_path)))}")
