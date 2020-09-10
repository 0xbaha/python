# custom for decimal-to-binary conversion

def print_binary(dec_in,digit_in):
    bin_in = bin(dec_in)
    biner_length = len(bin_in[2:]) # length of binary output without prefix 0b
    bin_out = bin(dec_in)
    print('Length of binary output =', biner_length)
    print('Binary number of',dec_in,'(use prefix 0b)     =', bin_out) # binary output use prefix 0b
    print('Binary number of',dec_in,'(without prefix 0b) =', bin_out[2:]) # binary output without prefix 0b
    return

def custom_dec2bin(dec_in,digit_in):
    bin_in = bin(dec_in)
    biner_length = len(bin_in[2:]) # length of binary output without prefix 0b
    biner_prefix = ''
    if biner_length < digit_in:
        for i in range(0,digit_in-biner_length):
            biner_prefix = biner_prefix + '0'
    bin_out = biner_prefix + bin_in[2:] # binary output without prefix 0b
    return bin_out

def generate_bin_table(dec_in,digit_in):
    table_out =[]
    for i in range(0,dec_in+1):
        table_out.append(custom_dec2bin(i,digit_in))
    return table_out

def check_input(dec_in,digit_in):
    bin_in = bin(dec_in)
    bin_len = len(bin_in[2:])
    while digit_in < bin_len:
        digit_in = int(input('Digit number: '))
    decimal_out = dec_in
    digit_out = digit_in
    return decimal_out,digit_out

input_number = int(input("Enter decimal number: "))
digit_number = int(input("Digit number: "))
valid_in,valid_digit = check_input(input_number,digit_number)
print()
print_binary(valid_in,valid_digit)
print()
print('Generated Binary Table:')
bin_table = generate_bin_table(valid_in,valid_digit)
for i in bin_table:
    print(i)
