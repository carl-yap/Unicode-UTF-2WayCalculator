from converter import to_utf8, to_utf16, to_utf32
from translator import from_utf8, from_utf16, from_utf32
from datetime import datetime


def validate_input(input:str) -> bool:
    '''
    Input should not be more than 8 HEXADECIMAL digits.
    '''
    if len(input) > 8:
        return False
    
    valid_chars = "0123456789ABCDEF"
    return all([ch in valid_chars for ch in input.upper()])

def generate_result_code() -> str:
    """
    Generates a unique code based on the current date and time.
    This ensures each filename will be unique.
    """
    # Get the current date and time
    now = datetime.now()
    
    # Format the datetime object as a string with a custom format
    # Example format: 'result_YYYYMMDD_HHMMSSmmm.txt'
    # Where 'mmm' is milliseconds
    timestamp = now.strftime('%Y%m%d_%H%M%S%f')
    code = f"result_{timestamp}.txt"
    
    return code
        
    
def output_to_text(input: str, proc: tuple, output: str):
    '''
    When user prompts output to text file, this will write a formatted result.
    The `proc` tuple contains the parameters (convert|translat, result_type)
    '''
    filename = generate_result_code()
    f_string = f"You entered the code {input}. When {proc[0]}ed into {proc[1]}, the result is {output}."
    with open(filename, 'w') as f:
        f.write(f_string)
    return filename

if __name__ == "__main__":
    ini_string = input("Enter a hexadecimal string: ")

    print(validate_input(ini_string))
    