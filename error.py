def print_error(num):
    ERROR_POSITION = {
        1: "pD",
        2: "pL",
        3: "pR",
        4: "pR (more string after ;)",
        5: "Error EBNF"
    }
    error = ERROR_POSITION[num]
    print(f"Error occured due to {error}")
