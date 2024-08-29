# Simple bin method
deci = 24
bindeci = bin(deci)
print(bindeci)
#removing 0b
bindeci = bindeci[2:]
print(bindeci)
print(type(bindeci))
print(list(bindeci))

# Without bin function :
def deci2bin(decimal):
    if(decimal == 0):
        return "0"
    bin = ""
    while(decimal > 0):
        rem = decimal % 2
        bin = str(rem) + bin
        decimal = decimal // 2
    return bin


# binary to decimal
def bin2deci(binary):
    deci = 0
    binlen = len(binary)
    for i in range(binlen):
        if(binary[binlen-i-1] == "1"):
            deci += 2 ** i
    return deci

print(deci2bin(24))
print(deci2bin(100))
print(bin2deci("1010"))