alphabet_chr_int = {}
start = 97
stop = 123

for i in range(0, stop - start):
    alphabet_chr_int[chr(start + i)] = i

alphabet_int_chr = dict(zip(alphabet_chr_int.values(), alphabet_chr_int.keys()))
print(alphabet_int_chr)
print(alphabet_chr_int)
def shift_encode(message, shift):
    if shift < 1:
        return message
    length = len(alphabet_chr_int)
    temp_list = []
    for i in message:
        shift_position = alphabet_chr_int[i] + shift % length
        temp_list.append(alphabet_int_chr[shift_position])
    return ''.join(temp_list)


def shift_decode(message, shift):
    if shift < 1:
        return message
    length = len(alphabet_chr_int)
    temp_list = []
    for i in message:
        shift_position = alphabet_chr_int[i] - shift % length
        temp_list.append(alphabet_int_chr[shift_position])
    return ''.join(temp_list)

string = 'abcdefgh'
shift = 5
encode_string = shift_encode(string, shift)
decode_string = shift_decode(encode_string, shift)

print(string)
print(shift)
print(encode_string)
print(decode_string)