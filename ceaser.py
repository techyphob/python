plain_text = input("Enter Plain Text: ")
shift = input("Enter shift value: ")
while not shift.isdigit():
    shift = input("Invalid shift value. Enter shift value: ")
shift = int(shift)
cipher_text = ''
for c in plain_text:
    if not c.isalpha():
        cipher_text += c
    elif c.islower():
        cipher_text += chr(97+((ord(c)-97)+shift)%26)
    else:
        cipher_text += chr(65+((ord(c)-65)+shift)%26)
print (cipher_text)
