def cleanbin(string):
  return list(bin(string).replace('0b', ''))

def flip(string):
  for i in range(len(string)//2):
    string[i], string[len(string)-1-i] = string[len(string)-1-i], string[i]
  return string

def spaced(string):
  return (" ".join(["".join(flip(k)) for k in [string[j:j+4] for j in range(0, len(string), 4)][::-1]])) 

def nprint(length, string):
  nprint_out = spaced(flip(string))
  for i in range(length - len(nprint_out.replace(" ", ""))):
    nprint_out = "0" + nprint_out
  return nprint_out

def add(bin1, bin2):
  return cleanbin(int(bin1,2) + int(bin2,2))

def onescomp(string):
  return ''.join(['0' if i == '1' else '1' if i == '0' else 'x' for i in list(string)])

def color(string):
  string = f'{int(string,16):0>24b}'
  red = string[:8][:5]
  green = string[8:16][:6]
  blue = string[16:][:5]
  color = ''.join(red + green + blue)
  colors = [color[4*i:4*(i+1)] for i in range(4)]
  hexa = ''.join([hex(int(colors[i],2)).replace('0x', '') for i in range(len(colors))])
  return str(hexa).upper()


while True:
  try:
    output = input("[f > flip | a > add | one > 1's comp | two > 2's comp | bcd > BCD | color > convert 24-bit]\nDecimal: ")

    if output == "f":
      bindec = int(input("Binary: ").replace(" ", ""),2)
      print(f"Decimal: {bindec}\n")

    elif output == "a":
      bin1 = input("Bin1: ").replace(" ", "")
      bin2 = input("Bin2: ").replace(" ", "")
      addbin = add(bin1,bin2)
      longer = len(bin1) if len(bin1) > len(bin2) else len(bin2)
      print(f"Total: {nprint(longer, addbin)}\n")

    elif output == "one":
      oc_input = input("1's Complement (Binary): ").replace(" ", "")
      print(f"1's Complement: {nprint(len(oc_input), list(onescomp(oc_input)))}\n")

    elif output == "two":
      tc_input = input("2's Complement (Binary): ")

      if tc_input == "neg":
        for i in range(21):
          tc_input = cleanbin(int(i))
          for j in range(8 - len(tc_input)):
            tc_input = "0" + "".join(tc_input)
          tc_input = list(tc_input)
          plusone = (add(onescomp(tc_input), "1"))[-len(tc_input):]
          print(f"2's Complement: {nprint(len(tc_input), plusone)} | Decimal : -{i}")
      else:
        tc_input = tc_input.replace(" ", "")
        plusone = (add(onescomp(tc_input), "1"))[-len(tc_input):]
        print(f"2's Complement: {nprint(len(tc_input), plusone)}\n")

    elif output == "bcd":
      bcd_conv = input("from / to?: ")

      if bcd_conv == "from":
        bcd = list(input("BCD (Decimal): "))
        bcd_out = []
        for i in bcd:
          bcd_digit = "".join(cleanbin(int(i)))
          for j in range(4-len(bcd_digit)):
            bcd_digit = "0" + bcd_digit
          bcd_out.append(bcd_digit)
        print(f"BCD from Decimal: {' '.join(bcd_out)}\n")

      if bcd_conv == "to":
        bcd = input("BCD (Binary): ").replace(" ", "")
        bcd_bin = [str(int(j,2)) for j in [bcd[i*4:i*4+4] for i in range(len(bcd)//4)]]
        print(f"BCD to Decimal: {''.join(bcd_bin)}\n")
    
    elif output == "color":
      print(color(input("24-bit to 16-bit: ")), '\n')

    else:
      decbin = cleanbin(int(output))
      print(f"Binary: {nprint(len(decbin), decbin)}\n")

  except Exception as e:
    print(f"\nINVALID ENTRY : {e}\n")