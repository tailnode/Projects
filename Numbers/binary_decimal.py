#!/usr/bin/python3

def bin2dec(bin_num):
    dec_num = 0
    bin_str = str(bin_num)
    bin_len = len(bin_str)
    for i in range(bin_len-1):
        dec_num += (int(bin_str[i]) * 2) ** (bin_len - i - 1)
    dec_num += int(str(bin_num)[-1])

    return dec_num

def dec2bin(dec_num):
    if dec_num == 0:
        return 0

    remainder = []
    while dec_num > 0:
        remainder.append(str(dec_num % 2))
        dec_num //= 2
    remainder.reverse()

    return int(''.join(remainder))
    
def test():
    print("""
    1. binary to decimal
    2. decemal to binary
    """)

    select = input('enter your select\n')

    if select == '1':
        original_num = input('enter the number you want to convert\n')
        converted_num = bin2dec(int(original_num))
        print('binary number', original_num, 'convert to decimal is', str(converted_num))
    elif select == '2':
        original_num = input('enter the number you want to convert\n')
        converted_num = dec2bin(int(original_num))
        print('decimal number', original_num, 'convert to binary is', str(converted_num))
    else:
        print('your input is error')

if __name__ == '__main__':
    test()
