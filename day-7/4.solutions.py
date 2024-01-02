def utf8_encode(text):
    """
    Encode text to UTF-8.
    
    Args:
    text (str): The text to encode.
    
    Returns:
    bytes: The UTF-8 encoded bytes.
    """
    return text.encode('utf-8')

def utf8_decode(bytes_text):
    """
    Decode UTF-8 bytes to text.
    
    Args:
    bytes_text (bytes): The UTF-8 encoded bytes.
    
    Returns:
    str: The decoded text.
    """
    return bytes_text.decode('utf-8')


my_text = "salam | سلام"
my_text_encoded = utf8_encode(my_text)
my_text_decoded = utf8_decode(my_text_encoded)

print(my_text)
print(my_text_encoded)
print(my_text_decoded)
