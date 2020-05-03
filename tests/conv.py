#By Joshua Perez
hexa = {
    'a' : 10,
    'b' : 11,
    'c' : 12,
    'd' : 13,
    'e' : 14,
    'f' : 15
}
bina = { #do we need 0?
    '1' : '0001',
    '2' : '0020',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'a' : '1010',
    'b' : '1011',
    'c' : '1100',
    'd' : '1101',
    'e' : '1110',
    'f' : '1111'
}

#NEED TO BE ABLE TO READ FILES FROM TRACE AND OUTPUT
ex = "s 0x1fffff78"
array = []
i = 0

for l in ex:
    if i < 2:
        i +=1
        continue
    else:
        array.append(l)

print(array)

print("\nHexadecimal")
for letter in array:
    if letter in hexa:      #maybe make this a function and just call it?
        for key, value in hexa.items():
            if key == letter:
                print(value)
            else:
                continue
    else:
        print(letter)

print("\nBinary")
for letter in array:
    if letter in bina:      #maybe make this a function and just call it?
        for key, value in bina.items():
            if key == letter:
                print(value)
            else:
                continue
    else:
        print(letter)
        