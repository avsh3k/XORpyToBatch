def xor_encrypt(input_string, key):
    """
    Encrypts the input string using XOR with the given key.
    """
    encrypted = []
    for char in input_string:
        encrypted.append(chr(ord(char) ^ key))
    return ''.join(encrypted)

def obfuscate_bat_file(input_file, output_file, key):
    """
    Obfuscates the .bat file using XOR with the given key.
    """
    with open(input_file, 'r') as file:
        original_content = file.read()
    
    obfuscated_content = xor_encrypt(original_content, key)
    
    with open(output_file, 'w') as file:
        file.write(obfuscated_content)

# Example usage
input_file = 'example.bat'
output_file = 'obfuscated_example.bat'
key = 42  # Key for XOR operation

obfuscate_bat_file(input_file, output_file, key)
print(f"{input_file} obfuscated and saved as {output_file} with XOR key {key}.")
