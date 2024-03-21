from converter import to_utf8, to_utf16, to_utf32
from translator import from_utf8, from_utf16, from_utf32


def validate_input(input:str) -> bool:
    if len(input) > 8:
        return False
    
    valid_chars = "0123456789ABCDEF"
    return all([ch in valid_chars for ch in input.upper()])

if __name__ == "__main__":
    ini_string = input("Enter a hexadecimal string: ")

    print(validate_input(ini_string))
     