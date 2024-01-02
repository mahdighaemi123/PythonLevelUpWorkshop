# solution 1

import base64

def encode_to_base64(string):
    encoded = base64.b64encode(string.encode('utf-8'))
    return encoded.decode('utf-8')

def decode_from_base64(encoded_string):
    decoded = base64.b64decode(encoded_string)
    return decoded.decode('utf-8')


my_data = "salam"
my_data_encoded = encode_to_base64(my_data)
my_data_decoded = decode_from_base64(my_data_encoded)

print(my_data)
print(my_data_encoded)
print(my_data_decoded)