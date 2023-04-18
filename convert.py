value = "Hello"
bit_value = 16


def ParseBinary(binaryValue):

    byte_list = [binaryValue[i:i+8] for i in range(0, len(binaryValue), 8)]
    ascii_list = [chr(int(byte, 2)) for byte in byte_list]
    parsed_value = "".join(ascii_list)
    return parsed_value

def ConvertToBinary(value):
    binary_list = []
    for c in value:
        code_point = ord(c)
        binary = bin(code_point)[2:].zfill(bit_value)
        binary_list.append(binary)
    binary_str = "".join(binary_list)
    return binary_str


output = ConvertToBinary(value)
print(output)
