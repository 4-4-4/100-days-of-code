alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift):  
    cipher =""
    for n in text:
        i= alphabet.index(n)
        cipher+=alphabet[i+shift]
        
    print("the encoded text is "+cipher)
def decrypt(text, shift):
    cipher =""
    shift += 26
    for n in text:
        i= alphabet.index(n)
        cipher+=alphabet[i-shift]
    print("the encoded text is "+cipher)
if direction==("encode"):
    encrypt(text, shift)

elif direction=="decode":
    decrypt(text, shift )

else:
    print("Wrong input")