from converter import to_utf8, to_utf16, to_utf32
from translator import from_utf8, from_utf16, from_utf32


def validate_input(input:str) -> bool:
    '''
    Input should not be more than 8 HEXADECIMAL digits.
    '''
    if len(input) > 8:
        return False
    
    valid_chars = "0123456789ABCDEF"
    return all([ch in valid_chars for ch in input.upper()])

def generate_result_code() -> str:
    '''
    When user prompts output to text file, this will create the 'result_code'.txt
    '''
    with open('data.bin', 'rb+') as f:
        data = f.read()
        data = int(data, 10)
        code = 'result_' + str(data) + '.txt'
        data += 1
        f.write(bin(data))
        return code
        
    
def output_to_text(input: str, proc: tuple, output: str):
    '''
    When user prompts output to text file, this will write a formatted result.
    The `proc` tuple contains the parameters (convert|translat, result_type)
    '''
    f_string = f"You entered the code {input}. When {proc[0]}ed into {proc[1]}, the result is {output}."
    with open(generate_result_code(), 'w') as f:
        f.write(f_string)

if __name__ == "__main__":
    ini_string = input("Enter a hexadecimal string: ")

    print(validate_input(ini_string))
    