# File : caesar.py
#   Program sederhana untuk enkripsi dan dekripsi string menggunakan algoritma
#   kriptografi Caesar.
#   Referensi tabel ASCII: http://www.asciitable.com/

def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

#check the above function
# text = "BELAJAR KRIPTOGRAFI"
# s = 3 #key

text = input("Plaintext: ")
s = input("kunci rahasia = ") 
s = int(s)

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text,s))
