# BitLab - Binary Logic and Arithmetic Tool
# First Year Python Project

# Truth tables stored in dictionaries for logic gate simulation
gate_and = {('0', '0'): '0', ('0', '1'): '0', ('1', '0'): '0', ('1', '1'): '1'}
gate_or  = {('0', '0'): '0', ('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '1'}
gate_xor = {('0', '0'): '0', ('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0'}

# List to record each run as a tuple: (op_name, val1, val2, output)
history = []
op_count = 0

active = True

while active:
    print("\n==================================")
    print("      BITLAB SIMULATION MENU      ")
    print("==================================")
    print("1. 8-Bit Two's Complement Converter")
    print("2. Binary Full Adder with Carries")
    print("3. Bitwise Logic Gates (AND, OR, XOR)")
    print("4. Parity & Set Bit Counter")
    print("5. View Previous Calculations")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ").strip()
    
    # 1. Two's Complement signed conversion
    if choice == '1':
        print("\n--- Two's Complement Signed Converter ---")
        mode = input("A: Decimal to Signed Binary | B: Signed Binary to Decimal: ").strip().lower()
        
        if mode == 'a':
            raw = input("Enter an integer (-128 to 127): ").strip()
            
            # input validation
            valid = True
            is_neg = False
            chk = raw
            
            if len(chk) == 0:
                valid = False
            else:
                if chk[0] == '-':
                    is_neg = True
                    chk = chk[1:]
                elif chk[0] == '+':
                    chk = chk[1:]
                
                if len(chk) == 0:
                    valid = False
                for digit in chk:
                    if digit not in "0123456789":
                        valid = False
                        break
                        
            if not valid:
                print("Error: Input is not a valid integer.")
                continue
                
            num = int(raw)
            if num < -128 or num > 127:
                print("Error: Value must be between -128 and 127.")
                continue
                
            # positive number conversion
            if num >= 0:
                t = num
                b_str = ""
                if t == 0:
                    b_str = "0"
                while t > 0:
                    b_str = str(t % 2) + b_str
                    t = t // 2
                final_bin = ("0" * (8 - len(b_str))) + b_str
            else:
                # negative number: magnitude -> flip -> add 1
                t = abs(num)
                b_str = ""
                while t > 0:
                    b_str = str(t % 2) + b_str
                    t = t // 2
                padded = ("0" * (8 - len(b_str))) + b_str
                
                # step 1: invert bits
                flipped = ""
                for b in padded:
                    if b == '0':
                        flipped = flipped + '1'
                    else:
                        flipped = flipped + '0'
                        
                # step 2: add 1
                final_bin = ""
                carry = 1
                i = 7
                while i >= 0:
                    bit_sum = int(flipped[i]) + carry
                    if bit_sum == 2:
                        final_bin = "0" + final_bin
                        carry = 1
                    elif bit_sum == 1:
                        final_bin = "1" + final_bin
                        carry = 0
                    else:
                        final_bin = "0" + final_bin
                        carry = 0
                    i = i - 1
                    
            print("Decimal Input :", num)
            print("8-Bit Result  :", final_bin)
            history.append(("Signed To Binary", str(num), "-", final_bin))
            op_count = op_count + 1
            
        elif mode == 'b':
            b_val = input("Enter an 8-bit binary pattern: ").strip()
            if len(b_val) != 8:
                print("Error: Must be exactly 8 bits.")
                continue
                
            valid_bits = True
            for ch in b_val:
                if ch not in "01":
                    valid_bits = False
                    break
            if not valid_bits:
                print("Error: Only 0 and 1 are allowed.")
                continue
                
            # MSB carries negative weight (-128)
            msb = int(b_val[0])
            dec_out = -1 * msb * (2 ** 7)
            
            p = 6
            for bit in b_val[1:]:
                dec_out = dec_out + (int(bit) * (2 ** p))
                p = p - 1
                
            print("Binary Pattern :", b_val)
            print("Decimal Value  :", dec_out)
            history.append(("Signed To Decimal", b_val, "-", str(dec_out)))
            op_count = op_count + 1
        else:
            print("Invalid mode selected.")
            
    # 2. Binary Full Adder
    elif choice == '2':
        print("\n--- Binary Full Adder ---")
        num1 = input("Enter first binary number : ").strip()
        num2 = input("Enter second binary number: ").strip()
        
        valid = True
        for ch in num1 + num2:
            if ch not in "01":
                valid = False
                break
                
        if not valid or len(num1) == 0 or len(num2) == 0:
            print("Error: Both inputs must be non-empty binary strings.")
            continue
            
        # pad to same length
        max_len = max(len(num1), len(num2))
        pad1 = ("0" * (max_len - len(num1))) + num1
        pad2 = ("0" * (max_len - len(num2))) + num2
        
        carry_line = ""
        sum_line = ""
        c = 0
        
        # add from right to left
        idx = max_len - 1
        while idx >= 0:
            s = int(pad1[idx]) + int(pad2[idx]) + c
            if s == 3:
                sum_line = "1" + sum_line
                c = 1
                carry_line = "1" + carry_line
            elif s == 2:
                sum_line = "0" + sum_line
                c = 1
                carry_line = "1" + carry_line
            elif s == 1:
                sum_line = "1" + sum_line
                c = 0
                carry_line = "0" + carry_line
            else:
                sum_line = "0" + sum_line
                c = 0
                carry_line = "0" + carry_line
            idx = idx - 1
            
        if c == 1:
            sum_line = "1" + sum_line
            carry_line = "1" + carry_line
        else:
            carry_line = "0" + carry_line
            
        print("\nAddition Trace:")
        print("Carry : " + carry_line)
        print("  A   :   " + pad1)
        print("+ B   :   " + pad2)
        print("-------------------")
        print("Sum   : " + sum_line)
        
        history.append(("Binary Addition", num1, num2, sum_line))
        op_count = op_count + 1
        
    # 3. Bitwise Logic Gates
    elif choice == '3':
        print("\n--- Bitwise Logic Gate Simulation ---")
        w1 = input("Enter binary word A: ").strip()
        w2 = input("Enter binary word B: ").strip()
        
        valid = True
        for ch in w1 + w2:
            if ch not in "01":
                valid = False
                break
                
        if not valid or len(w1) == 0 or len(w2) == 0:
            print("Error: Invalid binary input.")
            continue
            
        length = max(len(w1), len(w2))
        p1 = ("0" * (length - len(w1))) + w1
        p2 = ("0" * (length - len(w2))) + w2
        
        out_and = ""
        out_or = ""
        out_xor = ""
        
        for k in range(length):
            pair = (p1[k], p2[k])
            out_and = out_and + gate_and[pair]
            out_or  = out_or  + gate_or[pair]
            out_xor = out_xor + gate_xor[pair]
            
        print("\nGate Comparisons:")
        print("Word A   : " + p1)
        print("Word B   : " + p2)
        print("-------------------------")
        print("A AND B  : " + out_and)
        print("A OR B   : " + out_or)
        print("A XOR B  : " + out_xor)
        
        history.append(("Logic Gates", p1, p2, "AND:" + out_and + " OR:" + out_or + " XOR:" + out_xor))
        op_count = op_count + 1
        
    # 4. Bit Analysis & Parity
    elif choice == '4':
        print("\n--- Bit Analysis & Parity ---")
        stream = input("Enter binary stream: ").strip()
        
        valid = True
        for b in stream:
            if b not in "01":
                valid = False
                break
                
        if not valid or len(stream) == 0:
            print("Error: Invalid binary stream.")
            continue
            
        count_ones = 0
        count_zeros = 0
        for bit in stream:
            if bit == '1':
                count_ones = count_ones + 1
            else:
                count_zeros = count_zeros + 1
                
        if count_ones % 2 == 0:
            even_p = '0'
            odd_p = '1'
        else:
            even_p = '1'
            odd_p = '0'
            
        print("\nAnalysis Summary:")
        print("Total Bits  :", len(stream))
        print("Total 1s    :", count_ones)
        print("Total 0s    :", count_zeros)
        print("Even Parity : Append", even_p, "->", stream + even_p)
        print("Odd Parity  : Append", odd_p, "->", stream + odd_p)
        
        history.append(("Parity Analysis", stream, "-", "1s:" + str(count_ones) + ", EP:" + even_p))
        op_count = op_count + 1
        
    # 5. History Log
    elif choice == '5':
        print("\n--- Execution History ---")
        print("Total operations recorded:", op_count)
        if len(history) == 0:
            print("No calculations performed yet.")
        else:
            print("--------------------------------------------------")
            n = 1
            for item in history:
                print(str(n) + ". [" + item[0] + "]")
                if item[2] == "-":
                    print("   Input : " + item[1])
                else:
                    print("   Inputs: " + item[1] + " and " + item[2])
                print("   Result: " + item[3])
                n = n + 1
            print("--------------------------------------------------")
            
    # 6. Exit
    elif choice == '6':
        print("Exiting BitLab. Goodbye!")
        active = False
        
    else:
        print("Invalid selection. Please choose an option from 1 to 6.")