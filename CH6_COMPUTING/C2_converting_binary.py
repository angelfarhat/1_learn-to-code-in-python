#Complete the binary_string_to_int function. It takes three binary strings as input and returns each of them in #the same order as integers. Each integer is the numerical value of the string when interpreted as binary.


def binary_string_to_int(num_servers, num_players, num_admins):
    num_servers1 = int(num_servers, 2)
    num_players1 = int(num_players, 2)
    num_admins1 = int(num_admins, 2)

    return num_servers1, num_players1, num_admins1