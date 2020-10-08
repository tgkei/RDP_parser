def print_error(num):
    ERROR_POSITION = {
        1: "pD",
        2: "pL",
        3: "pR",
        4: "more string after ;"
    }
    error = ERROR_POSITION[num]
    print(f"Error occured due to {error}")
