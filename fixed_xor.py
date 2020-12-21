hex_string1 = input("Enter a hex string: ")
hex_string2 = input("Enter another hex string: ")
hex_array1 = bytearray.fromhex(hex_string1)
hex_array2 = bytearray.fromhex(hex_string2)
xored_array = []
for i in range(len(hex_array1)):
    xored_array.append(hex_array1[i] ^ hex_array2[i])
print(''.join(format(x, '02x') for x in xored_array))

