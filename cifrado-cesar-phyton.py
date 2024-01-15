texto = input()
if texto.isupper():
    abc= "abcdefghijklmnopqrstuvwxyz"
else:
    abc= "abcdefghijklmnopqrstuvwxyz"
    
cifrado=""
    
desplazamiento = int (input())

for c in texto:
    if c.isalpha():
        if c.isupper():
            cifrado += chr((ord(c) - ord('A') + desplazamiento) % 26 + ord('A'))
        else:
            cifrado += chr((ord(c) - ord('a') + desplazamiento) % 26 + ord('a'))
    else:
        cifrado += c
        
print(cifrado)