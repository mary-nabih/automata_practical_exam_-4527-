
# DFA that accepts binary strings containing the substring '101'
def dfa_accepts_101(s):
    if any(c not in '01' for c in s):
        return "Error: Please enter a valid binary string (only 0 and 1)."
    
    state = 'q0'
    for char in s:
        if state == 'q0':
            if char == '1':
                state = 'q1'
        elif state == 'q1':
            if char == '0':
                state = 'q2'
            elif char == '1':
                state = 'q1'
        elif state == 'q2':
            if char == '1':
                state = 'q3'
            elif char == '0':
                state = 'q0'
        elif state == 'q3':
            break
    return state == 'q3'

if __name__ == "__main__":
    user_input = input("Enter a binary string to check if it contains '101': ")
    result = dfa_accepts_101(user_input)
    print("Result:", result)
