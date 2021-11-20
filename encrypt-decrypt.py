encrypt_code = {'a':'j', 'b':'f', 'c':'a', 'd':'i', 'e':'s', 'f':'w', 'g':'l', 'h':'r', 'i':'p', 'j':'c', 'k':'v', 'l':'o',
'm':'u', 'n':'x', 'o':'g', 'p':'n', 'q':'t', 'r':'h', 's':'b', 't':'k', 'u':'q','v':'e','w':'y','x':'m', 'y':'z', 'z':'d'}

decrypt_code = {'a':'c', 'b':'s', 'c':'j', 'd':'z', 'e':'v', 'f':'b', 'g':'o', 'h':'r', 'i':'d', 'j':'a', 'k':'t', 'l':'g',
'm':'x', 'n':'p', 'o':'l', 'p':'i', 'q':'u', 'r':'h', 's':'e', 't':'q', 'u':'m','v':'k','w':'f','x':'n', 'y':'w', 'z':'y'}



def encrypt():
    message = input('Enter your message: ')
    translated = ''

    for i in message:
        if i in encrypt_code.keys():
            translated += (encrypt_code.get(i))
        elif i.lower() in encrypt_code.keys():
            i=i.lower()
            translated += (encrypt_code.get(i)).upper()
        elif i not in encrypt_code.keys():
            translated+=i
    print('Encrypted code: {}'.format(translated))


def decrypt():
    message = input('Enter code to decrypt: ')
    translated = ''

    for i in message:
        if i.islower():
            if i in decrypt_code.keys():
                translated += (decrypt_code.get(i))
        elif i.isupper():
            if i.lower() in decrypt_code.keys():
                translated+=(decrypt_code.get(i.lower())).upper()
        elif i.isspace():
            translated+=' '  
        elif i not in encrypt_code.keys():
            translated+=i  
    print('Decrypted code: {}'.format(translated))

def start():

    print("WELCOME TO ENCRYPT-DECRYPT")
    print("1. Encrypt\n2. Decrypt\n3. Exit")
    ch = input('Enter Choice: ')
    if ch=='1':
        encrypt()
        print('\n')
        start()
    elif ch=='2':
        decrypt()
        print('\n')
        start()
    elif ch=='3':
        exit()
    else:
        print('Wrong Choice')
        print('\n')
        start()
start()