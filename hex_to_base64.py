import base64

def dec_to_byte(decimal):
    byte = format(decimal, 'b')
    if len(byte) != 8:
        byte = "0" * (8 - len(byte)) + byte
    return byte

def binary_to_dec(binary):
    num = 0
    for i in range(len(binary)):
        num += int(binary[-(i + 1)]) * (2 ** i)
    return num

def hex_to_base64_manual(hex_string):
    b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_rep = ""
    b64_rep = ""
    hex_array = bytearray.fromhex(hex_string)
    for num in hex_array:
        binary_rep += dec_to_byte(num)
    if len(binary_rep) % 6 != 0:
        binary_rep += "0" * (6 - (len(binary_rep) % 6))
    for i in range(len(binary_rep) // 6):
        b64_rep += b64[binary_to_dec(binary_rep[6 * i : 6 * i + 6])]
    return b64_rep

def hex_to_base64(hex_string):
    hex_array = bytearray.fromhex(hex_string)
    base64_string = base64.b64encode(hex_array)
    return base64_string.decode()

hex_string = (input("Enter a hex string: "))
print(hex_to_base64_manual(hex_string))
print(hex_to_base64(hex_string))