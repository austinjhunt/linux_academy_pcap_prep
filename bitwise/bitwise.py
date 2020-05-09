#!/usr/bin/env python3.7

class BW:
    def bitwise_and(self, a, b):
        """ Pass in two numbers in decimal. Get a walkthrough of performing bitwise and on those two numbers. """
        A,B,a,b,max_len = self.reuse(a,b)
        print("We want bitwise AND. Any column that is both 1s, we keep 1. Otherwise, we turn to 0.")
        bin_out = self.format_bin(self._pad_num(self._get_binary(A & B),max_len))
        print(bin_out)
        dec_out = self.bin2dec(bin_out)
        print(f"{bin_out} in binary is {dec_out} in decimal.")
        print(f"Thus, {A} & {B} = {dec_out}")
        return A & B
    def bitwise_or(self,a,b):
        """ Pass in two numbers in decimal. Get a walkthrough of performing bitwise OR on those two numbers. """
        A,B,a,b,max_len = self.reuse(a,b)
        print("We want bitwise OR. Any column that has at least one 1, we keep 1. If both 0, we turn to 0.")
        bin_out = self.format_bin(self._pad_num(self._get_binary(A | B),max_len))
        print(bin_out)
        dec_out = self.bin2dec(bin_out)
        print(f"{bin_out} in binary is {dec_out} in decimal.")
        print(f"Thus, {A} | {B} = {dec_out}")
        return A | B

    def bitwise_xor(self,a,b):
        """ Pass in two numbers in decimal. Get a walkthrough of performing bitwise XOR on those two numbers. """
        A,B,a,b,max_len = self.reuse(a,b)
        print("We want bitwise XOR. Any column that has exactly one 1 and one 0, we keep 1. Otherwise, we turn to 0.")
        bin_out = self.format_bin(self._pad_num(self._get_binary(A ^ B),max_len))
        print(bin_out)
        dec_out = self.bin2dec(bin_out)
        print(f"{bin_out} in binary is {dec_out} in decimal.")
        print(f"Thus, {A} ^ {B} = {dec_out}")
        return A ^ B

    def left_shift(self,a,num_to_shift):
        print(f"We are doing a left shift by {num_to_shift} bits. First, let's write our number ({a}) in binary.")
        bin_a = self.format_bin(self._get_binary(a))
        print(bin_a)
        print(f"We are shifting left by {num_to_shift} bits.")
        print(f"That is, we are essentially cutting off {num_to_shift} bits from the left of {bin_a}")
        f = self.shift_loop(bin_a,num_to_shift,"left")
        decv = self.bin2dec(f)
        print(f"So, the final value in binary is {f}, which is {decv} in decimal.")
        print("So...")
        print(f"{a} << {num_to_shift} = {decv}")
        return a << num_to_shift

    def right_shift(self,a,num_to_shift):
        print(f"We are doing a right shift by {num_to_shift} bits. First, let's write our number ({a}) in binary.")
        bin_a = self.format_bin(self._get_binary(a))
        print(bin_a)
        print(f"We are shifting right by {num_to_shift} bits.")
        print(f"That is, we are essentially cutting off {num_to_shift} bits from the right of {bin_a}")
        f = self.shift_loop(bin_a,num_to_shift,"right")
        decv = self.bin2dec(f)
        print(f"So, the final value in binary is {f}, which is {decv} in decimal.")
        print("So...")
        print(f"{a} >> {num_to_shift} = {decv}")
        return a << num_to_shift

    def shift_loop(self,binary_string,num_to_shift,direction):
        i = 0
        x = ""
        binary_string = binary_string.replace("0b","")
        if num_to_shift == 0:
            return "0b" + binary_string
        if direction == "left":
            # cut from left:
            while i <= num_to_shift:
                print(f"{i} bits => {binary_string[i:]}")
                x = binary_string[i:]
                i += 1
        else:
            l = len(binary_string)
            while i <= num_to_shift:
                print(f'{i} bits => {binary_string[:l-i]}')
                x = binary_string[:l-i]
                i += 1
        return "0b" + x

    def bin2dec(self, num):
        rev = str(num)[::-1]
        dec = 0
        for index,val in enumerate(rev):
            if val == '1':
                dec += 2 ** index
        return dec



    def reuse(self,a,b):
        A = a
        B = b # maintain originals
        print(f"{a} is {self._get_binary(a)} in binary, and {b} is {self._get_binary(b)} in binary.")
        bin_a = self._get_binary(a)
        bin_b = self._get_binary(b)
        max_len = max([len(bin_a),len(bin_b)])
        a = self.format_bin(self._pad_num(bin_a,max_len))
        b = self.format_bin(self._pad_num(bin_b,max_len))
        print("Let's align the values vertically.")
        print(a)
        print(b)
        return A,B,a,b,max_len

    def format_bin(self,numstr):
        return '0b' + numstr

    def _pad_num(self,num,full_length ):
        num = str(num)
        d = full_length - len(num)
        return '0' * d + num

    def _get_binary(self, n, exclude_leading_zero=False):
        """ Return binary string for number n """
        if n == 0 and not exclude_leading_zero:
            return '0'
        elif n == 0:
            return ''
        else:
            remainder = n % 2
            quotient = n // 2
            return self._get_binary(quotient,True) + str(remainder)


def main():
    b = BW()
    # Test get binary
    for i in range(50):
        assert b.format_bin(b._get_binary(i)) == bin(i),  f'Expected {bin(i)} for {i} but got {b._get_binary(i)}'

    for i in range(10):
        for j in range(11,20):
            b.bitwise_and(i,j)
            print("\n\n")
            b.bitwise_or(i,j)
            print("\n\n")
            b.bitwise_xor(i,j)
            print("\n\n")

            b.left_shift(j,i)
            print("\n\n")
            b.right_shift(j,i)
            print("\n\n")
if __name__ == "__main__":
    main()