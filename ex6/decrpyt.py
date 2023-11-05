def decrypt(string,shift):
    cipher = ""
    
    for char in string:
        if char == " ":
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) - shift - 65)%26 + 65)
        else:
            cipher += chr((ord(char) - shift - 97)%26 + 97)
    return cipher

text = input("Enter a string:")
s = int(input("Enter no of shift:"))
print("Original text:", text) 
print("After decrypted:",decrypt(text,s))               

