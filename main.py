IP = []
PREFIX = 0
NETWORK_ID = {}
BROADCAST_ID = {}
SUBNET_MASK = {}


def get_data():
    global IP, PREFIX
    
    IP = (input("Enter IP: ")).split('.')
    PREFIX = int(input("Enter Prefix: "))


def bin_to_int(binary: list):
    return [int(str(octet), 2) for octet in binary]

def int_to_bin(integer: list):
    return [(bin(int(octet))[2:]).rjust(8, '0') for octet in integer]

def binary_list_to_string(data: list):
    return ''.join(data)

def binary_string_to_list(data: str):
    return [data[i:i + 8] for i in range(0, 32, 8)]

def int_string_to_list(data: str):
    return data.split('.')


def calculate_broadcast_id(network_binary_list):
    network_binary_string = binary_list_to_string(network_binary_list)
    result = ""

    for step in range(32):
        result += '1' if step >= PREFIX else network_binary_string[step]

    result = binary_string_to_list(result)

    return {
        "bin": result,
        "int": bin_to_int(result)
    }

def calculate_network_id():
    binary_list = int_to_bin(IP)
    binary_string = binary_list_to_string(binary_list)
    result = ""

    for step in range(32):
        result += '0' if step >= PREFIX else binary_string[step]
    
    result = binary_string_to_list(result)

    return {
        "bin": result,
        "int": bin_to_int(result)
    }

def calculate_subnet_mask():
    result = ""

    for step in range(32):
        result += '0' if step >= PREFIX else '1'
    
    result = binary_string_to_list(result)

    return {
        "bin": result,
        "int": bin_to_int(result)
    }

def calculate_ip_type(network_binary_list, broadcast_binary_list):
    network_binary_string = binary_list_to_string(network_binary_list)
    broadcast_binary_string = binary_list_to_string(broadcast_binary_list)
    ip_binary_string = binary_list_to_string(int_to_bin(IP))
    
    if ip_binary_string == network_binary_string:
        print(f"IP {'.'.join(IP)}/{PREFIX} is Network ID!")
    elif ip_binary_string == broadcast_binary_string:
        print(f"IP {'.'.join(IP)}/{PREFIX} is Broadcast ID!")
    else:
        print(f"IP {'.'.join(IP)}/{PREFIX} is Host ID!")


def show(data: list):
    return '.'.join([str(octet) for octet in data])



get_data()

print("----------")

SUBNET_MASK = calculate_subnet_mask()
print(f"Subnet Mask:\t {show(SUBNET_MASK['int'])} \t {show(SUBNET_MASK['bin'])}")

NETWORK_ID = calculate_network_id()
print(f"Netword ID:\t {show(NETWORK_ID['int'])} \t {show(NETWORK_ID['bin'])}")

BROADCAST_ID = calculate_broadcast_id(NETWORK_ID['bin'])
print(f"Broadcast ID:\t {show(BROADCAST_ID['int'])} \t {show(BROADCAST_ID['bin'])}")

print(f"Hosts Number:\t {format(2 ** (32 - PREFIX), ',')}")

print("----------")

calculate_ip_type(NETWORK_ID['bin'], BROADCAST_ID['bin'])
