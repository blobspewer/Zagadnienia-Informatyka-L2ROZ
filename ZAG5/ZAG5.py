def hex_to_bin(hex_str):
    """Konwertuje liczbę szesnastkową na binarną."""
    bin_str = bin(int(hex_str, 16))[2:]  
    return bin_str.zfill(len(hex_str) * 4)  

def bin_to_oct(bin_str):
    """Konwertuje liczbę binarną na ósemkową."""
    bin_str = bin_str.zfill((len(bin_str) + 2) // 3 * 3)
    
    oct_str = ""
    for i in range(0, len(bin_str), 3):
        oct_digit = int(bin_str[i:i+3], 2)
        oct_str += str(oct_digit)
    
    return oct_str

def hex_to_oct(hex_str):
    """Konwertuje liczbę szesnastkową na ósemkową."""
    bin_str = hex_to_bin(hex_str)

    oct_str = bin_to_oct(bin_str)
    
    return oct_str

hex_input = "1e2e"
oct_output = hex_to_oct(hex_input)
print(f"Hexadecimal: {hex_input}")
print(f"Octal: {oct_output}")
