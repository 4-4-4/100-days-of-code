alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caeser(text,shift,direction):
    cipher =""
    if direction == "encode":
        for n in text:
            i= alphabet.index(n)
            cipher+=alphabet[i+shift] 
        print("the encoded text is "+cipher)
    elif direction == "decode":
        shift += 26
        for n in text:
            i= alphabet.index(n)
            cipher+=alphabet[i-shift]
        print("the encoded text is "+cipher)  
    else:
        print("wrong input") 
caeser(text,shift,direction)