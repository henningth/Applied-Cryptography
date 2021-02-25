"""
Exercise 7: Implement a fixed-XOR function using the instructions here: https://cryptopals.com/sets/1/challenges/2

Given two equal length buffers, returns their XOR combination.
"""

input1 = "1c0111001f010100061a024b53535009181c"
input2 = "686974207468652062756c6c277320657965"
output = "746865206b696420646f6e277420706c6179"

def xor(input1, input2):
    input1int = int(input1, 16)
    input2int = int(input2, 16)
    result = input1int ^ input2int
    return result

result = xor(input1, input2)

if result == int(output, 16):
    print("They match.")
    
print(int(output, 16))
print(result)

utf8_input = "1c0111001f010100061a024b53535009181c"
utf8_key = "686974207468652062756c6c277320657965"

def convert(hex_string):
    utf_hex_string = bytes.fromhex(hex_string).decode("latin-1")
    return utf_hex_string

utf8_input_converted = convert(utf8_input)
utf8_key_converted = convert(utf8_key)
output_converted = convert(output)

xor_string = "".join(chr(ord(x) ^ ord(y)) for x, y in zip(utf8_input_converted, utf8_key_converted))

print(xor_string)
print(output_converted)