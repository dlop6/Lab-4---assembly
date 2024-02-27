

def binary_to_decimal(binary):
    binary = str(binary)
    
    if len(binary) != 8:
        return
    
    decimal = 0
    for i in range(8):
        decimal += int(binary[7-i]) * 2 ** i
    
    return decimal
        
def decimal_to_binary(decimal):

    
    binary = ""
    
    
    if decimal == 0:
        return "0"
    
    while decimal >= 1:
        
        integer_part = int(decimal) 
        
        residuo = integer_part % 2 
        
        binary = str(residuo) + binary 

        decimal = int(decimal) // 2 
    
    return binary  

def mantissa_to_binary(frac, bitCount=23):
    binary = ""
    while bitCount:
        frac *= 2
        bit = int(frac)
        if bit == 1:
            frac -= bit
            binary += "1"
        else:
            binary += "0"
        bitCount -= 1
    return binary


def decimal_to_IEEE754(decimal):
    sign_bit = "0" if decimal >= 0 else "1"
    decimal = abs(decimal)
    
    # Convert decimal to binary
    int_part = int(decimal)
    frac_part = decimal - int_part

    int_binary = decimal_to_binary(int_part)

    # Normalize the fractional part
    frac_binary = mantissa_to_binary(frac_part)

    # Calculate the exponent and mantissa
    if int_binary == '0':  # If the number is less than 1
        exponent_bits = bin(127 - 1)[2:].zfill(8)
        mantissa = frac_binary[:23]
    else:
        exponent = len(int_binary) - 1
        exponent_bits = bin(127 + exponent)[2:].zfill(8)
        mantissa = int_binary[1:] + frac_binary
        mantissa = mantissa[:23]  # Trim or pad mantissa to 23 bits

    ieee754_representation = sign_bit  + exponent_bits  + mantissa

    return ieee754_representation
            


def IEEE754_to_decimal(binary_number):
    if len(binary_number) != 32:
        return
    
    signo = (-1) ** int(binary_number[0]) 
    
    exponente = binary_to_decimal(binary_number[1:9]) - 127
    mantisa = binary_number[9:]
    mantisa_value = 0
    
    for i in range(0, len(mantisa)):
        mantisa_value += int(mantisa[i]) * (2 ** -(i + 1))
        
    decimal = signo * (1 + mantisa_value) * 2 ** exponente
    
    return decimal


   
ieee754 = decimal_to_IEEE754(9.452)
print(ieee754)

decimal = IEEE754_to_decimal(ieee754)
print(decimal)
    
    