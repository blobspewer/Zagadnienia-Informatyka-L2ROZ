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

def main():
    """Główna funkcja aplikacji w terminalu."""
    print("Aplikacja do konwersji z systemu szesnastkowego na ósemkowy")
    
    while True:
        hex_input = input("Wprowadź liczbę szesnastkową (lub 'exit' aby zakończyć): ").strip()
        
        if hex_input.lower() == 'exit':
            print("Zakończenie aplikacji.")
            break
        
        try:
            int(hex_input, 16) 
        except ValueError:
            print("Niepoprawna liczba szesnastkowa! Spróbuj ponownie.")
            continue
        
        oct_output = hex_to_oct(hex_input)
        print(f"System ósemkowy: {oct_output}")

if __name__ == "__main__":
    main()
