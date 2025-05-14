# Q3: Check if a binary number is divisible by 3 using DFA logic
def binary_divisible_by_3(binary_str):
    if any(c not in '01' for c in binary_str):
        return "Error: Please enter a valid binary number (only 0 and 1)."
    
    state = 0
    for bit in binary_str:
        digit = int(bit)
        state = (state * 2 + digit) % 3
    return state == 0

if __name__ == "__main__":
    user_input = input("Enter a binary number to check if it is divisible by 3: ")
    result = binary_divisible_by_3(user_input)
    print("Result:", result)
