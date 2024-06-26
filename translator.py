UC_LOWEST_UTF16 = 0xD800DC00
UC_HIGHEST_UTF16 = 0xDBFFDFFF

def bin2hex(bits):
    return hex(int(bits, 2))[2:].upper()

def hex2bin_z(digits):
    unit = ""
    for d in digits:
        d = bin(int(d, 16))[2:]
        unit += d.zfill(4)
    return unit

def leftpad_z(digits, length):
    n = len(digits)
    return "0" * (length-n) + digits if n < length else None

# UTF-8 to Unicode
def from_utf8(digits):
    unit = hex2bin_z(digits)

    if unit.startswith('0') and len(unit) == 8:
        return bin2hex(unit[1:])
    
    if unit.startswith('110') and len(unit) == 16:
        return bin2hex(unit[3:8] + unit[10:])
    
    if unit.startswith('1110') and len(unit) == 24:
        return bin2hex(unit[4:8] + unit[10:16] + unit[18:])
    
    if unit.startswith('11110') and len(unit) == 32:
        return bin2hex(unit[5:8] + unit[10:16] + unit[18:24] + unit[26:])
    
    return "Out of Range"

# UTF-16 to Unicode
def from_utf16(digits):
    if len(digits) <= 4:
        return hex(int(digits, 16))[2:].upper()

    n = int(digits, 16)
    if n < UC_LOWEST_UTF16 or n > UC_HIGHEST_UTF16:
        return "Out of Range"
    
    upper = int(digits[:4], 16) - 0xD800
    lower = int(digits[4:], 16) - 0xDC00

    unit = leftpad_z(bin(upper)[2:], 10) + leftpad_z(bin(lower)[2:], 10)
    unit = int(unit, 2) + 0x10000
    return bin2hex(bin(unit))

# UTF-32 to Unicode
def from_utf32(digits):
    return hex(int(digits, 16))[2:].upper()