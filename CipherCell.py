alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaSize=len(alphabet)

def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(text,shift,direction)

def whatToDoNow(answer):
    if answer == "yes":
        main()
    elif answer == "no":
        exit()
    else:
        print('----------------------- \n try again with valid input')
        whatNext=input('Do you want to encode/Decode Again(yes/no): ')
        whatToDoNow(whatNext)

def cipher(text , shift, direction):
    if shift>alphaSize:
        shift= shift % alphaSize

    finalText = ""

    if direction=='decode':
        shift= shift * -1

    for i in text:
        if i in alphabet:
            index_cipher= alphabet.index(i) + shift
            if index_cipher  >= alphaSize:
                index_cipher -= alphaSize
            finalText += alphabet[index_cipher]

        else:
            finalText += i

    print(f"The {direction}d text is: {finalText}\n----------------------- ")
    whatNext=input('Do you want to encode/Decode Again(yes/no): ')
    whatToDoNow(whatNext)

main()

