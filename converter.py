UTF8_UPPER_LIMIT = 0x1FFFFF
UTF16_UPPER_LIMIT = 0x10FFFF

def hex2bin(digits):
    return bin(int(digits, 16))[2:]

def bin2hex(bits):
    return hex(int(bits, 2))[2:].upper()

# Unicode to UTF-8
def to_utf8(digits):
    if int(digits, 16) > UTF8_UPPER_LIMIT:
        return "Out of range"
    
    res = hex2bin(digits)
    count = int(len(res) / 6)
    final = ""

    if int(digits, 16) <= 0x7F:
        pad = 7 - len(res)
        for i in range(pad):
            final = final + "0"
        final = "0" + final + res
        return bin2hex(final)
        
    else:
        for i in range(count):
            last_six = res[-6:]
            last_six = "10" + last_six
            final = last_six + " " + final
            res = res[:-6]
        first_byte = "1" * (count + 1) + "0"
        padding_length = 8 - len(first_byte + res)
        first_byte += "0" * padding_length + res
        final = first_byte + " " + final
        return ' '.join([bin2hex(byte) for byte in final.split()])

# Unicode to UTF-16
def to_utf16(digits):
    unit = int(digits, 16)
    if unit > UTF16_UPPER_LIMIT:
        return "Out of range"

    if unit < 0x10000:
        n = 4 - len(digits)
        unit = "0" * n + digits
        return ' '.join([unit[i:i+2] for i in range(0, 4, 2)])
    
    else:
        unit = unit - 0x10000
        unit = hex2bin(hex(unit)[2:])
        lower = int(bin2hex(unit[-10:]), 16) + 0xDC00
        upper = int(bin2hex(unit[:-10]), 16) + 0xD800
        unit = hex(upper)[2:] + hex(lower)[2:]
        unit = unit.upper()
        return ' '.join([unit[i:i+2] for i in range(0, 8, 2)])

# Unicode to UTF-32
def to_utf32(digits):
    n = 8 - len(digits)
    unit = "0" * n + digits
    return ' '.join([unit[i:i+2] for i in range(0, 8, 2)])