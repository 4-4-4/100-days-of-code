import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text,shift,direction):
    cipher =""
    if direction == "decode":
        shift *=-1
    for n in text:
        if n not in alphabet:
            cipher+=n
        else:
            i= alphabet.index(n)
            cipher+=alphabet[i+shift] 
    print(f"the {direction}d text is {cipher}.")

print(art.logo)
repeat ="yes"
while repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift %26
    caeser(text,shift,direction)
    repeat = input("would you like to restart? yes/no\n")
else:
    print("goodbye ^_^")
