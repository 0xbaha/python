input_number = int(input("Enter decimal number: "))
output_dec2bin = bin(input_number)
biner_length = len(output_dec2bin[2:]) # length of binary output without prefix 0b
digit_number = int(input("Digit number: "))
while digit_number < biner_length:
    digit_number = int(input("Digit number: "))
biner_prefix = ''
if biner_length < digit_number:
    for i in range(0,digit_number-biner_length):
        biner_prefix = biner_prefix + '0'
print('Length of binary output =', biner_length)
print('Binary number of',input_number,'(use prefix 0b)     =', biner_prefix+output_dec2bin) # binary output use prefix 0b
print('Binary number of',input_number,'(without prefix 0b) =', biner_prefix+output_dec2bin[2:]) # binary output without prefix 0b
