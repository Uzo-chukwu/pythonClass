import string


def encrypt(text, shift_key):
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    encrypted = ""
    for letter in text:
        if letter in upper_case:
            encrypted += upper_case[((upper_case.index(letter)) + shift_key) % 26]
        if letter in lower_case:
            encrypted += lower_case[((lower_case.index(letter)) + shift_key) % 26]

        else:
            encrypted += letter
    return encrypted
def decrypt(text, shift_key):
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    decrypted = ""
    for letter in text:
        if letter in upper_case:
            decrypted += upper_case[((upper_case.index(letter)) + shift_key) % 26]
        if letter in lower_case:
            decrypted += lower_case[((lower_case.index(letter)) + shift_key) % 26]
        else:
            decrypted += letter
    return decrypted





text_to_be_encrypted = input("Enter the text: ")
encrypted = encrypt(text_to_be_encrypted, 13)
print(encrypted)
decrypted = decrypt(encrypted, 13)
print(decrypted)

